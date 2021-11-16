## 数据集存储说明

### 数据含义标注:

``` yaml
hostname: 测试机器的名称
test_object: 待测试对象（算子/模型等）的名称
device_id: 机器上CPU/GPU编号。若 device_id = n：n>=0，则对应编号为n的GPU; n<0 表示编号为-n的CPU
test_dimension: python-tuple：((s0,s1,...,sn),(x,y))。表示待测对象存在n个输入，每个输入的维度分别为s1~sn。数据测试时改变的是sx的第y维度，x=0, y=0表示首个输入的最高维度
shape: ((-1,x1,x2,x3),(y0,y1,y2,y3),...)。表示该组数据实际测试时，选取的输入shape，-1表示变化为维度，通常对应数据的横坐标。应该满足两个基本条件：1. 作为输入满足算子输入限定条件，例如矩阵运算的shape关系 2. 和<test_dimension>描述内容一致
```

注：文档中的`shape`通常指代关键input参数，除了`batch size`以外的维度

### 数据(shapen.txt)格式说明:

```txt
# n为变化维度的当前取值，avg_runtime为平均运行时长(单位：ms)
n,avg_runtime(ms)
```

### 存储规则:

```Txt
TVM
└── datasets
    ├── dataset.json
    ├── hostname1
    │   └── test_object
    │       └── device_id
    │           └── test_dimension
    │               ├── shape1.txt
    │               ├── shape2.txt
    │               └── shapen.txt
    └── hostname2
        └── test_object
            └── device_id
                └── test_dimension
                    └── shapen.txt
```

### dataset.json格式说明:

```json
{
    "count": <int>总测试数据量（shapen.txt文件个数）</int>,
    "hostname":{
        "count": <int>hostname机器上总测试数据量</int>,
        "test_object":{
            "count": <int>hostname机器上测试的test_object数据量</int>,
            "device_id":{
                "count": <int>hostname机器的device_id上测试的test_object数据量</int>,
                "test_dimension":{
                    "count": <int>hostname机器的device_id上测试的test_object, 变化维度对应为test_dimension的数据量</int>,
                    "shape_n":{
                        "changed_shape": "test_dimension",
                        "file_path": "TVM/datasets/hostname*/test_object/device_id/test_dimension/shape_n.txt",
                        "shapes": "shape_n",
                        "time": "year-month-day hour:minutes:seconds"
                    }
                }
            }
        }
    }
}
```

### 处理数据集示例代码:

在本地生成各种显卡的数据图

目录：

```txt
.
├── TVM
│   └── datasets
│       ├── datas
│       └── dataset.json
└── plot_code
    └── plot.py
```

plot.py代码：

```python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import os
import math

# 开始画图
plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False      # 解决保存图像时'-'显示为方块的问题

program_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(program_path,"../TVM/datasets/dataset.json") 
datas = {}
picture_index = 1

with open(json_path,'r') as f:
    datas = json.load(f)

device = {"dell04":{"0":"GTX-2080Ti"},"dell03":{"0":"Tesla-T4"},"dell01":{"0":"Tesla-T4"},"dellh01":{"0":"Tesla-K40c"}}

for device_name in datas.keys():
    if device_name=="count":
        continue
    
    for op_name in datas[device_name].keys():
        if op_name=="count":
            continue

        for device_id in datas[device_name][op_name].keys():
            if device_id=="count":
                continue
            hardware_name = device[device_name][device_id]

            for shapes_dimensionality in datas[device_name][op_name][device_id].keys():
                if shapes_dimensionality=="count":
                    continue
                
                # 创建存储目录
                fold_path = os.path.join(os.path.join(os.path.join(program_path,"images"),op_name),shapes_dimensionality).replace(" ","").replace("(","[").replace(")","]")
                if not os.path.exists(fold_path):
                    os.makedirs(fold_path)

                # 开始绘图
                plt.figure(picture_index)
                plt.figure(figsize=(50,50))
                picture_index += 1
                picture_count = int(datas[device_name][op_name][device_id][shapes_dimensionality]["count"])

                img_index=0
                for shape in datas[device_name][op_name][device_id][shapes_dimensionality].keys():
                    if shape=="count":
                        continue

                    img_index+=1
                    value = datas[device_name][op_name][device_id][shapes_dimensionality][shape]
                    data=[[],[]]
                    with open(os.path.join(program_path,"../"+value["file_path"])) as f:
                        line = f.readline()
                        while line is not None and len(line)>0 :
                            data[0].append(int(line.split(",")[0]))
                            data[1].append(float(line.split(",")[1]))
                            line=f.readline()
                    img = plt.subplot(math.ceil(picture_count/10),10 , img_index)
                    plt.plot(*data)
                    # plt.legend() # 显示图例
                    plt.xlabel('batch size')
                    plt.ylabel('run-time')
                    img.set_title(shape)
                plt.savefig(os.path.join(fold_path,hardware_name+".png"))
```

运行效果：

```txt
.
├── TVM
│   └── datasets
│       ├── datas
│       └── dataset.json
└── plot_code
    ├── images
    │   └── test_object
    │       └── test_dimension
    │           └── device_type.png
    └── plot.py
```