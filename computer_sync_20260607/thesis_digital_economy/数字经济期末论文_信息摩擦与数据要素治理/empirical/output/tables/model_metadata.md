| model | dependent_variable | nobs | countries | adj_r2 | partial_within_r2 | country_fe | year_fe | country_trends | cluster | cluster_count | cluster_df | filter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1_baseline_gdppc | ln_gdp_pc | 2067 | 179 | 0.9951 | 0.0604 | True | True | False | country_code | 179 | 178 |  |
| M2_mobile_alt | ln_gdp_pc | 2114 | 179 | 0.9952 | 0.0725 | True | True | False | country_code | 179 | 178 |  |
| M3_labor_productivity | ln_gdp_per_worker | 1950 | 162 | 0.9929 | 0.0481 | True | True | False | country_code | 162 | 161 |  |
| M4_add_education_control | ln_gdp_pc | 1539 | 154 | 0.9966 | 0.0799 | True | True | False | country_code | 154 | 153 |  |
| M5_trade_openness_proxy | trade_pct_gdp | 2069 | 178 | 0.9622 | 0.0333 | True | True | False | country_code | 178 | 177 |  |
| M6_income_heterogeneity | ln_gdp_pc | 2067 | 179 | 0.9951 | 0.0639 | True | True | False | country_code | 179 | 178 |  |
| M7_country_trends | ln_gdp_pc | 2067 | 179 | 0.9990 | 0.8336 | True | True | True | country_code | 179 | 178 |  |
| M8_exclude_small_resource | ln_gdp_pc | 1596 | 131 | 0.9966 | 0.1510 | True | True | False | country_code | 131 | 130 | not_small_resource |
| M9_L2_lag | ln_gdp_pc | 1908 | 177 | 0.9956 | 0.0578 | True | True | False | country_code | 177 | 176 |  |
| M10_high_income_subsample | ln_gdp_pc | 768 | 65 | 0.9814 | 0.0196 | True | True | False | country_code | 65 | 64 | high_income |
| M11_non_high_income_subsample | ln_gdp_pc | 1299 | 114 | 0.9860 | 0.0996 | True | True | False | country_code | 114 | 113 | non_high_income |
| M12_broadband_without_internet | ln_gdp_pc | 2142 | 179 | 0.9950 | 0.0714 | True | True | False | country_code | 179 | 178 |  |
| M13_internet_without_broadband | ln_gdp_pc | 2131 | 180 | 0.9951 | 0.0458 | True | True | False | country_code | 180 | 179 |  |
