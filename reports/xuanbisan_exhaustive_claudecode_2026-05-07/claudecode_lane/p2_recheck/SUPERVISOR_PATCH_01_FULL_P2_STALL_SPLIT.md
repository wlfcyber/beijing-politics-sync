# Supervisor Patch 01: full P2 run stalled, split required

Time: 2026-05-07 16:39 +08:00

The full P2 ClaudeCode run started real CLI processes but after more than five
minutes wrote no P2 decisions, patches, evidence, or acceptance files. This is
not acceptable for supervision because no file evidence exists.

Supervisor action:

1. Stop the full P2 process tree.
2. Split P2 into smaller source groups:
   - P2A: Chaoyang and Dongcheng source_ids, 17 manifest rows.
   - P2B: Fengtai, Shunyi, Tongzhou source_ids, 22 manifest rows.
3. Require each group to write group-prefixed four-file outputs.
4. Codex will merge group outputs into the canonical P2 four-file outputs only
   after both groups pass row/key QA.

Boundary: no Word/PDF/delivery is allowed in this phase.
