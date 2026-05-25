# GAP001 Source Lock: 2024朝阳二模 Q7

Status: `closed_source_locked_pending_external_review`

This file closes GAP001 / BLK-002 at the local source-evidence level. It does not close GPT Pro, Claude V4/V5, Governor, Confucius, or final delivery gates.

## Source

- paper: `gpt_sources/9223488a4b5e6f80_003202405朝阳高三二模政治试题.md:96-114`
- answer key: `gpt_sources/f7c4cc4ac52ecefd_004202405朝阳高三政治质量检测二参考答案_以PDF为准.md:24-44`
- raw paper: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模\2024朝阳二模\试卷\003202405朝阳高三二模政治试题.pdf`
- raw answer: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模\2024朝阳二模\其他材料\004202405朝阳高三政治质量检测二参考答案（以PDF为准）.docx`

The formal scoring-detail PDF is a subjective-question marking summary and does not separately analyze Q7. The objective answer key confirms Q7 answer `D`.

## Paper Text

7. 科学思维离不开逻辑。下列表述中，合乎逻辑的是

A. 自媒体是思想政治教育的工具，自媒体也是娱乐的工具，所以，娱乐工具都是思想政治教育的工具。

B. 归纳推理是从个别性前提推出一般性结论的推理。我学过归纳推理，所以，我能推出一般性结论和新知识体系。

C. 只有既弄清对象的性质，又了解对象之间的关系，才能对对象有较为全面的把握。我善于弄清对象的性质，所以，我特别善于进行关系判断。

D. 如果推理结构不正确，也就是说，前提和结论的逻辑联系方式是错误的，那么，尽管前提真实，也不能保证推出正确的结论。

Answer key: `D`.

## Local Decision

Add as `Q0029` under reasoning choice-trap coverage.

- A is the core trap for the handbook: a categorical syllogism with minor-term illicit process. In “自媒体也是娱乐的工具”, the minor term “娱乐工具” is a predicate of an affirmative proposition and is not distributed; in the conclusion “娱乐工具都是思想政治教育的工具”, the same minor term becomes the subject of a universal affirmative proposition and is distributed. This violates “前提中不周延的项，结论中也不得周延”.
- B is invalid because “学过归纳推理” does not mean “能进行归纳推理”, and the conclusion expands from “推出一般性结论” to “推出一般性结论和新知识体系”.
- C misuses a necessary-condition judgment: satisfying only one conjunct, “弄清对象的性质”, cannot establish the full necessary condition, nor can it infer “善于进行关系判断”.
- D is correct because valid inferential form is required to guarantee the conclusion from true premises; if the logical link is wrong, true premises do not guarantee a true conclusion.

Teaching boundary:

- The old B-line placeholder said this was “小项不当扩大” and needed paper/answer confirmation. That confirmation is now complete.
- This row is source-locked locally, but still pending external review before release.
