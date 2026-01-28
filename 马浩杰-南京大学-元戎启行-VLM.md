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
- **元戎启行，perception 算法工程师, 2023.2~2026.1**
- **小马智行，perception 算法工程师, 2021.8~2022.10**
- **微软中国 公司，m365 部门，SDE, 2020.6~2021.7**

## <img src="assets/project-diagram-solid.svg" width="30px"> 科研经历(总引用量350+)
- AttnSense: Multi-level Attention Mechanism For Multimodal Human Activity Recognition (**Ijcai 2019, CCF A**, attention多模态融合)
- Unsupervised Human Activity Representation Learning with Multi-task Deep Clustering (**UbiComp 2020, CCF A**, 无监督预训练相关)

## <img src="assets/tools-solid.svg" width="30px"> 项目经历

### **项目一: 基于VLA架构的端到端自动驾驶大模型(元戎启行)**
  - 项目背景：构建统一的多模态自动驾驶大模型，旨在实现从感知理解到决策规划的端到端闭环
  构建具备场景理解，轨迹输出，风险评估能力的统一模型
  - 技术细节：
    - 模型整体架构
      - 基座模型采用Qwen2-VL 7B架构，整体参数量8B，精度为FP8.
      - 输入为BEV特征,导航地图，感知地图等多模态信息，输出为场景描述、轨迹规划、限速信息、纵横向规划、风险标志, 引入COT输出设计，要求模型在生成轨迹前先输出场景语义描述与意图预测
    - 预训练
      - 构建了异构数据混合训练，将通用视觉-语言数据集与自动驾驶数据集（大规模BEV-描述对）进行混合训练
      - 未来考虑结合Masked World Modeling (MWM) 思想，让模型在未标注的海量路测视频中学习物理规律，提高模型的空间感知能力。
    - 后训练：采用SFT监督微调和GRPO强化学习训练，通过多维度奖励函数优化模型在博弈场景下的表现。奖励函数包括：
      - 格式奖励：验证输出结构的完整性（场景描述、轨迹、限速、风险标志等标签）
      - 场景标签奖励：评估场景理解准确性（多标签分类）
      - 轨迹奖励：评估参考线轨迹生成质量（与ground truth的匹配度）
      - 速度奖励：评估速度token预测准确性
      - 风险标志奖励：评估安全决策能力（F0.5分数评估）
      - 多样性奖励：促进模型在corner case场景下的适应性
    - 数据方面: 
      - 车端部署VLM蒸馏模型用作场景分类，进行corner case采集,包含异形障碍物，极端道路结构(窄路，环岛)，交互博弈（强行加塞, 无保护左转）
  - 交付指标：
    - 复杂城市场景下的接管里程（MPI）提升 40%。
    - 典型 Corner Case（如无保护左转）的成功率从 75% 提升至 92%。
  - 当前问题
    - 模型泛化能力不够，过拟合明显
    - 轨迹输出不合理，下游仍旧需要大量规则进行兜底

### **项目二: 3D感知与OCC感知(元戎启行)**
  - QueryTracker
    - 项目背景：使用基于神经网络的tracker替代原先的基于规则的tracker
    - 采用了类似于TrackFormer和TransCenter的思想，基于query的Transformer架构
      - 使用Instance Bank存储object历史轨迹,是QueryTracker实现稳定长期跟踪的关键，解决了目标遮挡、短暂消失等问题，确保跟踪的连续性和稳定性。
      - 模型输入当前BEV特征，历史的BEV特征，bbox, 置信度，时间间隔，位姿等信息，通过self attention和cross attention直接输出追踪后的3D障碍物
  - 3D occ
    - 项目背景：基于3D感知的OCC识别，用于识别不同类型的占用物（水马、围栏、锥桶等）
    - 模型架构：
      - 全卷积的head，用于做3D分割，判断是否占据, 占据物体类别等信息
      - 针对雨花误检问题，增加noise类别预测
      - fusion occ探索, 单LIDAR occ遇到了瓶颈，结合图像数据上线了fusion occ.


### **项目三：点云检测和分割(小马智行)**

  - 项目描述： 复现并优化 Waymo 顶刊论文 Range Sparse Net (RSN)，构建一套兼顾 Range View (RV) 语义分割与 BEV 目标检测的端到端感知框架。
  - 模型架构: 
    - 在RV视角使用U-Net进行3D语义分割(类似occ)，识别噪点，地面点，背景点，行人车辆等信息，损失函数使用Focal Loss + Lovász-Softmax Loss
    - 目标检测在BEV视角进行，模型架构采用Sparse CNN + SSD/CenterPoint Head, 损失函数采用多任务损失，包含分类损失(focal loss), 回归损失(l1 loss), Direction Loss：专门用于处理朝向角的周期性问题
    - 稀疏卷积网络输入为经过 Range View 分割过滤后的点云，背景点已被去除，输入的具体形式为非零点的空间坐标 $(x, y, z)$, 稀疏卷积通过cuda实现，具体机制为结合哈希表和Rule Book(卷积核输出点对应的输入坐标),有了 Rule Book，计算过程就变成了矩阵乘法（GEMM），这让稀疏卷积在 GPU 上的执行速度飞快


### **项目四: 基于 SCOPE 静态分析的数据血缘系统(微软)**
  - 项目描述：开发了一套针对微软大数据特有语言 SCOPE 的静态解析引擎，通过构建全链路数据血缘图谱，解决 Cosmos 平台数据冗余及资产溯源难题
  - 核心贡献：
    - 编译级 Parser 开发：基于编译原理，自主实现了一套针对 SCOPE 语法的解析器（Parser），通过解析 抽象语法树 (AST) 提取数据表、视图及 UDF 之间的依赖关系。
    - 大规模血缘图谱构建：处理并关联 Cosmos 平台内 PB 级数据的生产与消费记录，实现了表级与字段级（Column-level）的血缘追踪。
  - 业务价值：
    - 成本优化：基于血缘关系识别并清理了长达 180 天无下游调用的“冷数据”和冗余副本，直接为部门节省了约 12% 的存储开销。
    - 安全合规：为敏感数据提供了清晰的溯源路径，满足了内部数据合规与影响分析的需求(欧盟GDPR法案)
  
### **项目五: 基于Azure ML的集群监控系统**
  - 项目描述：针对微软内部超大规模计算集群 Cosmos，搭建了一套从异常监测到自动化运维的闭环系统，旨在降低集群宕机风险并提升任务作业的稳定性。
  - 核心贡献：
    - 多维指标监控：集成 Cosmos 服务器底层硬件（CPU、磁盘 I/O、网络丢包）与系统级故障日志，构建了高维时序特征库。
    - 异常检测架构：接入 Azure Time Series Anomaly Detection 服务，利用其内置的 SR-CNN (Spectral Residual-CNN) 算法，实现了对非平稳时序数据的实时监控。相较于传统阈值告警，漏报率降低了 18%

  
