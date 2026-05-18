# Beijing Politics Master Governor

This folder is the project-wide supervision inbox for the Beijing Gaokao politics system.

Canonical generated files:

- `latest_master_governor_report.md`: newest whole-project supervision report.
- `worker_daily_orders.md`: instructions that each subproject AI must read before acting.
- `context_compression_manifest.csv`: files over the context-size threshold and their generated context capsules.
- `context_capsules/`: deterministic summaries for oversized text/log/context files.
- `adaptive_rules_ledger.md`: durable self-learning rules accepted by the project governor.
- `self_learning_register.csv`: candidate lessons, recurring failures, and accepted adaptations.

Run manually:

```bash
python3 scripts/master_governor.py report \
  --workspace "/Users/wanglifei/Desktop/北京高考政治" \
  --sync-root "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync"
```

The script writes reports both to the desktop project and to this sync repo so another machine can absorb the same control state.
