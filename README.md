# 古法编程

从零开始学习 Python 编程、数据处理、深度学习模型构建与大模型应用的个人练习项目。边学边练，从易到难逐步推进。

## 学习环境

默认使用本机 Python 3.10 环境（miniconda）：

```
E:\HOUYAXI\software\miniconda\envs\python310\python.exe
```

已安装的核心库：numpy、pandas、matplotlib、scipy、scikit-learn、torch（PyTorch）、torchvision、transformers、tokenizers。

运行方式：所有讲义和练习都是 Jupyter Notebook（.ipynb），分块学习，每讲一个知识点运行一小块。

在项目根目录打开终端，启动 Jupyter（二选一）：

```
E:\HOUYAXI\software\miniconda\envs\python310\python.exe -m jupyter lab
E:\HOUYAXI\software\miniconda\envs\python310\python.exe -m jupyter notebook
```

浏览器打开后，进入 stage_01_python基础 目录，双击 .ipynb 文件，从上往下一块一块运行（Shift+Enter）。

## 学习路线总览

| 阶段 | 主题 | 主要库 | 目标 |
| --- | --- | --- | --- |
| 1 | Python 基础（print、变量、import、数据类型） | 内置库 | 能写能跑第一段程序 |
| 2 | 控制流与函数（if/for/def） | 内置库 | 用代码解决简单逻辑问题 |
| 3 | class 面向对象 | 内置库 | 理解类、属性、方法、继承 |
| 4 | NumPy 数据处理 | numpy | 数组运算、索引、广播 |
| 5 | Pandas 数据清洗 | pandas | 读写数据、筛选、聚合 |
| 6 | 结果展示 | matplotlib | 画折线、柱状、散点图 |
| 7 | PyTorch 入门 | torch | 张量、自动求导 |
| 8 | 深度学习模型构建 | torch | 用 nn.Module 建模型并训练 |
| 9 | Transformer 原理与实现 | torch | 理解注意力机制，实现小型 Transformer |
| 10 | 大模型应用 | transformers | 加载预训练模型、推理、微调 |
| 11 | 综合小项目 | 全部 | 数据到模型到展示的完整流程 |

详细版见《学习路线.md》。每阶段包含讲义、可运行示例、练习任务，练习做完后对照 answers 目录下的参考答案自查，也可以随时在对话里让我检查你的代码。

## 目录结构

```
古法编程/
├── README.md              项目说明（本文件）
├── 学习路线.md             详细学习路线与库速查卡索引
├── stage_01_python基础     print、变量、import、数据类型
├── stage_02_控制流与函数    if/for/while、函数
├── stage_03_class面向对象   类、方法、继承
├── stage_04_numpy数据处理   NumPy 数组运算
├── stage_05_pandas数据清洗  Pandas 数据处理
├── stage_06_matplotlib结果展示  绘图与结果展示
├── stage_07_pytorch张量与自动求导  PyTorch 基础
├── stage_08_深度学习模型构建  模型构建与训练
├── stage_09_transformer原理与实现  注意力与 Transformer
├── stage_10_大模型应用     HuggingFace 模型使用
└── projects_综合小项目     综合练习项目
```

## 学习方法建议

- 每个阶段先读讲义并运行示例代码，理解后再独立完成练习。
- 练习先自己写，写完运行看结果，再对照参考答案。
- 卡住时把代码和报错发到对话里，我来帮你定位和讲解。
- 每学完一个库，用阶段末尾的速查卡复习，之后做综合项目巩固。
