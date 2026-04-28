# Handoff Queue

- pending: 子线程按年份和阶段处理后，将 worker report 写回本目录。
- pending: 任一 worker 完成后，优先补开独立监管者线程，复核 worker 输出与补丁者发现。
- pending: 所有 worker 完成后，由主线程合并 `worker_outputs/*.csv`，再生成最终三大文件候选稿。
