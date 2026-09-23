# -*- coding: utf-8 -*-
"""生成第八阶段（深度学习模型构建）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_08_深度学习模型构建"
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
    md("""# 第八阶段第一课：构建并训练第一个模型

深度学习训练的标准流程：定义模型 → 定义损失和优化器 → 循环：前向传播 → 算损失 → 反向传播 → 更新参数。这一课用线性回归入门。"""),
    md("""## 1. nn.Module：模型的基类

所有模型都继承 nn.Module，在 __init__ 里定义层，forward 里定义数据怎么流过。"""),
    code("""import torch
import torch.nn as nn

# 一个单层线性模型：y = w*x + b
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)   # 输入 1 维，输出 1 维

    def forward(self, x):
        return self.linear(x)

model = LinearModel()
print(model)                 # 查看模型结构
print(list(model.parameters()))  # 参数 w 和 b"""),
    md("""## 2. 准备训练数据

构造带噪声的线性数据，y ≈ 2x + 1。"""),
    code("""x = torch.linspace(-3, 3, 100).reshape(-1, 1)
true_w, true_b = 2.0, 1.0
y = true_w * x + true_b + 0.2 * torch.randn_like(x)

print(x[:3])
print(y[:3])"""),
    md("""## 3. 损失函数和优化器

MSE 衡量预测和真实值的差距；优化器（SGD）负责按梯度更新参数。"""),
    code("""criterion = nn.MSELoss()          # 均方误差
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降"""),
    md("""## 4. 训练循环：核心模板

这是深度学习最重要的 5 行代码模板，后面所有模型都用它。"""),
    code("""for epoch in range(100):
    # 前向：算预测
    pred = model(x)
    # 算损失
    loss = criterion(pred, y)
    # 清零梯度（不清会累积）
    optimizer.zero_grad()
    # 反向传播：算梯度
    loss.backward()
    # 更新参数
    optimizer.step()

    if epoch % 20 == 0:
        print(f"epoch {epoch}, loss = {loss.item():.4f}")

# 看看学到的 w 和 b 是否接近 2 和 1
w = model.linear.weight.item()
b = model.linear.bias.item()
print(f"学到的 w={w:.3f}, b={b:.3f}（真实 2.0, 1.0）")"""),
    md("""## 5. 练习（自己动手写）

练习 1：把训练循环改到 200 轮，观察损失是否降得更低。

练习 2：把学习率 lr 改成 0.001，重跑一遍，观察收敛变慢。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第八阶段第二课：MLP 分类手写数字

从回归到分类：用多层感知机（MLP）识别手写数字。分类和回归的区别：输出层用 softmax，损失用交叉熵。"""),
    md("""## 1. 准备数据：用 sklearn 自带的手写数字集

为了避免下载，这里用 sklearn 的 digits 数据集（8x8 像素的手写数字，10 类）。"""),
    code("""import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

digits = load_digits()
X = digits.data        # 1797 张图，每张 64 个像素
y = digits.target      # 标签 0-9

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("训练集", X_train.shape, "测试集", X_test.shape)"""),
    md("""## 2. 定义 MLP：64 -> 32 -> 10

nn.Sequential 把层串起来。中间用 ReLU 激活函数加非线性。"""),
    code("""model = nn.Sequential(
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10),        # 10 类输出
)
print(model)"""),
    md("""## 3. 损失和优化器

分类任务用 CrossEntropyLoss（它内部自带 softmax）。"""),
    code("""criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=64)"""),
    md("""## 4. 训练循环（和上一课同一套模板）"""),
    code("""for epoch in range(30):
    total_loss = 0
    for batch_x, batch_y in train_loader:
        pred = model(batch_x)
        loss = criterion(pred, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 10 == 0:
        print(f"epoch {epoch}, 平均损失 {total_loss / len(train_loader):.4f}")"""),
    md("""## 5. 评估准确率"""),
    code("""correct = 0
total = 0
with torch.no_grad():
    for batch_x, batch_y in test_loader:
        pred = model(batch_x)
        _, predicted = torch.max(pred, dim=1)   # 取分数最高的类别
        correct += (predicted == batch_y).sum().item()
        total += batch_y.size(0)

print(f"测试集准确率：{correct / total * 100:.1f}%")"""),
    md("""## 6. 保存和加载模型"""),
    code("""torch.save(model.state_dict(), "mlp_digits.pt")   # 保存参数

model2 = nn.Sequential(
    nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10),
)
model2.load_state_dict(torch.load("mlp_digits.pt"))   # 加载
print("模型已保存并重新加载")"""),
    md("""## 7. 练习（自己动手写）

练习 1：把隐层从 32 改成 64 个神经元，重训一遍，看准确率变化。

练习 2：把训练轮数从 30 改成 50，看准确率是否更高。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第八阶段综合练习

覆盖模型定义、训练循环、分类评估。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：拟合二次函数

数据：x 在 -3 到 3 之间 100 个点，y = x^2 + 0.5 加小噪声。用 nn.Sequential 搭一个两层网络（Linear(1, 16) + ReLU + Linear(16, 1)），训练 500 轮，打印最终损失。
提示：网络更深才能拟合曲线。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：分类准确率比较

用 digits 数据集训练两个模型：一个只有 Linear(64,10)（无隐层），一个 MLP(64-32-10)。各训练 20 轮，比较测试集准确率，看多层是否更强。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：模型保存与加载（挑战）

训练好题 2 的 MLP 后，保存参数到文件，再加载到一个新模型里，用它预测测试集前 10 张图，打印预测结果和真实标签。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第八阶段就过关了！"""),
]

