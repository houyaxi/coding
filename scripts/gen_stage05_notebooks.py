# -*- coding: utf-8 -*-
"""生成第五阶段（Pandas 数据清洗）的 notebook，并生成练习用数据文件 students.csv。"""
import os
import csv
import random
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_05_pandas数据清洗"
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


# 生成练习用数据文件 students.csv（含缺失值）
names = ["张伟", "王芳", "李娜", "刘强", "陈静", "杨洋", "赵敏", "黄磊", "周杰", "吴霞",
         "徐磊", "孙丽", "马超", "朱婷", "胡军", "郭静", "何平", "高远", "林峰", "罗雪"]
classes = ["一班", "一班", "一班", "一班", "一班", "二班", "二班", "二班", "二班", "二班",
           "三班", "三班", "三班", "三班", "三班", "一班", "二班", "三班", "一班", "二班"]
csv_path = os.path.join(BASE, "students.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "班级", "语文", "数学", "英语"])
    for i in range(20):
        chinese = random.randint(60, 100)
        math = random.randint(55, 100)
        english = random.randint(60, 100)
        row = [names[i], classes[i], chinese, math, english]
        # 随机制造 5 个缺失值
        if random.random() < 0.25:
            row[random.choice([2, 3, 4])] = ""
        w.writerow(row)
print(f"已生成数据文件：{csv_path}")

lesson01 = [
    md("""# 第五阶段第一课：Pandas 入门

Pandas 是处理表格数据的核心库。核心结构：Series（一列）和 DataFrame（一张表）。从上往下一块一块运行。"""),
    md("""## 1. 用字典创建 DataFrame

DataFrame 像一张 Excel 表，有行和列。"""),
    code("""import pandas as pd

data = {
    "姓名": ["小明", "小红", "小刚"],
    "语文": [85, 92, 78],
    "数学": [90, 88, 95],
}
df = pd.DataFrame(data)
print(df)"""),
    md("""## 2. Series：单独一列

DataFrame 的每一列就是一个 Series。"""),
    code("""print(df["语文"])          # 取一列，得到 Series
print(df["语文"].mean())    # 这一列的平均值"""),
    md("""## 3. 读取 CSV 文件

read_csv 是数据科学最常用的入口。项目里有个 students.csv 是我们生成的学生成绩表。"""),
    code("""df = pd.read_csv("students.csv")
print(df)"""),
    md("""## 4. 快速了解数据：head、info、describe"""),
    code("""print(df.head(3))         # 前 3 行
print(df.info())           # 列名、类型、缺失情况
print(df.describe())       # 数值列的统计摘要"""),
    md("""## 5. 练习（自己动手写）

练习 1：用字典创建一个 3 行 3 列的 DataFrame（列名随意），打印出来。

练习 2：读取 students.csv，打印前 5 行和 describe 的结果。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第五阶段第二课：筛选、清洗与分组

真实数据很脏，这一课学清洗三板斧：筛选、处理缺失值、分组统计。"""),
    md("""## 1. loc 和 iloc：按标签和按位置取

loc[行, 列] 用名字，iloc[行, 列] 用位置下标。"""),
    code("""import pandas as pd
df = pd.read_csv("students.csv")

print(df.loc[0])                 # 第 0 行（标签是 0）
print(df.loc[0, "语文"])          # 第 0 行的语文成绩
print(df.iloc[1, 2])             # 第 1 行第 2 列
print(df.iloc[0:3, 0:2])         # 前 3 行前 2 列"""),
    md("""## 2. 按条件筛选行

用布尔条件选行，和 NumPy 掩码一个思路。"""),
    code("""print(df[df["数学"] > 90])        # 数学大于 90 的行
print(df[df["班级"] == "一班"])    # 一班的同学
print(df[(df["语文"] > 80) & (df["数学"] > 80)])  # 双科都超过 80"""),
    md("""## 3. 排序：sort_values"""),
    code("""print(df.sort_values("数学", ascending=False).head(5))  # 数学从高到低前 5"""),
    md("""## 4. 缺失值处理：dropna 和 fillna

CSV 里有些成绩是空的（NaN），统计前必须处理。"""),
    code("""print(df.isna().sum())          # 每列有几个缺失

# 方法一：删除有缺失的行
df_drop = df.dropna()
print(df_drop.shape)

# 方法二：用该列平均值填充
df_fill = df.fillna({"语文": df["语文"].mean(),
                     "数学": df["数学"].mean(),
                     "英语": df["英语"].mean()})
print(df_fill.isna().sum())       # 没有缺失了"""),
    md("""## 5. 分组聚合：groupby

按班级分组，再算每组的平均值，一条语句搞定。"""),
    code("""clean = df.dropna()
print(clean.groupby("班级")["数学"].mean())    # 各班数学平均
print(clean.groupby("班级").agg({"语文": "mean", "数学": "max"}))  # 各班的语文均值和数学最高"""),
    md("""## 6. 练习（自己动手写）

练习 1：读取 students.csv，打印英语成绩大于 85 的同学。

练习 2：用 fillna 填充缺失值后，按班级统计语文平均分。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第五阶段综合练习

数据文件 students.csv 在 stage_05_pandas数据清洗 目录里。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：数据浏览

读取 students.csv，打印：数据总共有多少行、每列缺失数量、数学成绩的平均值和最高分。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：筛选优秀学生

找出语文和数学都大于 85 的同学，按语文成绩从高到低排序，打印前 5 名。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：缺失值清洗

用 fillna 把每科的缺失值填成该科平均分，然后打印清洗后还有没有缺失。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：分组统计

清洗后按班级分组，统计每个班的英语平均分，并找出平均分最高的班。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第五阶段就过关了！"""),
]

answer = [
    md("""# 第五阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""import pandas as pd
df = pd.read_csv("students.csv")
print("总行数：", len(df))
print(df.isna().sum())
print("数学平均：", round(df["数学"].mean(), 1))
print("数学最高：", df["数学"].max())"""),
    md("""## 题 2 参考答案"""),
    code("""import pandas as pd
df = pd.read_csv("students.csv").dropna()
top = df[(df["语文"] > 85) & (df["数学"] > 85)]
top = top.sort_values("语文", ascending=False)
print(top.head(5))"""),
    md("""## 题 3 参考答案"""),
    code("""import pandas as pd
df = pd.read_csv("students.csv")
clean = df.fillna({
    "语文": df["语文"].mean(),
    "数学": df["数学"].mean(),
    "英语": df["英语"].mean(),
})
print(clean.isna().sum())"""),
    md("""## 题 4 参考答案"""),
    code("""import pandas as pd
df = pd.read_csv("students.csv")
clean = df.dropna()
eng = clean.groupby("班级")["英语"].mean()
print(eng)
print("平均分最高的班：", eng.idxmax())"""),
]

files = {
    "lesson_01_Pandas入门.ipynb": lesson01,
    "lesson_02_筛选清洗分组.ipynb": lesson02,
    "practice_05.ipynb": practice,
    os.path.join("answers", "practice_05_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
