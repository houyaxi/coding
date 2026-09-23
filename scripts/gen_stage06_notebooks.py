# -*- coding: utf-8 -*-
"""生成第六阶段（matplotlib 结果展示）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_06_matplotlib结果展示"
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
    md("""# 第六阶段第一课：matplotlib 基础绘图

matplotlib 是 Python 最基础的绘图库。核心思路：先画图对象，再逐项设置，最后 plt.show() 显示。从上往下一块一块运行。"""),
    md("""## 0. 让图直接显示在 notebook 里"""),
    code("""%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np"""),
    md("""## 1. 折线图：plot

适合看趋势，比如随时间的变化。"""),
    code("""x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 4, 8, 9])

plt.plot(x, y)
plt.show()"""),
    md("""## 2. 柱状图：bar

适合对比不同类别的数值。"""),
    code("""names = ["语文", "数学", "英语"]
scores = [85, 92, 78]

plt.bar(names, scores)
plt.show()"""),
    md("""## 3. 散点图：scatter

适合看两个变量之间的关系。"""),
    code("""np.random.seed(1)
x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y)
plt.show()"""),
    md("""## 4. 直方图：hist

适合看数据的分布。"""),
    code("""data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()"""),
    md("""## 5. 练习（自己动手写）

练习 1：画一条 sin 曲线（提示：x = np.linspace(0, 2*np.pi, 100)，y = np.sin(x)）。

练习 2：画一个柱状图展示你三个月的花费（自己编数据）。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第六阶段第二课：美化、布局与中文

图要能给别人看懂：标题、坐标轴、图例、网格、多子图。还有最常踩的坑：中文乱码。"""),
    md("""## 1. 标题、轴标签、图例、网格"""),
    code("""%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = np.array([3, 5, 4, 8, 9])
y2 = np.array([2, 4, 6, 5, 7])

plt.plot(x, y1, label="产品A")
plt.plot(x, y2, label="产品B")
plt.title("销量趋势")
plt.xlabel("月份")
plt.ylabel("销量")
plt.legend()
plt.grid(True)
plt.show()"""),
    md("""## 2. 中文乱码的解决办法

Windows 下 matplotlib 默认字体不含中文，手动指定中文字体即可。"""),
    code("""import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False   # 防止负号显示成方块

plt.plot([1, 2, 3], [1, 4, 9])
plt.title("中文标题测试")
plt.show()"""),
    md("""## 3. 子图：subplot

一张大图里放多个小图，适合对比。"""),
    code("""plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)          # 1 行 2 列，第 1 个
x = np.arange(10)
plt.plot(x, x ** 2)
plt.title("平方")

plt.subplot(1, 2, 2)          # 第 2 个
plt.plot(x, np.sqrt(x))
plt.title("平方根")

plt.show()"""),
    md("""## 4. 保存图片：savefig"""),
    code("""plt.plot([1, 2, 3], [1, 4, 9])
plt.title("保存示例")
plt.savefig("my_chart.png", dpi=150)   # 保存为文件
print("已保存 my_chart.png")"""),
    md("""## 5. 练习（自己动手写）

练习 1：画一个 2 行 1 列的子图：上面是 sin 曲线，下面是 cos 曲线，都要标题。

练习 2：从 students.csv 读数据，画一班和二班数学平均分的柱状图（提示：groupby + bar）。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第六阶段综合练习

覆盖折线、柱状、散点、子图和中文显示。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：数据看图

用 np.random.randint 生成 12 个月的气温数据（15-35 度），画一条折线图，加标题"月度气温"、x 轴"月份"、y 轴"温度"。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：成绩对比柱状图

读取 students.csv，清洗缺失值后按班级分组算数学平均分，画柱状图展示三个班的对比。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：散点看关系

生成 100 个随机点，x 是 0-100 随机整数，y = 2x + 噪声（np.random.randn(100) * 10），画散点图观察线性关系。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：双图对比（挑战）

画一个 1 行 2 列的子图：左边是随机数据的直方图，右边是 sin 曲线。都要中文标题。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第六阶段就过关了！"""),
]

answer = [
    md("""# 第六阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

temps = np.random.randint(15, 36, 12)
plt.plot(range(1, 13), temps)
plt.title("月度气温")
plt.xlabel("月份")
plt.ylabel("温度")
plt.show()"""),
    md("""## 题 2 参考答案"""),
    code("""import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv(r"C:\\Users\\26643\\Desktop\\古法编程\\stage_05_pandas数据清洗\\students.csv").dropna()
avg = df.groupby("班级")["数学"].mean()
plt.bar(avg.index, avg.values)
plt.title("各班数学平均分")
plt.show()"""),
    md("""## 题 3 参考答案"""),
    code("""import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 101, 100)
y = 2 * x + np.random.randn(100) * 10
plt.scatter(x, y)
plt.title("x 与 y 的关系")
plt.show()"""),
    md("""## 题 4 参考答案"""),
    code("""import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(np.random.randn(500), bins=20)
plt.title("随机数据分布")

plt.subplot(1, 2, 2)
x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x))
plt.title("sin 曲线")

plt.show()"""),
]

files = {
    "lesson_01_基础绘图.ipynb": lesson01,
    "lesson_02_美化布局与中文.ipynb": lesson02,
    "practice_06.ipynb": practice,
    os.path.join("answers", "practice_06_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
