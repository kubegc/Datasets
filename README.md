# 用于存储各类框架、平台等测试数据集, 内部应该包含数据集组织结构说明文档

## 内容目录
| 文件夹名称 |    介绍   |  生成代码 |  分析结果 | 创建人 | 创建时间 |
| :-----:   | :-----:   | :-----:  | :-----:  | :-----:  | :-----:  |
| [datasets](#/datasets/)  | [TVM算子运行时间测量](datasets/README.md) | [TVMPredictor](https://github.com/dos-lab/TVMPredictor/tree/yutian/create_dataset/test_code/op_test_code) | [TVM-Analyze](https://github.com/dos-lab/TVM-Analyze/tree/master/TVM/operators) | [余甜](https://github.com/oneflyingfish) | 2021年 |
| [datasets_300](datasets_300/)  | [TVM算子运行时间测量(batch size增强版)](datasets_300/README.md) | [TVMPredictor](https://github.com/dos-lab/TVMPredictor/tree/yutian/create_dataset/test_code/op_test_code) | [参考TVM-Analyze](https://github.com/dos-lab/TVM-Analyze/tree/master/TVM/operators) | [余甜](https://github.com/oneflyingfish) | 2021年 |
| [datasets_model](datasets_model/)  | [TVM模型在不同CPU/GPU配置组合的下运行时间测量](datasets_model/README.md) | [TVMPredictor](https://github.com/dos-lab/TVMPredictor/tree/yutian/create_dataset/test_code/model_test_code) | [TVM-Analyze](https://github.com/dos-lab/TVM-Analyze/tree/master/TVM/models/analyze_model) | [胡艺]()、[余甜](https://github.com/oneflyingfish) | 2021年 |
| [datasets_models](datasets_models/)  | [TVM模型运行时间测量](datasets_models/README.md) | [TVMPredictor](https://github.com/dos-lab/TVMPredictor/tree/yutian/create_dataset/test_code/model_test_code) | [TVM-Analyze](https://github.com/dos-lab/TVM-Analyze/tree/master/TVM/models/analyze_models) | [余甜](https://github.com/oneflyingfish) | 2021年 |

## 相关仓库说明：
* TVM
    * [数据集生成](https://github.com/dos-lab/TVMPredictor)
    * [绘图分析代码](https://github.com/dos-lab/TVM-Analyze)

[Git submodule使用](https://www.aflyingfish.top/articles/bd654071b044/)