 <center>
    <h1>马浩杰</h1>
    <div>
        <span>
            <img src="assets/phone-solid.svg" width="18px">
            18151681382
        </span>
        ·
        <span>
            <img src="assets/envelope-solid.svg" width="18px">
            1137633684@qq.com
        </span>
    </div>
</center>

 ## <img src="assets/info-circle-solid.svg" width="30px"> 个人信息 

  男，1994 年出生                                求职意向：算法工程师                               工作经验：约5年

  技能清单: 3D目标检测，强化学习(DQN, PPO, GRPO, GSPO)，VLM，LLM微调和蒸馏，c++, cuda.

## <img src="assets/graduation-cap-solid.svg" width="30px"> 教育经历

- 硕士，南京大学，计算机科学与技术专业，2017.9~2020.7

- 学士，南京大学，计算机科学与技术专业，2013.9~2017.7
## <img src="assets/briefcase-solid.svg" width="30px"> 工作经历
- **元戎启行，perception 算法工程师, 2023.1~至今**
- **小马智行，perception 算法工程师, 2021.8~2022.12**
- **微软中国 公司，m365 部门，SDE, 2020.6~2021.7**

## <img src="assets/project-diagram-solid.svg" width="30px"> 科研经历
- AttnSense: Multi-level Attention Mechanism For Multimodal Human Activity Recognition (**Ijcai 2019, CCF A**, attention多模态融合)
- Unsupervised Human Activity Representation Learning with Multi-task Deep Clustering (**UbiComp 2020, CCF A**, 无监督预训练相关)

## <img src="assets/tools-solid.svg" width="30px"> 项目经历


### **项目一：交通标志识别（TSR）感知模块(元戎启行)**

  - 项目描述：负责自动驾驶量产车端的交通标志识别（TSR）模块，覆盖限速标牌、可变车道标志、收费站通行标志三大场景，支撑城区/高速/匝道全场景限速决策与车道级路径规划。
  - 限速标牌识别：
    - 支持100+类限速标志检测与分类（最高/最低/解除限速，5-130 km/h全速段）
    - 设计时序平滑机制，基于历史帧投票策略（滑动窗口投票 + 置信度加权）抑制单帧误检，提升连续帧识别稳定性
    - 结合SD地图与RAS地图实现标牌-车道关联：通过DFS构建前方路径拓扑，区分主路/匝道限速标志，解决匝道场景下主路标牌误触发问题
    - 实现多相机融合的标牌跟踪与深度估计（前视+周视），跟踪缓存距离达120米
  - 可变车道标志识别：
    - 支持12类可变车道标志检测（左转/右转/直行/掉头及组合方向），并于感知车道线进行绑定，辅助决策系统实现车道级路径规划
  - 收费站通行标志识别：
    - 支持6类收费站标志识别（ETC专用/人工通道/ETC+人工/免费车道/货车专用/关闭），融合SD地图收费站位置信息（200米范围判定），实现收费站区域精准进出判定与标牌过滤

### **项目二：自动驾驶场景理解与风险分类系统(元戎启行)**

  - 项目描述：负责自动驾驶场景理解模块开发，对行车环境进行多维度联合分类（天气/光照/区域/路面/风险等 60+ 细分标签），为下游感知与决策模块提供场景上下文，支撑感知策略动态切换与风险预警。经历从传统 CNN 分类到 VLA 大模型的架构演进。
  - V1 — 多分支 CNN 分类架构：
    - 设计 SceneMultiBranchHead，针对天气(8类)、光照(5类)、区域(10类)、路面(7类)四个维度使用独立分类分支，解决多任务间类别语义差异大、互相干扰的问题
    - 混合损失：互斥类别采用 Softmax Loss，可共现类别（区域）采用 Asymmetric Loss（gamma\_neg=9, gamma\_pos=1）缓解类别不平衡；引入 learnable\_weights 自动平衡四分支损失
    - 构建车端数据挖掘 → 云端挖掘 → 模型预标注 → 自动质检 → 人工质检的数据闭环流水线
  - V2 — VLA 大模型架构升级：
    - 模型架构：基于 Qwen2.5-VL / InternVL + Qwen2 多模态大模型，相机图像经 Vision Encoder、BEV 特征图(26通道)经 CNN Encoder、导航信息经 Embedding Tables 分别编码后，通过 masked\_scatter 注入 LLM embedding 序列由 Transformer 统一建模；设计场景模式 token 注入 prompt，引导输出结构化场景描述与二值风险标志
    - 数据构造：构建 positive/negative 对照样本格式，支持多标签；56 万样本，风险/非风险约 4:6，存在严重长尾分布（高频积水 10% vs 低频减速带 0.006%）
    - GRPO 训练：设计 scene\_tags\_reward，风险类用 F0.5（偏精确率）、非风险类用 F1；按频率与安全关键性分层加权（低频关键风险 ×8，主导非风险 ×0.4）；风险类 FP 重惩罚（-0.8）防止误接管
    - 评估：多标签 per-category IoU/F0.5/mAP（分风险/非风险组）+ 二值风险 Precision/Recall + LLM-as-Judge 12 维场景描述逐帧打分

### **项目三：点云检测和分割(小马智行)**

  - 项目描述： 复现并优化 Waymo 顶刊论文 Range Sparse Net (RSN)，构建一套兼顾 Range View (RV) 语义分割与 BEV 目标检测的端到端感知框架。
  - 模型架构: 
    - 在RV视角使用U-Net进行3D语义分割(类似occ)，识别噪点，地面点，背景点，行人车辆等信息，损失函数使用Focal Loss + Lovász-Softmax Loss
    - 目标检测在BEV视角进行，模型架构采用Sparse CNN + SSD/CenterPoint Head, 损失函数采用多任务损失，包含分类损失(focal loss), 回归损失(l1 loss), Direction Loss：专门用于处理朝向角的周期性问题
    - 稀疏卷积网络输入为经过 Range View 分割过滤后的点云，背景点已被去除，输入的具体形式为非零点的空间坐标 $(x, y, z)$, 稀疏卷积通过cuda实现，具体机制为结合哈希表和Rule Book(卷积核输出点对应的输入坐标),有了 Rule Book，计算过程就变成了矩阵乘法（GEMM），这让稀疏卷积在 GPU 上的执行速度飞快

### **项目四: 数据血缘系统与集群监控(微软)**
  - 数据血缘系统：基于编译原理实现 SCOPE 语法解析器（AST），构建 Cosmos 平台 PB 级数据的表级与字段级血缘图谱；基于血缘清理 180 天无调用冷数据，节省约 12% 存储开销，并满足 GDPR 合规溯源需求
  - 集群监控系统：集成 Cosmos QPS/RT/失败率与硬件指标，接入 Azure 时序异常检测服务（SR-CNN + 孤立森林），实现非平稳时序实时监控，相较阈值告警漏报率降低 18%
