# -*- coding: utf-8 -*-
"""
生成第一阶段的 Jupyter Notebook 讲义与练习。
把原有的 .py 讲义拆分为 markdown 讲解块 + 代码块，便于分块学习。
运行后生成 4 个 .ipynb 文件。
"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_01_python基础"

nb = nbf.v4


def make_nb(cells, title):
    notebook = nb.new_notebook()
    notebook.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (python310)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python"},
    }
    notebook.cells = cells
    return notebook


def md(text):
    return nb.new_markdown_cell(text)


def code(text):
    return nb.new_code_cell(text)


# ============================================================
# lesson_01_print与变量.ipynb
# ============================================================
lesson01_cells = [
    md("""# 第一课：print 输出与变量

本 notebook 是讲义，从上往下一块一块运行。点代码块左侧的运行按钮，或选中代码块后按 Shift+Enter 运行。
每运行一块，立刻就能看到结果。

如果右上角 Kernel 不是 Python 3，点右上角 Kernel > Change kernel 选择 python310 对应的 Python 3。"""),
    md("""## 1. print 的基础用法

print 会把内容输出到屏幕上，这是你观察程序结果最重要的方式。"""),
    code("""print("你好，编程！")
print(123)
print(3.14)

# 可以一次打印多个内容，print 会在它们之间加一个空格
print("今天", "天气", "不错")

# 用 sep 参数自定义分隔符
print("2026", "09", "23", sep="-")

# 用 end 参数控制结尾，默认是换行，可以改成空格或其他
print("第一行", end=" ")
print("第二行")"""),
    md("""## 2. 变量：给数据起个名字

变量名 = 值，之后就可以用名字来引用这个值。"""),
    code("""name = "小明"
age = 25
height = 1.75

print(name)
print(age)
print(height)

# 变量可以重新赋值，新的值会覆盖旧的值
age = 26
print(age)

# 变量命名规则：字母、数字、下划线，不能以数字开头，不能用关键字
# 习惯用小写字母 + 下划线，例如 user_name、my_age"""),
    md("""## 3. 常见数据类型

整数 int、浮点数 float、字符串 str、布尔值 bool。type() 可以查看变量的类型。"""),
    code("""a = 10      # 整数 int
b = 3.5     # 浮点数 float
c = "hello" # 字符串 str
d = True    # 布尔值 bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))"""),
    md("""## 4. 数字运算"""),
    code("""print(10 + 3)     # 加法 13
print(10 - 3)     # 减法 7
print(10 * 3)     # 乘法 30
print(10 / 3)     # 除法 3.333...
print(10 // 3)    # 整除 3
print(10 % 3)     # 取余 1
print(2 ** 3)     # 幂运算 8"""),
    md("""## 5. 字符串拼接与格式化

f-string：在引号前加 f，用 {变量名} 直接嵌入变量，这是最常用的格式化方式。"""),
    code("""greeting = "你好，" + name
print(greeting)

message = f"{name}今年{age}岁，身高{height}米"
print(message)

# 可以嵌入表达式
print(f"明年{age}岁，后年{age + 1}岁")"""),
    md("""## 6. 输入：input()

input() 让程序停下来等用户输入，输入的内容是字符串。这里把示例注释掉了，想体验可以取消注释运行。"""),
    code("""# your_name = input("请输入你的名字：")
# print(f"你好，{your_name}！")

# 如果输入的是数字，要转换类型才能运算
# num = input("请输入一个数字：")
# num = int(num)
# print(f"它的两倍是{num * 2}")"""),
    md("""## 练习（自己动手写）

练习 1：创建三个变量：你的名字、年龄、喜欢的编程语言，用 f-string 打印一句话把它们组合起来。

练习 2：计算并打印一个半径为 5 的圆的周长（公式 2 * 3.14159 * r）。

练习 3：打印一个 3 行 3 列的简单乘法口诀表中的一行，例如 "3 x 4 = 12"，用 sep 或 f-string 实现。

在下面的代码块里写你的答案，写完运行。参考答案在 answers/practice_01_answer.ipynb 里，做完再对照。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# lesson_02_import导入.ipynb
# ============================================================
lesson02_cells = [
    md("""# 第二课：import 导入

Python 的强大之处在于海量的现成库（模块）。导入库就能直接用别人写好的功能。本 notebook 是讲义，从上往下一块一块运行。"""),
    md("""## 1. 导入方式一：import 模块名

导入 math 数学库，然后用 模块名.函数名 的方式调用。"""),
    code("""import math

print(math.sqrt(16))        # 开平方 → 4.0
print(math.pi)              # 圆周率
print(math.floor(3.7))      # 向下取整 → 3
print(math.ceil(3.2))       # 向上取整 → 4"""),
    md("""## 2. 导入方式二：from 模块 import 名字

只导入模块里的某个函数，之后直接写函数名，不用带模块名。注意：这种方式容易和同名函数冲突，大型项目建议用方式一。"""),
    code("""from math import sqrt, log

print(sqrt(25))             # 5.0
print(log(2.718281828))     # 自然对数，接近 1"""),
    md("""## 3. 导入方式三：as 起别名

有些库名字长，起个简短别名，之后统一用别名。numpy 和 pandas 是后面阶段的主角，这里先认识一下。"""),
    code("""import numpy as np
import pandas as pd

arr = np.array([1, 2, 3])
print(arr)                  # [1 2 3]"""),
    md("""## 4. 常用标准库速览

Python 自带的库，不用额外安装：random（随机数）、datetime（日期时间）、os（操作系统）。"""),
    code("""import random
print(random.randint(1, 100))     # 1 到 100 的随机整数
print(random.choice(["苹果", "香蕉", "橘子"]))  # 随机选一个"""),
    code("""import datetime
now = datetime.datetime.now()
print(now)                          # 当前日期时间
print(now.year, now.month, now.day) # 分别取年、月、日"""),
    code("""import os
print(os.getcwd())                  # 当前工作目录"""),
    md("""## 5. 查看模块里有什么：dir()

dir(模块名) 列出模块的所有函数和属性，忘了有什么可以查。"""),
    code("""import math
print(dir(math))            # 输出很长，看个大概即可"""),
    md("""## 6. import 的执行效果

无论 import 多少次，模块代码只执行一次，重复导入没有副作用。"""),
    md("""## 练习（自己动手写）

练习 1：导入 math，计算半径为 7 的圆的面积（公式 pi * r * r），用 f-string 打印，保留 2 位小数（用 round(值, 2)）。

练习 2：导入 random，随机生成 5 个 1-100 的整数，用列表存起来并打印。

练习 3：导入 datetime，打印"今天是一年中的第几天"（提示：now.timetuple().tm_yday）。

练习 4：导入 os，打印当前目录下所有文件和文件夹的名字（提示：os.listdir(".")）。

在下面的代码块里写你的答案，写完运行。做完再对照 answers/practice_01_answer.ipynb。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# practice_01.ipynb（综合练习）
# ============================================================
practice_cells = [
    md("""# 第一阶段综合练习

独立完成下面 5 道题。先自己写，运行通过后再对照 answers/practice_01_answer.ipynb 的参考答案。
写不出来的题先跳过，做完其他题再回来想，还是卡住就发到对话里问我。"""),
    md("""## 题 1：个人信息卡

创建变量：姓名、年龄、城市、爱好（爱好用列表存多个），用 f-string 打印成一段自我介绍。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：温度转换

摄氏温度 c = 26.5，转成华氏温度 f = c * 9 / 5 + 32，用 f-string 打印，华氏温度保留 1 位小数。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：随机密码生成器

用 random 从数字和字母里随机挑 6 个字符组成一个"密码"并打印。
提示：import random，random.choice("abcdefg123456") 每次挑一个。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：面积计算

用 math.pi 计算一个半径 r = 12 的圆的面积，再计算半径翻倍后的面积，打印两者之比。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 5：日期分析

获取当前时间，打印：
a) 今天是星期几（提示：now.strftime("%A")）
b) 现在距 2030 年 1 月 1 日还有多少天（提示：目标日 datetime.datetime(2030,1,1)，两者相减取 .days）"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完后运行没有报错，就说明第一阶段基础过关了！"""),
]

