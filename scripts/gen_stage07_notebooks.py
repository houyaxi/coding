# -*- coding: utf-8 -*-
"""生成第七阶段（PyTorch 张量与自动求导）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_07_pytorch张量与自动求导"
nb = nbf.v4


def make_nb(cells):
    nbk = nb.new_notebook()
    nbk.metadata = {"kernelspec": {"display_name": "Python 3 (python310)", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}
    nbk.cells = cells
    return nbk


def md(t):
    return nb.new_markdown_cell(t)


def code(t):
    return nb.new_code_cell(t)


lesson01 = [
    md("""# 第七阶段第一课：PyTorch 张量基础

PyTorch 是深度学习框架，核心数据结构是张量（Tensor），可以理解为"能在 GPU 上跑的 NumPy 数组"。从上往下一块一块运行。"""),
    md("""## 1. 创建张量

张量和 NumPy 数组很像，但多了自动求导、GPU 这些能力。"""),
    code("""import torch

print(torch.tensor([1, 2, 3]))          # 从列表创建
print(torch.zeros(3))                   # 全 0
print(torch.ones(2, 3))                 # 全 1，2 行 3 列
print(torch.randn(2, 3))                # 标准正态分布随机数
print(torch.arange(10))                 # 0 到 9"""),
    md("""## 2. 张量属性：形状、类型、设备"""),
    code("""x = torch.randn(3, 4)
print(x.shape)          # torch.Size([3, 4])
print(x.dtype)          # torch.float32
print(x.device)         # cpu（如果装了 CUDA 版且硬件支持，会是 cuda）"""),
    md("""## 3. 张量与 NumPy 互转"""),
    code("""import numpy as np

arr = np.array([1.0, 2.0, 3.0])
t = torch.from_numpy(arr)      # numpy -> tensor
print(t)

back = t.numpy()               # tensor -> numpy
print(back)"""),
    md("""## 4. 形状操作：view、reshape、permute"""),
    code("""x = torch.arange(12)
print(x.view(3, 4))            # 重排成 3x4
print(x.reshape(4, 3))         # 另一种重排
print(x.view(2, 6).permute(1, 0))  # 转置：6x2"""),
    md("""## 5. 数学运算

和 NumPy 一样，直接运算符即可。"""),
    code("""a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
print(a + b)
print(a * 2)
print(a.mean())
print(a.sum())
print(a @ b)                 # 点积"""),
    md("""## 6. 练习（自己动手写）

练习 1：创建一个 5 行 3 列的随机张量，打印它的形状和平均值。

练习 2：用 torch.arange 创建 0-23 的整数张量，view 成 4x6，再转置，打印结果的形状。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第七阶段第二课：自动求导与数据加载

自动求导是深度学习训练的核心机制：PyTorch 自动帮你算梯度。这一课还要学怎么组织数据。"""),
    md("""## 1. 自动求导：requires_grad 和 backward

给张量设 requires_grad=True，对它做运算后调用 backward()，梯度自动算好放在 .grad 里。"""),
    code("""import torch

x = torch.tensor(3.0, requires_grad=True)
y = x ** 2 + 2 * x          # y = x^2 + 2x，x=3 时 y=15

y.backward()                # 自动求导
print(x.grad)               # dy/dx = 2x + 2 = 8"""),
    md("""## 2. 多个变量的梯度"""),
    code("""a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
z = a * b + a               # z = ab + a

z.backward()
print(a.grad)               # dz/da = b + 1 = 4
print(b.grad)               # dz/db = a = 2"""),
    md("""## 3. 关闭梯度：with torch.no_grad()

推理（预测）时不需要梯度，关掉能省内存和提速。"""),
    code("""x = torch.tensor([1.0, 2.0])
with torch.no_grad():
    y = x * 3
print(y)"""),
    md("""## 4. Dataset：自定义数据集

把数据和标签打包成一个 Dataset，PyTorch 才能按批次喂给模型。"""),
    code("""from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, n):
        self.x = torch.arange(n, dtype=torch.float32)
        self.y = 2 * self.x + 1      # 假设 y = 2x + 1

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

ds = MyDataset(10)
print(ds[0], ds[5])"""),
    md("""## 5. DataLoader：按批次取数据

DataLoader 自动打乱、分批，训练时直接循环取。"""),
    code("""loader = DataLoader(ds, batch_size=4, shuffle=True)

for batch_x, batch_y in loader:
    print(batch_x, batch_y)
# 10 个样本，每批 4 个，最后一批 2 个"""),
    md("""## 6. 练习（自己动手写）

练习 1：写一个函数 f(x) = x^3，在 x=2 处 backward，验证梯度是 12（d(x^3)/dx = 3x^2）。

练习 2：自定义一个 Dataset，包含 20 个样本，特征 x 是 0-19，标签 y = 3x + 5，然后用 DataLoader 按批次 8 打印第一批。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第七阶段综合练习

覆盖张量、自动求导、Dataset/DataLoader。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：张量热身

创建 3x3 的随机张量，打印形状、最大值、每行求和（提示：t.sum(dim=1)）。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：梯度验证

设 x = 4.0（requires_grad），计算 y = x^2 + 3x，backward 后打印 x.grad，验证等于 2x+3=11。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：线性关系数据

创建 50 个样本的 Dataset：x 是 0-49，y = 0.5x + 3，用 DataLoader（batch 10）循环打印第一批的 x 和 y。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：多维梯度（挑战）

两个参数 a、b（都是 requires_grad），z = a^2 + b^3，在 a=2、b=3 处求导，打印两个梯度（期望 4 和 27）。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第七阶段就过关了！"""),
]

answer = [
    md("""# 第七阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""import torch
t = torch.randn(3, 3)
print("形状", t.shape)
print("最大值", t.max())
print("每行求和", t.sum(dim=1))"""),
    md("""## 题 2 参考答案"""),
    code("""import torch
x = torch.tensor(4.0, requires_grad=True)
y = x ** 2 + 3 * x
y.backward()
print("梯度", x.grad)   # 11"""),
    md("""## 题 3 参考答案"""),
    code("""import torch
from torch.utils.data import Dataset, DataLoader

class LinearDS(Dataset):
    def __init__(self, n):
        self.x = torch.arange(n, dtype=torch.float32)
        self.y = 0.5 * self.x + 3
    def __len__(self):
        return len(self.x)
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

ds = LinearDS(50)
loader = DataLoader(ds, batch_size=10)
batch_x, batch_y = next(iter(loader))
print(batch_x)
print(batch_y)"""),
    md("""## 题 4 参考答案"""),
    code("""import torch
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
z = a ** 2 + b ** 3
z.backward()
print("da", a.grad)   # 4
print("db", b.grad)   # 27"""),
]

files = {
    "lesson_01_张量基础.ipynb": lesson01,
    "lesson_02_自动求导与数据加载.ipynb": lesson02,
    "practice_07.ipynb": practice,
    os.path.join("answers", "practice_07_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
