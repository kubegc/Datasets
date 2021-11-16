### 不同配置下模型运行时间测量：

shape: 设定经验值
batch size:
  * inception_v3: 1~128
  * lstm: 1~201, 10为间隔等间距采样
  * mobilenet: 1~128
  * resnet-50: 1~128
  * resnet3d-50: 1~128
  * squeezenet_v1_1: 1~128

数据集：
* inception_v3,lstm,mobilenet,resnet-50,resnet3d-50,squeezenet_v1_1: 
  * aws_p3_2xlarge_v100
  * aws_g3s_xlarge_m60
  * aws_g4dn_2xlarge_T4
  * aws_g4dn_4xlarge_T4
  * aws_p2_xlarge_k80
  * aws_p3_2xlarge_v100
  * aws_p3_8xlarge_v100
  
* lstm,mobilenet,resnet-50,resnet3d-50,squeezenet_v1_1
  * aws_T4