# ============================================================
# answers/practice_01_answer.ipynb（参考答案）
# ============================================================
answer_cells = [
    md("""# 第一阶段综合练习参考答案

建议：先自己写，运行通过后再打开本文件对照。对照时重点看：
- 思路是否一致（做法可以不同，结果对就行）
- 有没有用上 f-string、import、类型转换"""),
    md("""## 题 1 参考答案：个人信息卡"""),
    code("""name = "小明"
age = 25
city = "上海"
hobbies = ["编程", "跑步", "看电影"]
intro = f"我叫{name}，今年{age}岁，住在{city}，爱好是{hobbies}"
print(intro)
# 输出：我叫小明，今年25岁，住在上海，爱好是['编程', '跑步', '看电影']"""),
    md("""## 题 2 参考答案：温度转换"""),
    code("""c = 26.5
f = c * 9 / 5 + 32
print(f"摄氏{c}度 = 华氏{round(f, 1)}度")
# 输出：摄氏26.5度 = 华氏79.7度"""),
    md("""## 题 3 参考答案：随机密码生成器

每次运行结果不同。另一种更简洁的写法（列表推导式，阶段 2 会学）：
password2 = "".join(random.choice(chars) for _ in range(6))"""),
    code("""import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""
for _ in range(6):
    password = password + random.choice(chars)
print(f"生成的密码：{password}")"""),
    md("""## 题 4 参考答案：面积计算

半径翻倍，面积变 4 倍。"""),
    code("""import math
r = 12
area1 = math.pi * r * r
area2 = math.pi * (2 * r) * (2 * r)
print(f"半径{r}的面积：{round(area1, 2)}")
print(f"半径翻倍后的面积：{round(area2, 2)}")
print(f"面积之比：{area2 / area1:.1f}倍")"""),
    md("""## 题 5 参考答案：日期分析"""),
    code("""import datetime
now = datetime.datetime.now()
print(f"今天是{now.strftime('%A')}")
target = datetime.datetime(2030, 1, 1)
days_left = (target - now).days
print(f"距离2030年1月1日还有{days_left}天")"""),
]

# ============================================================
# 写出文件
# ============================================================
files = {
    "lesson_01_print与变量.ipynb": lesson01_cells,
    "lesson_02_import导入.ipynb": lesson02_cells,
    "practice_01.ipynb": practice_cells,
    os.path.join("answers", "practice_01_answer.ipynb"): answer_cells,
}

for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells, name), f)
    print(f"已生成：{path}")
