### 模型在不同输入shape、batch size下运行时间测量:

数据集：
* inception_v3,mobilenet,resnet-50,resnet3d-50,squeezenet_v1_1: 
  * 输入：
    * shape: 16~256, 16为间隔
    * batch size: 1~128
  * 硬件：
    * GTX-2080Ti
    * Tesla-T4
    * Tesla-k40c
    
* 自定义CNN、NN:
  * 输入：
    * shape: 1~91, 10为间隔
    * batch size: 1~100
  * 硬件：
    * GTX-2080Ti
    * Tesla-T4
    * Tesla-k40c