from __future__ import annotations

import json
import math
import time
from urllib.request import urlopen
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_JSON_DIR = DATA_DIR / "raw_wb_json"
TABLE_DIR = ROOT / "output" / "tables"
FIG_DIR = ROOT / "output" / "figures"

YEARS = list(range(2010, 2024))

INDICATORS = {
    "NY.GDP.PCAP.KD": "gdp_pc_const2015",
    "SL.GDP.PCAP.EM.KD": "gdp_per_worker_const2021ppp",
    "IT.NET.USER.ZS": "internet_users_pct",
    "IT.NET.BBND.P2": "fixed_broadband_per100",
    "IT.CEL.SETS.P2": "mobile_subs_per100",
    "NE.GDI.TOTL.ZS": "gross_capital_formation_pct_gdp",
    "NE.TRD.GNFS.ZS": "trade_pct_gdp",
    "SP.URB.TOTL.IN.ZS": "urban_pop_pct",
    "SE.TER.ENRR": "tertiary_enrollment_gross_pct",
    "TX.VAL.TECH.MF.ZS": "hightech_exports_pct_manufactured",
    "SP.POP.TOTL": "population_total",
    "NY.GDP.TOTL.RT.ZS": "natural_resource_rents_pct_gdp",
}

SOURCE_URLS = {
    "WDI country metadata": "https://api.worldbank.org/v2/country?format=json&per_page=400",
    "WDI indicator API": "https://api.worldbank.org/v2/country/all/indicator/{indicator}?format=json&per_page=20000",
}


def _betacf(a: float, b: float, x: float) -> float:
    max_iter = 200
    eps = 3.0e-12
    fpmin = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def regularized_incomplete_beta(a: float, b: float, x: float) -> float:
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def normal_two_sided_p(t_value: float) -> float:
    if pd.isna(t_value):
        return float("nan")
    return math.erfc(abs(float(t_value)) / math.sqrt(2))


def student_t_two_sided_p(t_value: float, df: int) -> float:
    if pd.isna(t_value) or df <= 0:
        return float("nan")
    t_abs = abs(float(t_value))
    x = df / (df + t_abs * t_abs)
    return regularized_incomplete_beta(df / 2.0, 0.5, x)


def wb_get(url: str, save_path: Path | None = None) -> list[dict]:
    with urlopen(url, timeout=60) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    if save_path is not None:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if not isinstance(payload, list) or len(payload) < 2:
        raise RuntimeError(f"Unexpected World Bank API payload for {url}")
    return payload[1]


def fetch_country_metadata() -> pd.DataFrame:
    rows = wb_get(SOURCE_URLS["WDI country metadata"], RAW_JSON_DIR / "country_metadata.json")
    out = []
    for row in rows:
        income = row.get("incomeLevel") or {}
        region = row.get("region") or {}
        out.append(
            {
                "country_code": row.get("id"),
                "country": row.get("name"),
                "income_level": income.get("value"),
                "region": region.get("value"),
            }
        )
    df = pd.DataFrame(out)
    df = df[df["region"].ne("Aggregates")].copy()
    return df


def fetch_indicator(indicator: str, name: str) -> pd.DataFrame:
    url = SOURCE_URLS["WDI indicator API"].format(indicator=indicator)
    rows = wb_get(url, RAW_JSON_DIR / f"{indicator}.json")
    out = []
    for row in rows:
        try:
            year = int(row.get("date"))
        except Exception:
            continue
        if year not in YEARS:
            continue
        code = row.get("countryiso3code")
        if not code:
            continue
        out.append(
            {
                "country_code": code,
                "year": year,
                name: row.get("value"),
            }
        )
    df = pd.DataFrame(out)
    if df.empty:
        return df
    df[name] = pd.to_numeric(df[name], errors="coerce")
    df = df.groupby(["country_code", "year"], as_index=False)[name].mean()
    return df


def build_panel() -> tuple[pd.DataFrame, pd.DataFrame]:
    countries = fetch_country_metadata()
    frames = []
    for indicator, name in INDICATORS.items():
        frames.append(fetch_indicator(indicator, name))
        time.sleep(0.15)

    panel = None
    for frame in frames:
        if panel is None:
            panel = frame
        else:
            panel = panel.merge(frame, on=["country_code", "year"], how="outer")
    if panel is None:
        raise RuntimeError("No WDI data fetched")

    panel = panel.merge(countries, on="country_code", how="left")
    panel = panel[panel["region"].notna()].copy()
    for col in INDICATORS.values():
        panel[col] = pd.to_numeric(panel[col], errors="coerce")

    return panel, countries


