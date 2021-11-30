### 模型在不同输入shape、batch size下运行时间测量:

数据集：
* inception_v3:
  * 输入:
    * shape: 299*299
    * batch size: 1~128
    * 注：因为TVM内部调用原因，暂时仅采样这一组数据
  * 硬件
    * GTX-2080Ti（两张卡的数据集等同）
    * Tesla-T4
    * Tesla-k40c

* resnet-50,resnet3d-50: 
  * 输入：
    * shape: 16~256, 16为间隔
    * batch size: 1~128
  * 硬件：
    * GTX-2080Ti
    * Tesla-T4
    * Tesla-k40c

* squeezenet_v1_1: 
  * 输入：
    * shape: 32~256, 16为间隔
    * batch size: 1~128
  * 硬件：
    * GTX-2080Ti
    * Tesla-T4
    * Tesla-k40c

* mobilenet:
  * 输入height/width比例达到极限时发生错误，数据集采样失败。

* 自定义CNN、NN:
  * 输入：
    * shape: 1~91, 10为间隔
    * batch size: 1~100
  * 硬件：
    * GTX-2080Ti
    * Tesla-T4
    * Tesla-k40c