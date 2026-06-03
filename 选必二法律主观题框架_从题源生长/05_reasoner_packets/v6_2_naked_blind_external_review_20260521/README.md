# V6.2 裸题盲测外部二审包

用途：发送给 GPTPro 与 Claude Opus 4.7，要求它们以聪明零基础学生 + 严格阅卷人身份攻击 V6.2。

当前底座：65 题，61 formal / 4 reference_only / 0 missing。

当前稿件：27 strict core + 38 non-core guard/index/reference/boundary。

本包不允许外部模型把 reference_only 或 source-check 题升成 formal 满分闭环。