def add_variables(panel: pd.DataFrame) -> pd.DataFrame:
    df = panel.sort_values(["country_code", "year"]).copy()
    df["ln_gdp_pc"] = df["gdp_pc_const2015"].where(df["gdp_pc_const2015"] > 0).map(math.log)
    df["ln_gdp_per_worker"] = df["gdp_per_worker_const2021ppp"].where(
        df["gdp_per_worker_const2021ppp"] > 0
    ).map(math.log)
    df["ln_broadband"] = (1 + df["fixed_broadband_per100"]).map(lambda x: math.log(x) if pd.notna(x) and x > 0 else None)
    df["ln_mobile"] = (1 + df["mobile_subs_per100"]).map(lambda x: math.log(x) if pd.notna(x) and x > 0 else None)
    df["internet_10pct"] = df["internet_users_pct"] / 10.0
    df["broadband_10"] = df["fixed_broadband_per100"] / 10.0

    lag_cols = [
        "ln_broadband",
        "internet_10pct",
        "ln_mobile",
        "gross_capital_formation_pct_gdp",
        "trade_pct_gdp",
        "urban_pop_pct",
        "tertiary_enrollment_gross_pct",
    ]
    for col in lag_cols:
        df[f"L1_{col}"] = df.groupby("country_code")[col].shift(1)
        df[f"L2_{col}"] = df.groupby("country_code")[col].shift(2)

    df["is_high_income"] = df["income_level"].eq("High income").astype(int)
    resource_avg = df.groupby("country_code")["natural_resource_rents_pct_gdp"].transform("mean")
    pop_min = df.groupby("country_code")["population_total"].transform("min")
    df["exclude_small_or_resource"] = ((pop_min < 1_000_000) | (resource_avg > 20)).fillna(False)
    return df


def sample_log(df: pd.DataFrame) -> pd.DataFrame:
    steps = []
    steps.append(("raw_country_year", len(df), "all non-aggregate WDI country-year observations"))
    needed = [
        "ln_gdp_pc",
        "L1_ln_broadband",
        "L1_internet_10pct",
        "L1_gross_capital_formation_pct_gdp",
        "L1_trade_pct_gdp",
        "L1_urban_pop_pct",
    ]
    baseline = df.dropna(subset=needed)
    steps.append(("baseline_complete_cases", len(baseline), "complete cases for baseline FE regression"))
    countries = baseline["country_code"].nunique()
    steps.append(("baseline_countries", countries, "number of countries in baseline sample"))
    return pd.DataFrame(steps, columns=["step", "observations", "reason"])


def descriptive_table(df: pd.DataFrame) -> pd.DataFrame:
    vars_ = [
        "gdp_pc_const2015",
        "gdp_per_worker_const2021ppp",
        "internet_users_pct",
        "fixed_broadband_per100",
        "mobile_subs_per100",
        "gross_capital_formation_pct_gdp",
        "trade_pct_gdp",
        "urban_pop_pct",
        "tertiary_enrollment_gross_pct",
        "population_total",
        "natural_resource_rents_pct_gdp",
    ]
    rows = []
    for v in vars_:
        s = df[v].dropna()
        rows.append(
            {
                "variable": v,
                "N": int(s.shape[0]),
                "mean": s.mean(),
                "sd": s.std(),
                "p25": s.quantile(0.25),
                "median": s.quantile(0.5),
                "p75": s.quantile(0.75),
            }
        )
    return pd.DataFrame(rows)


def sample_composition(df: pd.DataFrame) -> pd.DataFrame:
    needed = [
        "ln_gdp_pc",
        "L1_ln_broadband",
        "L1_internet_10pct",
        "L1_gross_capital_formation_pct_gdp",
        "L1_trade_pct_gdp",
        "L1_urban_pop_pct",
    ]
    out = df.copy()
    out["baseline_sample"] = out[needed].notna().all(axis=1)
    rows = []
    for label, part in [
        ("baseline_sample", out[out["baseline_sample"]]),
        ("excluded_from_baseline", out[~out["baseline_sample"]]),
    ]:
        rows.append(
            {
                "group": label,
                "observations": int(part.shape[0]),
                "countries": int(part["country_code"].nunique()),
                "high_income_share": part["is_high_income"].mean(),
                "median_gdp_pc": part["gdp_pc_const2015"].median(),
                "median_fixed_broadband_per100": part["fixed_broadband_per100"].median(),
                "median_internet_users_pct": part["internet_users_pct"].median(),
                "median_population": part["population_total"].median(),
            }
        )
    return pd.DataFrame(rows)


