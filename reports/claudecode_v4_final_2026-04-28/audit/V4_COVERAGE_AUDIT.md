# v4 真实套卷覆盖审计

## 结论

旧 v3 完成结论撤销。它把 2025/2026 的父级聚合目录当成套卷，导致真实套卷没有逐套闭环。

- 真实套卷目录：55
- 旧 v3 精确套卷名覆盖：14
- 旧 v3 精确套卷名未覆盖：41
- 新文本抽取文件：180

## 旧产物的核心错误

1. `suite` 字段错误：`2025各区一模`、`2025各区二模`、`2025各区期末`、`2026各区一模`、`2026各区期末和期中` 是父目录，不是套卷。
2. 最终 MD/Word 错误地按题目/来源堆列，没有按用户既有必修四哲学框架组织。
3. `FINAL_ACCEPTANCE_REPORT.md` 中的完成判断不能成立；必须以本文件的真实套卷矩阵重新验收。

## 新验收门槛

- `CANONICAL_SUITE_INVENTORY.csv` 每一行都必须有 `repair_status` 终态。
- 终态只能是 `included`、`module-boundary-excluded`、`reference-only`、`objective-key-only`、`source-missing`、`ocr-needed`、`conversion-needed`、`blocked`。
- 最终成果必须先按用户原哲学框架节点组织，再在节点内列来源证据。
- 不能再把题目顺序表包装成最终框架。

## 未被旧 v3 精确覆盖的真实套卷

- S015｜2025｜2025东城一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025东城一模｜文件状态：ok:2;skip:1
- S016｜2025｜2025丰台一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025丰台一模｜文件状态：ok:2
- S017｜2025｜2025延庆一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025延庆一模｜文件状态：ok:2
- S018｜2025｜2025房山一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025房山一模｜文件状态：ok:2;skip:1
- S019｜2025｜2025朝阳一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025朝阳一模｜文件状态：failed:Namespace prefix w for pos on tab is not defined, line 1, column 1202 (<string>, line 1):1;ocr-needed:1;ok:4
- S020｜2025｜2025海淀一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025海淀一模｜文件状态：ok:3
- S021｜2025｜2025石景山一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025石景山一模｜文件状态：ok:2
- S022｜2025｜2025西城一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025西城一模｜文件状态：ok:2
- S023｜2025｜2025门头沟一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025门头沟一模｜文件状态：ok:2
- S024｜2025｜2025顺义一模｜/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025顺义一模｜文件状态：ok:2
- S025｜2025｜2025东城二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025东城二模｜文件状态：ok:2
- S026｜2025｜2025丰台二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025丰台二模｜文件状态：ok:9;skip:4
- S027｜2025｜2025昌平二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025昌平二模｜文件状态：ok:2
- S028｜2025｜2025朝阳二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025朝阳二模｜文件状态：ocr-needed:1;ok:2
- S029｜2025｜2025海淀二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模｜文件状态：ocr-needed:1;ok:3
- S030｜2025｜2025西城二模｜/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025西城二模｜文件状态：ok:2
- S031｜2025｜2025东城期末｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末｜文件状态：ok:3;skip:1
- S032｜2025｜2025丰台期末｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025丰台期末｜文件状态：ok:2
- S033｜2025｜2025朝阳期末｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025朝阳期末｜文件状态：ocr-needed:1;ok:2
- S034｜2025｜2025海淀期中｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期中｜文件状态：ok:2
- S035｜2025｜2025海淀期末｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末｜文件状态：ok:2
- S036｜2025｜2025西城期末｜/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025西城期末｜文件状态：ok:2
- S037｜2026｜2026东城一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模｜文件状态：ocr-needed:2;ok:10
- S038｜2026｜2026丰台一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模｜文件状态：ocr-needed:1;ok:1
- S039｜2026｜2026延庆一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026延庆一模｜文件状态：ok:2
- S040｜2026｜2026房山一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026房山一模｜文件状态：ocr-needed:1;ok:1
- S041｜2026｜2026朝阳一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026朝阳一模｜文件状态：ok:2
- S042｜2026｜2026海淀一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模｜文件状态：ocr-needed:1;ok:1;skip:1
- S043｜2026｜2026石景山一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026石景山一模｜文件状态：ok:2
- S044｜2026｜2026西城一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026西城一模｜文件状态：ocr-needed:1;ok:2
- S045｜2026｜2026门头沟一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模｜文件状态：ok:2
- S046｜2026｜2026顺义一模｜/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模｜文件状态：ok:2
- S047｜2026｜2026东城期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末｜文件状态：ok:2
- S048｜2026｜2026丰台期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026丰台期末｜文件状态：ocr-needed:1;ok:1
- S049｜2026｜2026朝阳期中｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中｜文件状态：ok:3
- S050｜2026｜2026朝阳期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末｜文件状态：ocr-needed:2
- S051｜2026｜2026海淀期中｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期中｜文件状态：ocr-needed:1;ok:1
- S052｜2026｜2026海淀期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期末｜文件状态：ok:2
- S053｜2026｜2026西城期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末｜文件状态：ocr-needed:1;ok:2;skip:1
- S054｜2026｜2026通州期末｜/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末｜文件状态：ok:2
- S055｜2026｜2026石景山期末｜/Users/wanglifei/Desktop/2026模拟题/已放弃/2026石景山期末｜文件状态：ok:1;skip:1