answer = [
    md("""# 第八阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""import torch
import torch.nn as nn

x = torch.linspace(-3, 3, 100).reshape(-1, 1)
y = x ** 2 + 0.5 + 0.1 * torch.randn_like(x)

model = nn.Sequential(
    nn.Linear(1, 16),
    nn.ReLU(),
    nn.Linear(16, 1),
)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
    pred = model(x)
    loss = criterion(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(f"最终损失 {loss.item():.4f}")"""),
    md("""## 题 2 参考答案"""),
    code("""import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader

digits = load_digits()
X = torch.tensor(digits.data, dtype=torch.float32)
y = torch.tensor(digits.target, dtype=torch.long)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
test_loader = DataLoader(TensorDataset(X_test, y_test), batch_size=64)


def train_and_eval(model):
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    for epoch in range(20):
        for bx, by in train_loader:
            pred = model(bx)
            loss = criterion(pred, by)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    correct = total = 0
    with torch.no_grad():
        for bx, by in test_loader:
            _, predicted = torch.max(model(bx), dim=1)
            correct += (predicted == by).sum().item()
            total += by.size(0)
    return correct / total


model1 = nn.Sequential(nn.Linear(64, 10))
model2 = nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))

print("无隐层准确率：", round(train_and_eval(model1) * 100, 1), "%")
print("MLP准确率：", round(train_and_eval(model2) * 100, 1), "%")"""),
    md("""## 题 3 参考答案"""),
    code("""import torch
import torch.nn as nn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
X = torch.tensor(digits.data, dtype=torch.float32)
y = torch.tensor(digits.target, dtype=torch.long)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 快速训练一个简单模型
model = nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
from torch.utils.data import TensorDataset, DataLoader
loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)
for epoch in range(20):
    for bx, by in loader:
        loss = criterion(model(bx), by)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

torch.save(model.state_dict(), "my_model.pt")

new_model = nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10))
new_model.load_state_dict(torch.load("my_model.pt"))

with torch.no_grad():
    pred = new_model(X_test[:10])
    _, predicted = torch.max(pred, dim=1)
print("预测：", predicted.tolist())
print("真实：", y_test[:10].tolist())"""),
]

files = {
    "lesson_01_构建训练线性模型.ipynb": lesson01,
    "lesson_02_MLP分类手写数字.ipynb": lesson02,
    "practice_08.ipynb": practice,
    os.path.join("answers", "practice_08_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