def residualize_on_country_year(data: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    use = data.dropna(subset=[*cols, "country_code", "year"]).copy()
    country_dummies = pd.get_dummies(use["country_code"], prefix="cty", drop_first=True).reset_index(drop=True).astype(float)
    year_dummies = pd.get_dummies(use["year"], prefix="yr", drop_first=True).reset_index(drop=True).astype(float)
    Xfe = pd.concat([pd.Series(1.0, index=country_dummies.index, name="const"), country_dummies, year_dummies], axis=1)
    X = Xfe.to_numpy(dtype=float)
    out = {}
    for col in cols:
        y = use[col].astype(float).to_numpy().reshape(-1, 1)
        beta = np.linalg.pinv(X.T @ X) @ X.T @ y
        out[col] = (y - X @ beta).flatten()
    return pd.DataFrame(out)


def collinearity_diagnostics(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "L1_ln_broadband",
        "L1_internet_10pct",
        "L1_gross_capital_formation_pct_gdp",
        "L1_trade_pct_gdp",
        "L1_urban_pop_pct",
    ]
    resid = residualize_on_country_year(df, cols)
    corr = resid.corr()
    rows = []
    for col in cols:
        other = [c for c in cols if c != col]
        y = resid[col].to_numpy(dtype=float).reshape(-1, 1)
        X = pd.concat([pd.Series(1.0, index=resid.index, name="const"), resid[other]], axis=1).to_numpy(dtype=float)
        beta = np.linalg.pinv(X.T @ X) @ X.T @ y
        fitted = X @ beta
        ssr = float(((y - fitted).T @ (y - fitted))[0, 0])
        tss = float(((y - y.mean()).T @ (y - y.mean()))[0, 0])
        r2 = 1 - ssr / tss if tss else float("nan")
        rows.append(
            {
                "variable": col,
                "vif_after_country_year_fe": 1 / (1 - r2) if r2 < 1 else float("inf"),
                "corr_with_L1_ln_broadband_after_fe": corr.loc[col, "L1_ln_broadband"],
                "corr_with_L1_internet_10pct_after_fe": corr.loc[col, "L1_internet_10pct"],
            }
        )
    return pd.DataFrame(rows)


def fit_fe_ols(
    df: pd.DataFrame,
    yvar: str,
    xvars: list[str],
    cluster_col: str = "country_code",
    add_country_trends: bool = False,
) -> tuple[dict, pd.DataFrame]:
    needed = [yvar, cluster_col, "year", *xvars]
    data = df.dropna(subset=needed).copy()
    y = data[yvar].astype(float).to_numpy().reshape(-1, 1)

    x = data[xvars].astype(float).reset_index(drop=True)
    country_dummies = pd.get_dummies(data["country_code"], prefix="cty", drop_first=True).reset_index(drop=True)
    year_dummies = pd.get_dummies(data["year"], prefix="yr", drop_first=True).reset_index(drop=True)
    pieces = [
        pd.Series(1.0, index=x.index, name="const"),
        x,
        country_dummies.astype(float),
        year_dummies.astype(float),
    ]
    if add_country_trends:
        trend = (data["year"].astype(float) - data["year"].astype(float).mean()).reset_index(drop=True)
        country_all = pd.get_dummies(data["country_code"], prefix="ctytrend", drop_first=False).reset_index(drop=True).astype(float)
        country_trends = country_all.mul(trend, axis=0)
        pieces.append(country_trends)

    Xdf = pd.concat(pieces, axis=1)

    Xfe_df = pd.concat(
        [
            pd.Series(1.0, index=x.index, name="const"),
            country_dummies.astype(float),
            year_dummies.astype(float),
        ],
        axis=1,
    )
    X = Xdf.to_numpy(dtype=float)
    n, k = X.shape
    xtx_inv = np.linalg.pinv(X.T @ X)
    beta = xtx_inv @ X.T @ y
    resid = y - X @ beta

    clusters = data[cluster_col].to_numpy()
    meat = np.zeros((k, k))
    for cl in np.unique(clusters):
        idx = clusters == cl
        Xg = X[idx, :]
        ug = resid[idx, :]
        score = Xg.T @ ug
        meat += score @ score.T
    g = len(np.unique(clusters))
    correction = (g / (g - 1)) * ((n - 1) / (n - k)) if g > 1 and n > k else 1.0
    vcov = correction * xtx_inv @ meat @ xtx_inv
    se = np.sqrt(np.maximum(np.diag(vcov), 0.0)).reshape(-1, 1)
    tstat = beta / se

    y_mean = y.mean()
    ssr = float((resid.T @ resid)[0, 0])
    Xfe = Xfe_df.to_numpy(dtype=float)
    beta_fe = np.linalg.pinv(Xfe.T @ Xfe) @ Xfe.T @ y
    resid_fe = y - Xfe @ beta_fe
    ssr_fe = float((resid_fe.T @ resid_fe)[0, 0])
    partial_within_r2 = 1 - ssr / ssr_fe if ssr_fe else float("nan")
    tss = float(((y - y_mean).T @ (y - y_mean))[0, 0])
    r2 = 1 - ssr / tss if tss else float("nan")
    adj_r2 = 1 - (1 - r2) * (n - 1) / (n - k) if n > k and not np.isnan(r2) else float("nan")

    cluster_df = g - 1
    result = {
        "params": pd.Series(beta.flatten(), index=Xdf.columns),
        "bse": pd.Series(se.flatten(), index=Xdf.columns),
        "tstats": pd.Series(tstat.flatten(), index=Xdf.columns),
        "pvalues_normal": pd.Series([normal_two_sided_p(v) for v in tstat.flatten()], index=Xdf.columns),
        "pvalues_t_cluster_df": pd.Series([student_t_two_sided_p(v, cluster_df) for v in tstat.flatten()], index=Xdf.columns),
        "vcov": pd.DataFrame(vcov, index=Xdf.columns, columns=Xdf.columns),
        "cluster_count": g,
        "cluster_df": cluster_df,
        "nobs": n,
        "k": k,
        "rsquared_adj": adj_r2,
        "partial_within_r2": partial_within_r2,
        "xvars": xvars,
        "yvar": yvar,
        "add_country_trends": add_country_trends,
    }
    return result, data


def tidy_result(name: str, result, variables: list[str]) -> pd.DataFrame:
    rows = []
    for var in variables:
        if var not in result["params"].index:
            continue
        rows.append(
            {
                "model": name,
                "variable": var,
                "coef": result["params"][var],
                "se_cluster_country": result["bse"][var],
                "t_stat": result["tstats"][var],
                "p_value_normal": result["pvalues_normal"][var],
                "p_value_t_cluster_df": result["pvalues_t_cluster_df"][var],
                "cluster_df": int(result["cluster_df"]),
                "nobs": int(result["nobs"]),
                "adj_r2": result["rsquared_adj"],
            }
        )
    return pd.DataFrame(rows)


def linear_combo_result(name: str, result: dict, combo_name: str, terms: list[tuple[str, float]]) -> pd.DataFrame:
    indexes = result["params"].index
    missing = [term for term, _ in terms if term not in indexes]
    if missing:
        return pd.DataFrame()
    coef = 0.0
    weights = pd.Series(0.0, index=indexes)
    for term, weight in terms:
        coef += result["params"][term] * weight
        weights[term] = weight
    var = float(weights.T @ result["vcov"] @ weights)
    se = math.sqrt(max(var, 0.0))
    t_stat = coef / se if se > 0 else float("nan")
    return pd.DataFrame(
        [
            {
                "model": name,
                "variable": combo_name,
                "coef": coef,
                "se_cluster_country": se,
                "t_stat": t_stat,
                "p_value_normal": normal_two_sided_p(t_stat),
                "p_value_t_cluster_df": student_t_two_sided_p(t_stat, int(result["cluster_df"])),
                "cluster_df": int(result["cluster_df"]),
                "nobs": int(result["nobs"]),
                "adj_r2": result["rsquared_adj"],
            }
        ]
    )


def stars(p: float) -> str:
    if p < 0.01:
        return "***"
    if p < 0.05:
        return "**"
    if p < 0.1:
        return "*"
    return ""


def table_to_markdown(df: pd.DataFrame, path: Path) -> None:
    out = df.copy()
    for col in out.columns:
        if pd.api.types.is_float_dtype(out[col]):
            out[col] = out[col].map(lambda x: f"{x:.4f}" if pd.notna(x) else "")
    out = out.fillna("").astype(str)
    cols = list(out.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in out.iterrows():
        vals = [str(row[col]).replace("\n", " ").replace("|", "\\|") for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RAW_JSON_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    panel, countries = build_panel()
    panel.to_csv(DATA_DIR / "wdi_raw_panel.csv", index=False, encoding="utf-8-sig")
    countries.to_csv(DATA_DIR / "wdi_country_metadata.csv", index=False, encoding="utf-8-sig")

    df = add_variables(panel)
    df.to_csv(DATA_DIR / "analysis_panel.csv", index=False, encoding="utf-8-sig")

    sample = sample_log(df)
    sample.to_csv(TABLE_DIR / "sample_log.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(sample, TABLE_DIR / "sample_log.md")

    desc = descriptive_table(df)
    desc.to_csv(TABLE_DIR / "table1_descriptive.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(desc, TABLE_DIR / "table1_descriptive.md")

    composition = sample_composition(df)
    composition.to_csv(TABLE_DIR / "sample_composition.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(composition, TABLE_DIR / "sample_composition.md")

    coldiag = collinearity_diagnostics(df)
    coldiag.to_csv(TABLE_DIR / "collinearity_diagnostics.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(coldiag, TABLE_DIR / "collinearity_diagnostics.md")

    df["L1_ln_broadband_x_high_income"] = df["L1_ln_broadband"] * df["is_high_income"]
    df["L1_internet_10pct_x_high_income"] = df["L1_internet_10pct"] * df["is_high_income"]

    models = {
        "M1_baseline_gdppc": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M2_mobile_alt": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_mobile",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M3_labor_productivity": {
            "y": "ln_gdp_per_worker",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M4_add_education_control": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_tertiary_enrollment_gross_pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M5_trade_openness_proxy": {
            "y": "trade_pct_gdp",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M6_income_heterogeneity": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_ln_broadband_x_high_income",
                "L1_internet_10pct_x_high_income",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M7_country_trends": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
            "add_country_trends": True,
        },
        "M8_exclude_small_resource": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
            "filter": "not_small_resource",
        },
        "M9_L2_lag": {
            "y": "ln_gdp_pc",
            "x": [
                "L2_ln_broadband",
                "L2_internet_10pct",
                "L2_gross_capital_formation_pct_gdp",
                "L2_trade_pct_gdp",
                "L2_urban_pop_pct",
            ],
        },
        "M10_high_income_subsample": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
            "filter": "high_income",
        },
        "M11_non_high_income_subsample": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
            "filter": "non_high_income",
        },
        "M12_broadband_without_internet": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_ln_broadband",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
        "M13_internet_without_broadband": {
            "y": "ln_gdp_pc",
            "x": [
                "L1_internet_10pct",
                "L1_gross_capital_formation_pct_gdp",
                "L1_trade_pct_gdp",
                "L1_urban_pop_pct",
            ],
        },
    }

    all_rows = []
    key_vars = [
        "L1_ln_broadband",
        "L1_internet_10pct",
        "L1_ln_mobile",
        "L1_tertiary_enrollment_gross_pct",
        "L1_ln_broadband_x_high_income",
        "L1_internet_10pct_x_high_income",
        "L1_ln_broadband_high_income_marginal",
        "L1_internet_10pct_high_income_marginal",
        "L2_ln_broadband",
        "L2_internet_10pct",
    ]
    full_x_rows = []
    model_meta = []
    for name, spec in models.items():
        model_df = df.copy()
        if spec.get("filter") == "not_small_resource":
            model_df = model_df[~model_df["exclude_small_or_resource"]].copy()
        elif spec.get("filter") == "high_income":
            model_df = model_df[model_df["is_high_income"].eq(1)].copy()
        elif spec.get("filter") == "non_high_income":
            model_df = model_df[model_df["is_high_income"].eq(0)].copy()
        res, used = fit_fe_ols(model_df, spec["y"], spec["x"], add_country_trends=spec.get("add_country_trends", False))
        key_part = tidy_result(name, res, key_vars)
        full_x_rows.append(tidy_result(name, res, spec["x"]))
        if name == "M6_income_heterogeneity":
            m6_combo = [
                linear_combo_result(
                    name,
                    res,
                    "L1_ln_broadband_high_income_marginal",
                    [("L1_ln_broadband", 1.0), ("L1_ln_broadband_x_high_income", 1.0)],
                ),
                linear_combo_result(
                    name,
                    res,
                    "L1_internet_10pct_high_income_marginal",
                    [("L1_internet_10pct", 1.0), ("L1_internet_10pct_x_high_income", 1.0)],
                ),
            ]
            combos = pd.concat([part for part in m6_combo if not part.empty], ignore_index=True)
            key_part = pd.concat([key_part, combos], ignore_index=True)
            full_x_rows.append(combos)
        all_rows.append(key_part)
        model_meta.append(
            {
                "model": name,
                "nobs": int(res["nobs"]),
                "countries": int(used["country_code"].nunique()),
                "adj_r2": res["rsquared_adj"],
                "partial_within_r2": res["partial_within_r2"],
                "country_trends": bool(res["add_country_trends"]),
                "country_fe": True,
                "year_fe": True,
                "cluster": "country_code",
                "cluster_count": int(res["cluster_count"]),
                "cluster_df": int(res["cluster_df"]),
                "filter": spec.get("filter", ""),
                "dependent_variable": spec["y"],
                "xvars": ", ".join(spec["x"]),
            }
        )

    reg = pd.concat(all_rows, ignore_index=True)
    reg["stars"] = reg["p_value_t_cluster_df"].map(stars)
    reg.to_csv(TABLE_DIR / "regression_results_tidy.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(reg, TABLE_DIR / "regression_results_tidy.md")

    full_reg = pd.concat(full_x_rows, ignore_index=True)
    full_reg["stars"] = full_reg["p_value_t_cluster_df"].map(stars)
    full_reg.to_csv(TABLE_DIR / "regression_results_all_xvars.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(full_reg, TABLE_DIR / "regression_results_all_xvars.md")

    meta = pd.DataFrame(model_meta)
    meta.to_csv(TABLE_DIR / "model_metadata.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(
        meta[
            [
                "model",
                "dependent_variable",
                "nobs",
                "countries",
                "adj_r2",
                "partial_within_r2",
                "country_fe",
                "year_fe",
                "country_trends",
                "cluster",
                "cluster_count",
                "cluster_df",
                "filter",
            ]
        ],
        TABLE_DIR / "model_metadata.md",
    )

    source_ledger = {
        "downloaded_at_local": time.strftime("%Y-%m-%d %H:%M:%S"),
        "years": YEARS,
        "source_urls": SOURCE_URLS,
        "indicators": INDICATORS,
        "notes": [
            "World Bank WDI country-year panel excludes aggregate regions.",
            "Key digital variables are lagged by one year before regression.",
            "Regressions include country and year fixed effects and cluster standard errors by country.",
            "Reported significance stars use Student-t p-values with country-cluster degrees of freedom.",
            "The design is associational fixed-effects evidence, not a definitive causal estimate.",
        ],
    }
    (DATA_DIR / "source_ledger.json").write_text(json.dumps(source_ledger, ensure_ascii=False, indent=2), encoding="utf-8")

    var_dict = pd.DataFrame(
        [
            {"variable": k, "definition": v, "source_indicator": k if k in INDICATORS else ""}
            for k, v in {
                **INDICATORS,
                "ln_gdp_pc": "Log of GDP per capita, constant 2015 US dollars",
                "ln_gdp_per_worker": "Log of GDP per person employed, constant 2021 PPP dollars",
                "L1_ln_broadband": "One-year lag of log(1 + fixed broadband subscriptions per 100 people)",
                "L1_internet_10pct": "One-year lag of internet users share, scaled by 10 percentage points",
                "L1_ln_mobile": "One-year lag of log(1 + mobile cellular subscriptions per 100 people)",
                "is_high_income": "World Bank high-income economy dummy",
            }.items()
        ]
    )
    var_dict.to_csv(TABLE_DIR / "variable_dictionary.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(var_dict, TABLE_DIR / "variable_dictionary.md")

    plot_df = reg[reg["variable"].isin(["L1_ln_broadband", "L1_internet_10pct"])].copy()
    plot_df = plot_df[plot_df["model"].isin(["M1_baseline_gdppc", "M3_labor_productivity", "M4_add_education_control"])]
    plot_df["ci_low"] = plot_df["coef"] - 1.96 * plot_df["se_cluster_country"]
    plot_df["ci_high"] = plot_df["coef"] + 1.96 * plot_df["se_cluster_country"]
    plot_df.to_csv(TABLE_DIR / "coef_plot_data.csv", index=False, encoding="utf-8-sig")
    table_to_markdown(plot_df[["model", "variable", "coef", "ci_low", "ci_high"]], TABLE_DIR / "coef_plot_data.md")

    print(json.dumps({"ok": True, "rows": len(df), "countries": df["country_code"].nunique(), "years": YEARS}, ensure_ascii=False))


if __name__ == "__main__":
    main()
