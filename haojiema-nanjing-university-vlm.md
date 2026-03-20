# Ma Haojie

<div align="center">
    <h1>Ma Haojie</h1>
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
</div>

## <img src="assets/info-circle-solid.svg" width="30px"> Personal Information

Male, Born in 1994                           Position: Algorithm Engineer                           Work Experience: ~5 years

Skills: 3D Object Detection, Reinforcement Learning (DQN, PPO, GRPO, GSPO), VLM, LLM fine-tuning and distillation, c++, cuda.

## <img src="assets/graduation-cap-solid.svg" width="30px"> Education

- Master, Nanjing University, Computer Science and Technology, 2017.9~2020.7

- Bachelor, Nanjing University, Computer Science and Technology, 2013.9~2017.7

## <img src="assets/briefcase-solid.svg" width="30px"> Work Experience
- **DeepRoute, Perception Algorithm Engineer, 2023.1~Now**
- **Pony.ai, Perception Algorithm Engineer, 2021.8~2022.12**
- **Microsoft China, m365 Department, SDE, 2020.6~2021.7**

## <img src="assets/project-diagram-solid.svg" width="30px"> Research Experience (Total Citations 350+)
- AttnSense: Multi-level Attention Mechanism For Multimodal Human Activity Recognition (**Ijcai 2019, CCF A**, attention-based multimodal fusion)
- Unsupervised Human Activity Representation Learning with Multi-task Deep Clustering (**UbiComp 2020, CCF A**, unsupervised pre-training related)

## <img src="assets/tools-solid.svg" width="30px"> Project Experience

### **Project 1: End-to-End Autonomous Driving Large Model Based on VLA Architecture (DeepRoute)**
  - Project Background: Build a unified multimodal autonomous driving large model, aiming to achieve an end-to-end closed loop from perception understanding to decision planning. Construct a unified model with scene understanding, trajectory output, and risk assessment capabilities.
  - Technical Details:
    - Model Architecture
      - Base model adopts Qwen2-VL 7B architecture, overall parameter count is 8B, precision is FP8.
      - Input includes multimodal information such as BEV features, navigation maps, perception maps, etc., outputs include scene descriptions, trajectory planning, speed limit information, longitudinal/lateral planning, risk flags. Introduces COT output design, requiring the model to first output scene semantic descriptions and intent predictions before generating trajectories.
    - Pretraining
      - Built heterogeneous data mixed training, mixing general visual-language datasets with autonomous driving datasets (large-scale BEV-description pairs) for joint training.
      - Future consideration of combining Masked World Modeling (MWM) concepts to allow the model to learn physical laws from unannotated massive road test videos, improving the model's spatial perception capability.
    - Post-training: Adopted SFT supervised fine-tuning and GRPO reinforcement learning training, optimizing model performance in game scenarios through multi-dimensional reward functions. Reward functions include:
      - Format Reward: Verify the completeness of output structure (scene description, trajectory, speed limit, risk flag labels, etc.)
      - Scene Label Reward: Assess scene understanding accuracy (multi-label classification)
      - Trajectory Reward: Evaluate reference line trajectory generation quality (matching degree with ground truth)
      - Speed Reward: Assess speed token prediction accuracy
      - Risk Flag Reward: Assess safety decision-making capability (F0.5 score evaluation)
      - Diversity Reward: Promote model adaptability in corner case scenarios
    - Data Aspect: 
      - Deployed VLM distillation model on vehicle for scene classification, performing corner case collection, including irregular obstacles, extreme road structures (narrow roads, roundabouts), interactive gaming (forced lane cutting, unprotected left turns).
  - Delivery Metrics:
    - Improved complex urban scenario disengagement distance (MPI) by 40%.
    - Increased success rate for typical Corner Cases (such as unprotected left turns) from 75% to 92%.
  - Current Issues
    - Model generalization capability is insufficient with obvious overfitting
    - Trajectory output is unreasonable, still requiring significant rule-based fallback downstream

