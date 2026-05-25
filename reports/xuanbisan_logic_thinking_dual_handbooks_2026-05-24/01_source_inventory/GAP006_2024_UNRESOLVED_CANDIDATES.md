# GAP006 2024 Unresolved Candidates

Status: `open_unresolved_not_promoted`

Purpose: record 2024 elective-3 candidates visible in the 2024一模分类汇编 cache but not yet safe to promote because raw district paper and/or official answer-key evidence was not recovered locally in this pass.

Source cache:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\4b25cddd4dc2992d_2024届各区一模试题分类汇编选必3.md`

## Not Promoted

| candidate | cache lines | reason not promoted | needed evidence |
|---|---:|---|---|
| 2024门头沟一模 Q14 | around `:42-49` | 吉祥物“宸宸”形象设计题，只在分类汇编中见到题面和选项；本机 `2024各区一模` 原始目录未找到 2024门头沟一模原卷或官方答案键。 | Raw paper plus official answer key or formal explanation. |
| 2024房山一模 Q6 | around `:220-225` | 中国式现代化传统/现代、连续性/飞跃性选择题，只在分类汇编中见到题面和选项；本机 `2024各区一模` 原始目录未找到 2024房山一模原卷或官方答案键。 | Raw paper plus official answer key or formal explanation. |
| 2024房山一模 Q7 | around `:268-272` | 写北京的联想思维/聚合思维/形象思维选择题，只在分类汇编中见到题面和选项；本机 `2024各区一模` 原始目录未找到 2024房山一模原卷或官方答案键。 | Raw paper plus official answer key or formal explanation. |
| 2024房山一模 Q8 | around `:87-92` | 演绎推理错误组合选择题，只在分类汇编中见到题面和选项；本机 `2024各区一模` 原始目录未找到 2024房山一模原卷或官方答案键。 | Raw paper plus official answer key or formal explanation. |

## Already Promoted But Still Needs Raw Upgrade

| row | candidate | current level | remaining issue |
|---|---|---|---|
| Q0069 | 2024门头沟一模 Q20 | `B-compilation` | Needs raw district paper and formal rubric/answer to upgrade beyond compilation level. |
| Q0070 | 2024房山一模 Q20(1) | `B-compilation` | Needs raw district paper and formal rubric/answer to upgrade beyond compilation level. |

## Current Local Source Tree Finding

During this pass, the local 2024一模 source tree contained district folders for 东城、丰台、朝阳、海淀、石景山、西城, but not 2024门头沟一模 or 2024房山一模. Therefore 门头沟/房山 choice candidates remain unresolved and must not be counted as source-locked coverage.

## Gate Rule

Do not promote these unresolved candidates from classification cache alone unless at least one of the following is recovered:

- original district paper plus official answer key;
- official teacher-version paper with embedded answer key;
- formal scoring rule / marking-rule file;
- another independently checkable official source that locks both prompt and answer.
