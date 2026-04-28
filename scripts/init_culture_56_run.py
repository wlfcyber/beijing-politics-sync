import csv
import shutil
from datetime import datetime
from pathlib import Path


REPO = Path(r"C:\bp_sync_visible")
RUN = REPO / "reports" / "culture_all_suites_rerun_2026-04-29"
PHILO_RUN = REPO / "reports" / "full_all_suites_independent_rerun_2026-04-29"
TEMPLATE = Path(r"C:\Users\Administrator\Desktop\01_北京政治资料\必修四文化材料-知识触发总框架_持续更新版.md")
ARTIFACT_TEMPLATE = REPO / "artifacts" / "必修四文化材料-知识触发总框架_持续更新版.md"


def read(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def copy(src, dst):
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main():
    for sub in [
        "worker_outputs",
        "worker_reports",
        "governor_reports",
        "patcher_reports",
        "student_outputs",
        "audit",
        "scripts",
        "logs",
    ]:
        (RUN / sub).mkdir(parents=True, exist_ok=True)

    template_src = TEMPLATE if TEMPLATE.exists() else ARTIFACT_TEMPLATE
    copy(template_src, RUN / "USER_CULTURE_TEMPLATE.md")
    copy(REPO / "reports" / "必修四文化_2024-2026题源穷尽清单.md", RUN / "prior_必修四文化_2024-2026题源穷尽清单.md")
    copy(REPO / "reports" / "必修四文化_细则文化题逐题复核表.md", RUN / "prior_必修四文化_细则文化题逐题复核表.md")
    copy(REPO / "reports" / "必修四文化_细则文化题复核队列.md", RUN / "prior_必修四文化_细则文化题复核队列.md")
    copy(PHILO_RUN / "SUITE_ROSTER.csv", RUN / "SUITE_ROSTER.csv")
    copy(PHILO_RUN / "COVERAGE_MATRIX.csv", RUN / "PHILOSOPHY_V6_COVERAGE_MATRIX.csv")

    task = f"""# 必修四文化 56 套全量重跑任务书

创建时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 目标

- 按用户提供过的文化模板，重跑 56 套北京政治试卷的文化线。
- 产出学生版文化框架、文化选择题触发链、审计证据、覆盖矩阵和最终 Word。
- 不沿用哲学 v6 的粗筛文化文档作为最终成果；哲学 v6 只能作为题源和客观证据参考。

## 模板骨架

1. 0 载体：文化载体、文化符号、展示平台、精神标识。
2. 1 特点：源远流长、博大精深。
3. 2 作用：引领风尚、教育人民；服务社会、推动发展。
4. 3 横向：文化交流与传播。
5. 4 纵向：文化的继承与发展；融通不同资源实现综合创新；立足时代之基回应时代问题；创造性转化、创新性发展。
6. 5 建设文化强国，树立文化自信。
7. 6 民族精神。
8. 7 坚持习近平文化思想。

## 证据规则

- 主观题：只用正式评分细则、评标、阅卷报告、讲评给分口径，普通参考答案不能升级为主观文化细则。
- 选择题：必须有题干和可靠答案键，才能写正确项/错肢链。
- 交叉题：经济、政治、法律题中的文化词，只有细则给文化分时才入 A 类；否则只登记边界。
- 不能用“文化”等泛词新造答题点；必须落回 0-7 框架。
"""
    (RUN / "TASK_BRIEF.md").write_text(task, encoding="utf-8")

    roles = """# 角色契约

- 决策者：盯住下一批缺口，不允许因已有旧文化框架就停止。
- 劳动者：按套卷处理文化主观题和文化选择题，写明证据等级。
- 补丁者：检查一材多点是否漏挂到 0-7 多个位置，尤其文化功能/双创/文化自信/民族精神交叉。
- 监管者：拒绝参考答案冒充细则、拒绝题号漂移、拒绝选择题无答案键硬写。
- 自动化检测者：核对 56 套覆盖矩阵、worker 输出、学生版、审计版、Word 渲染是否一致。
"""
    (RUN / "ROLE_CONTRACTS.md").write_text(roles, encoding="utf-8")

    progress = f"""# Progress

- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: 初始化文化 56 套独立重跑目录；已复制用户文化模板、旧文化复核表、哲学 v6 题源清单和覆盖矩阵。
- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: 确认本轮不用哲学 v6 的文化粗筛 Word 作为终稿，必须按文化模板重新落库。
"""
    (RUN / "PROGRESS.md").write_text(progress, encoding="utf-8")

    decision = """# Decision Log

- 文化线采用用户 0-7 模板；不新增总章节。
- A 类逐点标分、B 类等级细则支持、C 类材料识别词必须分清。
- 文化主观题和文化选择题分册处理，但最终学生版可合并为文化框架 Word。
"""
    (RUN / "DECISION_LOG.md").write_text(decision, encoding="utf-8")

    thread_registry = """# Thread Registry

| role | agent_id | assignment | write_scope | status | last_report |
| --- | --- | --- | --- | --- | --- |
"""
    (RUN / "THREAD_REGISTRY.md").write_text(thread_registry, encoding="utf-8")

    rows = []
    roster = RUN / "SUITE_ROSTER.csv"
    if roster.exists():
        with roster.open("r", encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rows.append(
                    {
                        "suite_id": r["suite_id"],
                        "year": r["year"],
                        "district": r["district"],
                        "stage": r["stage"],
                        "suite_name": r["suite_name"],
                        "culture_subjective_status": "pending",
                        "culture_choice_status": "pending",
                        "framework_slots": "",
                        "evidence_level": "pending",
                        "worker": "",
                        "governor_status": "pending",
                        "blocker": "",
                    }
                )
    fields = list(rows[0].keys()) if rows else [
        "suite_id",
        "year",
        "district",
        "stage",
        "suite_name",
        "culture_subjective_status",
        "culture_choice_status",
        "framework_slots",
        "evidence_level",
        "worker",
        "governor_status",
        "blocker",
    ]
    with (RUN / "COVERAGE_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"initialized {RUN}")


if __name__ == "__main__":
    main()
