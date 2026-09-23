# -*- coding: utf-8 -*-
"""
生成第二阶段（控制流与函数）的 Jupyter Notebook 讲义与练习。
生成后包含 5 个文件：
  lesson_01_if条件判断.ipynb
  lesson_02_for循环与while.ipynb
  lesson_03_函数与lambda.ipynb
  practice_02.ipynb
  answers/practice_02_answer.ipynb
"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_02_控制流与函数"

nb = nbf.v4


def make_nb(cells):
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
# lesson_01_if条件判断.ipynb
# ============================================================
lesson01_cells = [
    md("""# 第二阶段第一课：if 条件判断

程序默认从上往下顺序执行，if 让程序学会"看情况决定做不做"。从上往下一块一块运行。"""),
    md("""## 1. 比较运算

比较运算的结果是布尔值 True 或 False：等于 ==、不等于 !=、小于 <、大于 >、小于等于 <=、大于等于 >=。"""),
    code("""a = 10
b = 20

print(a == b)    # False
print(a != b)    # True
print(a < b)     # True
print(a >= 10)   # True

# 比较结果可以直接保存
result = a < b
print(result)"""),
    md("""## 2. 最简单的 if

if 后面跟条件，条件为 True 就执行缩进的代码块，否则跳过。注意缩进（4 个空格）是 Python 的语法，不能省略。"""),
    code("""age = 20

if age >= 18:
    print("你已经成年了")

print("程序继续运行")"""),
    md("""## 3. if / else：二选一

else 在条件不成立时执行。"""),
    code("""score = 59

if score >= 60:
    print("及格")
else:
    print("不及格")"""),
    md("""## 4. if / elif / else：多选一

elif 是"否则如果"，可以有多个，从上到下检查，命中第一个成立的就执行。"""),
    code("""score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 85 命中第二个条件，输出"良好"；后面的条件不会再检查"""),
    md("""## 5. 逻辑运算：and / or / not

- and：两边都成立才为 True
- or：有一边成立就为 True
- not：取反"""),
    code("""age = 25
has_id = True

# 两个条件同时满足
if age >= 18 and has_id:
    print("可以进网吧")

# 有一个满足即可
if age < 12 or age > 80:
    print("免费乘车")
else:
    print("正常购票")

# 取反
if not has_id:
    print("没带证件")"""),
    md("""## 6. 练习（自己动手写）

练习 1：输入一个整数（直接赋值即可），判断它是奇数还是偶数（偶数：x % 2 == 0）。

练习 2：给一个 0-100 的分数，用 if/elif/else 输出评级：90 以上优秀，80-89 良好，70-79 中等，60-69 及格，60 以下不及格。

练习 3：给一个年份（如 2024），判断是不是闰年。闰年规则：能被 4 整除但不能被 100 整除，或者能被 400 整除。
提示：year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

