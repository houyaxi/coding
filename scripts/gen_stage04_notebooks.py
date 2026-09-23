# -*- coding: utf-8 -*-
"""生成第四阶段（NumPy 数据处理）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_04_numpy数据处理"
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
    md("""# 第四阶段第一课：NumPy 基础

NumPy 是 Python 数据科学的基石，核心是"数组"（ndarray）。它让批量数值运算又快又简洁。从上往下一块一块运行。"""),
    md("""## 1. 认识数组

数组和列表类似，但要求元素同类型，且支持直接做数学运算。"""),
    code("""import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)      # 元素类型
print(type(arr))      # numpy.ndarray"""),
    md("""## 2. 创建数组的常用方法"""),
    code("""print(np.zeros(3))           # 全 0
print(np.ones(4))            # 全 1
print(np.arange(10))         # 0 到 9
print(np.arange(1, 10, 2))   # 1 到 9，步长 2
print(np.linspace(0, 1, 5))  # 0 到 1 均匀分 5 份
print(np.random.randint(1, 100, 5))  # 5 个 1-99 随机整数"""),
    md("""## 3. 形状：shape、reshape、转置

二维数组像表格，行和列统称形状。"""),
    code("""arr = np.arange(12)
print(arr.shape)             # (12,)

matrix = arr.reshape(3, 4)   # 变成 3 行 4 列
print(matrix)
print(matrix.shape)          # (3, 4)

print(matrix.T)              # 转置：行变列
print(matrix.T.shape)        # (4, 3)"""),
    md("""## 4. 索引与切片

和列表类似，二维用 [行, 列] 两个下标。"""),
    code("""matrix = np.arange(12).reshape(3, 4)
print(matrix[0])             # 第 0 行
print(matrix[1, 2])          # 第 1 行第 2 列，值 6
print(matrix[:, 1])          # 所有行的第 1 列
print(matrix[0:2, :])        # 前两行全部列
print(matrix[:, :2])         # 所有行，前两列"""),
    md("""## 5. 布尔掩码：按条件选元素

这是 NumPy 最爽的特性，一行完成"找出满足条件的元素"。"""),
    code("""arr = np.array([1, 8, 3, 9, 5, 12])
print(arr > 4)               # 每个元素比较，得到布尔数组
print(arr[arr > 4])          # 只保留大于 4 的
print(arr[arr % 2 == 0])     # 只保留偶数"""),
    md("""## 6. 练习（自己动手写）

练习 1：用 np.random.randint 生成 20 个 1-100 的随机整数，用布尔掩码找出所有大于 50 的。

练习 2：把 1 到 16 排成 4 行 4 列的矩阵，打印第 2 行、第 3 列、以及转置后的形状。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第四阶段第二课：NumPy 运算

上一课会建数组，这一课让数组"干活"：数学运算、统计、矩阵乘法、广播。"""),
    md("""## 1. 元素级运算：不用写循环

数组直接加减乘除，自动作用于每个元素。"""),
    code("""import numpy as np

arr = np.array([1, 2, 3])
print(arr + 10)          # 每个元素加 10
print(arr * 2)           # 每个元素乘 2
print(arr ** 2)          # 每个元素平方

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)             # 对应位置相加"""),
    md("""## 2. 统计函数"""),
    code("""data = np.random.randint(1, 100, 20)
print(data)
print("总和", data.sum())
print("平均", data.mean())
print("最大", data.max())
print("最小", data.min())
print("标准差", data.std())"""),
    md("""## 3. 矩阵运算：dot

矩阵乘法用 np.dot 或 @，注意和元素乘法的区别。"""),
    code("""A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)            # 元素逐个相乘
print(A.dot(B))         # 矩阵乘法
print(A @ B)            # 和 dot 一样"""),
    md("""## 4. 广播机制

形状不同的数组也能运算，NumPy 会自动扩展小的那个。"""),
    code("""matrix = np.arange(12).reshape(3, 4)
row = np.array([1, 2, 3, 4])

print(matrix + row)     # 每一行都加 row
print(matrix * 2)       # 标量自动广播"""),
    md("""## 5. 保存与读取"""),
    code("""import numpy as np
arr = np.arange(10)

np.save("my_array.npy", arr)       # 保存
loaded = np.load("my_array.npy")   # 读取
print(loaded)"""),
    md("""## 6. 练习（自己动手写）

练习 1：生成 30 个 1-100 的随机整数，打印平均值、最大值，并统计大于平均值的个数。

练习 2：A 是 3 行 2 列、B 是 2 行 4 列，用 dot 求 A@B 并打印结果的形状。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第四阶段综合练习

覆盖 NumPy 的创建、运算、统计、布尔掩码。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：成绩统计

生成 30 个 60-100 的随机整数当成绩（np.random.randint(60, 101, 30)），用 NumPy 计算并打印：
- 平均分
- 最高分
- 不及格（小于 60，这题不会出现，换成低于 80 的）个数
- 所有成绩里能被 5 整除的有哪些"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：矩阵操作

把 1 到 20 排成 4 行 5 列，完成：
- 打印第 3 行
- 打印所有行的第 2 列
- 把每个元素加 100，打印新矩阵"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：温度转换（向量化）

摄氏温度数组 [0, 10, 20, 30, 40]，用广播一行算出对应的华氏温度（F = C * 9 / 5 + 32），打印结果"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：矩阵乘法（挑战）

两个矩阵：A 是 2x3，B 是 3x2，用随机整数填充，计算 A @ B，验证结果形状是 2x2。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第四阶段就过关了！"""),
]

answer = [
    md("""# 第四阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""import numpy as np
scores = np.random.randint(60, 101, 30)
print(f"平均分：{round(scores.mean(), 1)}")
print(f"最高分：{scores.max()}")
print(f"低于80的个数：{(scores < 80).sum()}")
print(f"能被5整除的：{scores[scores % 5 == 0]}")"""),
    md("""## 题 2 参考答案"""),
    code("""import numpy as np
m = np.arange(1, 21).reshape(4, 5)
print(m[2])            # 第 3 行
print(m[:, 1])         # 所有行的第 2 列
print(m + 100)         # 全部加 100"""),
    md("""## 题 3 参考答案"""),
    code("""import numpy as np
c = np.array([0, 10, 20, 30, 40])
f = c * 9 / 5 + 32
print(f)"""),
    md("""## 题 4 参考答案"""),
    code("""import numpy as np
A = np.random.randint(1, 10, (2, 3))
B = np.random.randint(1, 10, (3, 2))
C = A @ B
print(A)
print(B)
print(C)
print("形状：", C.shape)"""),
]

files = {
    "lesson_01_NumPy基础.ipynb": lesson01,
    "lesson_02_NumPy运算.ipynb": lesson02,
    "practice_04.ipynb": practice,
    os.path.join("answers", "practice_04_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