### **Project 2: 3D Perception and OCC Perception (DeepRoute)**
  - QueryTracker
    - Project Background: Use neural network-based tracker to replace the original rule-based tracker
    - Adopted ideas similar to TrackFormer and TransCenter, based on query Transformer architecture
      - Used Instance Bank to store object historical trajectories, which is key to QueryTracker achieving stable long-term tracking, solving problems like target occlusion, brief disappearance, etc., ensuring tracking continuity and stability.
      - Model inputs current BEV features, historical BEV features, bbox, confidence, time intervals, pose and other information, directly outputs tracked 3D obstacles through self-attention and cross-attention
  - 3D OCC
    - Project Background: OCC recognition based on 3D perception, used to identify different types of occupancy objects (water barriers, fences, cones, etc.)
    - Model Architecture:
      - Fully convolutional head, used for 3D segmentation, judging whether occupied, occupied object categories and other information
      - Addressed rain false detection issues by adding noise class prediction
      - Explored fusion OCC, single LIDAR OCC encountered bottlenecks, combined image data to implement fusion OCC.

### **Project 3: Point Cloud Detection and Segmentation (Pony.ai)**

  - Project Description: Reproduced and optimized the top-tier paper Range Sparse Net (RSN) from Waymo, building an end-to-end perception framework that balances Range View (RV) semantic segmentation and BEV object detection.
  - Model Architecture: 
    - Performed 3D semantic segmentation (similar to OCC) using U-Net in RV view, identifying noise, ground points, background points, pedestrians, vehicles and other information, with loss function using Focal Loss + Lovász-Softmax Loss
    - Object detection was performed in BEV view, with model architecture adopting Sparse CNN + SSD/CenterPoint Head, loss function using multitask loss containing classification loss (focal loss), regression loss (l1 loss), Direction Loss: specifically designed to handle periodicity issues with orientation angles
    - Sparse convolution network input was point cloud filtered after Range View segmentation, with background points removed. The specific input format was spatial coordinates $(x, y, z)$ of non-zero points. Sparse convolution was implemented via cuda, with the specific mechanism combining hash tables and Rule Book (input coordinates corresponding to convolution kernel output points). With the Rule Book, the calculation process becomes matrix multiplication (GEMM), making sparse convolution extremely fast on GPUs

### **Project 4: Data Lineage System Based on SCOPE Static Analysis (Microsoft)**
  - Project Description: Developed a static parsing engine targeting Microsoft's proprietary big data language SCOPE, solving data redundancy and asset tracing challenges on the Cosmos platform by constructing full-link data lineage graphs.
  - Key Contributions:
    - Compiler-Level Parser Development: Based on compiler principles, independently implemented a parser for SCOPE syntax, extracting dependencies between data tables, views and UDFs by parsing Abstract Syntax Trees (AST).
    - Large-Scale Lineage Graph Construction: Processed and associated production and consumption records of PB-level data within the Cosmos platform, achieving table-level and field-level (Column-level) lineage tracking.
  - Business Value:
    - Cost Optimization: Identified and cleaned "cold data" and redundant copies without downstream calls for 180 days based on lineage relationships, directly saving approximately 12% of storage costs for the department.
    - Security Compliance: Provided clear traceability paths for sensitive data, meeting internal data compliance and impact analysis requirements (EU GDPR).

### **Project 5: Cluster Monitoring System Based on Azure ML (Microsoft)**
  - Project Description: For Microsoft's ultra-large-scale computing cluster Cosmos, built a closed-loop system from anomaly monitoring to automated operations and maintenance, aimed at reducing cluster downtime risks and improving job stability.
  - Key Contributions:
    - Multi-dimensional Metrics Monitoring: Integrated underlying hardware (CPU, disk I/O, network packet loss) and system-level fault logs of Cosmos servers, constructing a high-dimensional time-series feature database.
    - Anomaly Detection Architecture: Connected to Azure Time Series Anomaly Detection service, utilizing its built-in SR-CNN (Spectral Residual-CNN) algorithm to achieve real-time monitoring of non-stationary time series data. Compared to traditional threshold alerts, the false negative rate decreased by 18%.