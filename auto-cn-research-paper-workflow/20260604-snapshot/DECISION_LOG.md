# DECISION_LOG

| Time | Decision | Reason | Boundary |
| --- | --- | --- | --- |
| 2026-06-04T21:24:50+0800 | Treat this as a Mac migration/resync verification step, not a final paper run. | Device changed from Windows to Mac, so browser, local materials, scripts, and tests must be freshly verified. | Do not claim final readiness until the workflow matrix says `final_user_goal_ready=yes`. |
| 2026-06-04T21:24:50+0800 | Keep GPT/Claude final-review gates limited to visible web/App sessions. | User explicitly requires real webpage/App review records. | CLI/API can advise during skill-building but cannot satisfy final approval. |
| 2026-06-04T21:43:34+0800 | Promote Mac material gate to ready after current-device redownload and provenance rebuild. | S-001 to S-007 were redownloaded through RUC/CNKI, all 15 formal sources have current Mac source/text files, and provenance validates with file hashes. | Still not final: keyword-derived anchors and missing visible GPT/Claude pass reviews block `final_user_goal_ready`. |