在下面的代码块写答案，做完对照 answers/practice_02_answer.ipynb。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# lesson_02_for循环与while.ipynb
# ============================================================
lesson02_cells = [
    md("""# 第二阶段第二课：for 循环与 while 循环

循环让程序重复做同一件事，是消除重复代码的核心武器。"""),
    md("""## 1. for 循环遍历列表

for 变量 in 列表：依次取出列表里的每个元素，执行一次缩进的代码块。"""),
    code("""hobbies = ["编程", "跑步", "看电影"]

for h in hobbies:
    print(f"我喜欢{h}")

print("循环结束")"""),
    md("""## 2. range()：生成数字序列

range(5) 生成 0,1,2,3,4（不含 5）；range(1,6) 生成 1 到 5；range(1,10,2) 表示从 1 到 9 步长 2。"""),
    code("""# 从 0 到 4
for i in range(5):
    print(i)

print("---")

# 从 1 到 5
for i in range(1, 6):
    print(i)

print("---")

# 步长 2：1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)"""),
    md("""## 3. 用 for 做累加

在循环外先准备一个变量，循环里不断更新它，这是最常用的模式。"""),
    code("""total = 0

for i in range(1, 101):
    total = total + i

print(f"1 到 100 的和是：{total}")"""),
    md("""## 4. while 循环

while 后面跟条件，条件为 True 就一直循环，直到条件变 False。注意：一定要有让条件变化的语句，否则会死循环。"""),
    code("""count = 1

while count <= 5:
    print(f"第{count}次")
    count = count + 1   # 这一行让循环能结束

print("循环结束")"""),
    md("""## 5. break 和 continue

- break：立刻跳出整个循环
- continue：跳过本次，进入下一次循环"""),
    code("""# break 示例：找到第一个能被 7 整除的数就停
for i in range(1, 100):
    if i % 7 == 0:
        print(f"第一个能被7整除的是{i}")
        break"""),
    code("""# continue 示例：只打印奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue        # 偶数直接跳过
    print(i)"""),
    md("""## 6. 用循环改写重复代码

第二课随机密码那题你写了 6 遍 random.choice，现在一行循环就搞定："""),
    code("""import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = ""

for _ in range(6):
    password = password + random.choice(chars)

print(f"生成的密码：{password}")"""),
    md("""## 7. 练习（自己动手写）

练习 1：用 for 循环打印 1 到 20 的所有偶数。

练习 2：用 for 循环计算 1 到 100 里所有能被 3 整除的数的和。

练习 3：用 while 循环从 100 开始往下数，每 5 个数打印一次（100, 95, 90, ...），数到 0 停止。

练习 4：用 for 循环 + random 生成 10 个 1-100 的随机整数存入列表，再循环统计其中大于 50 的有几个。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# lesson_03_函数与lambda.ipynb
# ============================================================
lesson03_cells = [
    md("""# 第二阶段第三课：函数与 lambda

函数把一段可重复使用的代码打包，起个名字，需要时调用。"""),
    md("""## 1. 定义函数：def

def 函数名(参数): 定义函数，函数体缩进。定义后要调用才会执行。"""),
    code("""def say_hello():
    print("你好呀！")

# 调用函数
say_hello()
say_hello()"""),
    md("""## 2. 带参数和返回值

参数让函数处理不同的输入，return 把结果交给调用者。"""),
    code("""def add(a, b):
    result = a + b
    return result

x = add(3, 5)
print(x)                    # 8
print(add(100, 200))        # 300

# 没有 return 时函数返回 None
def nothing():
    print("我没有返回值")

r = nothing()
print(r)                    # None"""),
    md("""## 3. 默认参数

给参数一个默认值，调用时可以不传。"""),
    code("""def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(greet("小明"))             # 你好，小明！
print(greet("小红", "早上好"))    # 早上好，小红！"""),
    md("""## 4. lambda 匿名函数

lambda 用于写简单的一次性函数，格式：lambda 参数: 表达式。常用在需要"传入一个函数"的场景。"""),
    code("""# 普通函数写法
def double(x):
    return x * 2

# lambda 写法，两者等价
double2 = lambda x: x * 2

print(double(10))       # 20
print(double2(10))      # 20

# 配合 sorted 使用：按元组第二个元素排序
pairs = [(1, 5), (3, 2), (2, 8)]
pairs_sorted = sorted(pairs, key=lambda p: p[1])
print(pairs_sorted)     # [(3, 2), (1, 5), (2, 8)]"""),
    md("""## 5. 列表推导式

一行生成列表，是 Python 的标志性写法，替代"建空列表 + for + append"。"""),
    code("""# 普通写法
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)          # [1, 4, 9, 16, 25]

# 列表推导式一行完成
squares2 = [i * i for i in range(1, 6)]
print(squares2)         # [1, 4, 9, 16, 25]

# 可以加 if 过滤
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)            # 1 到 20 的偶数"""),
    md("""## 6. 练习（自己动手写）

练习 1：写一个函数 area_of_circle(r)，返回半径为 r 的圆面积（用 math.pi），调用它算半径 3 和 7 的面积。

练习 2：写一个函数 is_prime(n)，判断 n 是不是质数（只能被 1 和自身整除，提示：用 for 检查 2 到 n-1，有整除就返回 False），调用它判断 17 和 25。

练习 3：用列表推导式生成 1 到 100 中所有能被 7 整除的数。

练习 4：写一个函数 max_of_list(lst)，返回列表里最大的数（不要用内置 max，用 for 循环自己找），测试 [3, 9, 1, 7, 5]。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# practice_02.ipynb（综合练习）
# ============================================================
practice_cells = [
    md("""# 第二阶段综合练习

覆盖 if、for、while、函数。先自己写，运行通过后再对照 answers/practice_02_answer.ipynb。"""),
    md("""## 题 1：偶数筛选

用 for 循环打印 1 到 50 中所有能被 5 整除的数，每行一个。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：成绩评级函数

写一个函数 grade(score)，分数 90 以上返回"优秀"，80-89"良好"，70-79"中等"，60-69"及格"，否则"不及格"。分别调用它计算 95、73、45 的结果并打印。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：累加求和函数

写一个函数 sum_to(n)，用 while 循环计算 1+2+...+n 的和并返回。调用 sum_to(100) 验证结果是 5050。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：统计大于平均值

用 random 生成 20 个 1-100 的随机整数存入列表，计算平均值（sum 除以个数），再用循环统计列表里大于平均值的数有几个，打印结果。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 5：猜数字小游戏

程序随机生成一个 1-50 的整数，用 while 循环让用户猜（用 input 输入，int 转换）。猜大了提示"大了"，猜小了提示"小了"，猜中提示"猜对了！共猜了N次"并结束循环。
（在 notebook 里运行 input 会弹输入框，正常体验即可）"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第二阶段就过关了！"""),
]

# ============================================================
# answers/practice_02_answer.ipynb（参考答案）
# ============================================================
answer_cells = [
    md("""# 第二阶段综合练习参考答案

先自己写，运行通过后再对照。重点看：循环和条件是否写对，函数是否合理复用。"""),
    md("""## 题 1 参考答案：偶数筛选"""),
    code("""for i in range(1, 51):
    if i % 5 == 0:
        print(i)"""),
    md("""## 题 2 参考答案：成绩评级函数"""),
    code("""def grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

print(grade(95))    # 优秀
print(grade(73))    # 中等
print(grade(45))    # 不及格"""),
    md("""## 题 3 参考答案：累加求和函数"""),
    code("""def sum_to(n):
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total

print(sum_to(100))   # 5050"""),
    md("""## 题 4 参考答案：统计大于平均值

也可以用列表推导式简化最后一步：
greater = [x for x in nums if x > avg]"""),
    code("""import random

nums = [random.randint(1, 100) for _ in range(20)]
print(f"生成的列表：{nums}")

avg = sum(nums) / len(nums)
print(f"平均值：{round(avg, 2)}")

count = 0
for x in nums:
    if x > avg:
        count = count + 1

print(f"大于平均值的个数：{count}")"""),
    md("""## 题 5 参考答案：猜数字小游戏"""),
    code("""import random

secret = random.randint(1, 50)
times = 0

while True:
    guess = int(input("请猜一个 1-50 的数字："))
    times = times + 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"猜对了！共猜了{times}次")
        break"""),
]

# ============================================================
# 写出文件
# ============================================================
files = {
    "lesson_01_if条件判断.ipynb": lesson01_cells,
    "lesson_02_for循环与while.ipynb": lesson02_cells,
    "lesson_03_函数与lambda.ipynb": lesson03_cells,
    "practice_02.ipynb": practice_cells,
    os.path.join("answers", "practice_02_answer.ipynb"): answer_cells,
}

for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
