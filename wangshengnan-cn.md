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
         ·
         <span>
             <img src="assets/github-brands.svg" width="18px">
             <a href="https://github.com/angelhunt">github</a>
         </span>
         ·
         <span>
             <img src="assets/rss-solid.svg" width="18px">
         </span>
     </div>
 </center>

<div>
    <img src="assets/info-circle-solid.svg" width="80px" position=absolute right=0 top=0> 
</div>

 ## <img src="assets/info-circle-solid.svg" width="30px"> 个人信息 

   男，1994 年出生                                求职意向：算法工程师                               工作经验：约2年



## <img src="assets/graduation-cap-solid.svg" width="30px"> 教育经历

- 硕士，南京大学，计算机科学与技术专业，2017.9~2020.7

- 学士，南京大学，计算机科学与技术专业，2013.9~2017.7

  

## <img src="assets/briefcase-solid.svg" width="30px"> 工作经历
- **小马智行，perception L2++, 算法工程师, 2021.8~至今**

- **微软中国 公司，m365 部门，SDE, 2020.6~2021.7**

## <img src="assets/tools-solid.svg" width="30px"> 项目经历

- 自动驾驶领域中的场景分类
  - 基于前向摄像机的多任务分类模型，用于天气识别，收费站杆子，图像质量和拥堵识别
    - 基于detection和车道线检测结果用于生成virtual image，从而辅助进行拥堵识别
    - 实现了状态维持时间的衰减系数的平滑策略，用于收费站杆子识别结果平滑
    - 实现了基于时间窗口(5 min)的投票策略，用于天气识别结果平滑 

- 车道线识别的fusion和后处理逻辑
  - 将多个摄像头识别的车道线在3d空间中的融合
  - 尝试使用lidar识别的车道线，并于camera的结果进行融合

- 基于range view的点云检测和基于bird view的点云分割
  - 负责Range View Segmentation部分的线上模块，包括
    - 基于cuda实现point segmentation结果转换到grid
    - 在point segmentation结果上实现的floodfill，并通过与camera detection结果进行fusion, 减少overseg.
  - 协助实现Sparse Conv算子与tensorrt plugin，用于降低分割和检测的latency   

- 基于azure ml Anomaly Detection搭建异常检测系统
  - 用于微软内部数据平台集群异常检测
  - 通过收集微软cosmos服务器的大量机器故障信息训练异常检测模型
  - 实现从异常预警，机器下线到任务重启的完整pipeline
   
- 基于scope语法树静态分析实现的data lineage系统
  - 用于微软大数据生态中数据的追踪与溯源
  - 通过实现scope语法的parser，解析微软大数据平台cosmos中的血缘关系
  
- 基于Intel MKL加速spark MLlib算法性能
  - 通过MKL实现了PCA, ALS, Logistic Regression等算法




  
## <img src="assets/project-diagram-solid.svg" width="30px"> 科研经历
- Unsupervised Human Activity Representation Learning with Multi-task Deep Clustering (**UbiComp 2020, CCF A**)
- AttnSense: Multi-level Attention Mechanism For Multimodal Human Activity Recognition (**Ijcai 2019, CCF A**)
