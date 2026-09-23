# -*- coding: utf-8 -*-
"""
生成第三阶段（class 面向对象）的 Jupyter Notebook 讲义与练习。
包含：
  lesson_01_类与对象.ipynb
  lesson_02_继承与魔法方法.ipynb
  practice_03.ipynb
  answers/practice_03_answer.ipynb
"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_03_class面向对象"
nb = nbf.v4


def make_nb(cells):
    notebook = nb.new_notebook()
    notebook.metadata = {
        "kernelspec": {"display_name": "Python 3 (python310)", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    }
    notebook.cells = cells
    return notebook


def md(t):
    return nb.new_markdown_cell(t)


def code(t):
    return nb.new_code_cell(t)


# ============================================================
# lesson_01_类与对象.ipynb
# ============================================================
lesson01_cells = [
    md("""# 第三阶段第一课：类与对象

面向对象编程（OOP）：把数据和操作数据的方法打包成一个"类"，再用它创建具体的"对象"。从上往下一块一块运行。"""),
    md("""## 1. 什么是类和对象

类是模板，对象是按模板造出来的具体东西。比如"狗"是类（模板），"旺财，3岁"是对象（具体那只狗）。"""),
    md("""## 2. 定义类：class、__init__、self

class 类名 定义类；__init__ 是初始化方法，创建对象时自动运行；self 代表"对象自己"，所有方法第一个参数都是它。"""),
    code("""class Dog:
    def __init__(self, name, age):
        # self.name 把传入的名字存到对象身上
        self.name = name
        self.age = age

    def bark(self):
        # 方法里用 self.name 访问这个对象自己的数据
        print(f"{self.name}：汪汪汪！")"""),
    md("""## 3. 创建对象并使用

类名(参数) 创建对象，然后通过 对象.属性、对象.方法() 访问。"""),
    code("""my_dog = Dog("旺财", 3)

# 访问属性
print(my_dog.name)
print(my_dog.age)

# 调用方法
my_dog.bark()"""),
    md("""## 4. 同一个类造多个对象

类是模板，造出来的每个对象互相独立，数据各管各的。"""),
    code("""dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 5)

dog1.bark()
dog2.bark()

print(f"{dog1.name}今年{dog1.age}岁，{dog2.name}今年{dog2.age}岁")"""),
    md("""## 5. 修改对象的属性

属性可以直接改，用 对象.属性 = 新值。"""),
    code("""my_dog = Dog("旺财", 3)
print(my_dog.age)

my_dog.age = 4        # 直接改
print(my_dog.age)"""),
    md("""## 6. 练习（自己动手写）

练习 1：定义一个 Student 类，属性有 name 和 score，方法 introduce 打印"我叫XX，成绩XX分"。创建两个学生对象并调用 introduce。

练习 2：定义一个 Car 类，属性有 brand（品牌）和 speed（速度），方法 accelerate 让 speed 增加 10 并打印当前速度。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# lesson_02_继承与魔法方法.ipynb
# ============================================================
lesson02_cells = [
    md("""# 第三阶段第二课：继承与魔法方法

继承让一个类复用另一个类的属性和方法；魔法方法让对象和 Python 内置行为（print、len、==）配合得更自然。"""),
    md("""## 1. 类属性：所有对象共享的数据

写在类里但不在 __init__ 里的变量，所有对象共用一份。"""),
    code("""class Dog:
    species = "犬科"      # 类属性，所有狗共享

    def __init__(self, name, age):
        self.name = name

dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 5)

print(dog1.species)       # 都能访问
print(dog2.species)
print(Dog.species)        # 也可以类名直接访问"""),
    md("""## 2. 继承：子类复用父类

class 子类(父类)：子类自动拥有父类的所有属性和方法。"""),
    code("""class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}发出声音")

# Dog 继承 Animal
class Dog(Animal):
    pass

# Dog 自动有了 Animal 的 __init__ 和 speak
my_dog = Dog("旺财")
my_dog.speak()"""),
    md("""## 3. 重写：子类改父类的方法

子类定义同名方法，就覆盖父类的版本。"""),
    code("""class Cat(Animal):
    # 重写 speak 方法
    def speak(self):
        print(f"{self.name}：喵喵喵")

my_cat = Cat("咪咪")
my_cat.speak()"""),
    md("""## 4. super()：调用父类的初始化

子类要加自己的属性时，用 super().__init__() 先把父类的初始化做完，再加自己的。"""),
    code("""class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)   # 先做父类的初始化
        self.age = age            # 再加自己的属性

my_dog = Dog("旺财", 3)
print(my_dog.name, my_dog.age)"""),
    md("""## 5. 魔法方法 __str__：让 print(对象) 更好看

默认 print(对象) 打印一串看不懂的内存地址。__str__ 定义"打印这个对象时显示什么"。"""),
    code("""class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"狗：{self.name}，{self.age}岁"

my_dog = Dog("旺财", 3)
print(my_dog)        # 不再是 <__main__.Dog object ...>，而是友好的文字"""),
    md("""## 6. 其他常用魔法方法 __len__ 和 __eq__

__len__：让 len(对象) 生效；__eq__：让 对象1 == 对象2 生效。"""),
    code("""class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members       # 列表

    def __len__(self):
        return len(self.members)    # len(team) 返回成员数

    def __eq__(self, other):
        return self.name == other.name

team_a = Team("红队", ["小明", "小红"])
team_b = Team("红队", ["小刚"])

print(len(team_a))        # 2
print(team_a == team_b)   # True，因为队名相同"""),
    md("""## 7. 练习（自己动手写）

练习 1：写一个 Person 类（name、age），再写一个继承它的 Student 类，加一个 score 属性（用 super() 初始化），加一个 study 方法打印"XX在学习"。

练习 2：给 Student 类加 __str__ 方法，让 print(student) 显示"学生：XX，X岁，成绩X分"。"""),
    code("""# 在这里写你的练习代码
"""),
]

# ============================================================
# practice_03.ipynb
# ============================================================
practice_cells = [
    md("""# 第三阶段综合练习

覆盖类的定义、属性、方法、继承、魔法方法。先自己写，运行通过后再对照 answers/practice_03_answer.ipynb。"""),
    md("""## 题 1：银行账户类

写一个 BankAccount 类：
- __init__ 接收 owner（户主）和 balance（余额，默认 0）
- 方法 deposit(amount)：存钱，余额增加，打印新余额
- 方法 withdraw(amount)：取钱，余额足够就扣，不够打印"余额不足"
创建一个账户，存 1000，取 300，再取 900，看结果。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：图书类与继承

写一个 Book 类：
- 属性：title（书名）、author（作者）
- __str__ 方法：print(book) 显示《书名》-作者
再写一个 EBook 类继承 Book，多一个属性 format（格式，如 PDF），重写 __str__ 显示格式。
创建一个普通书和一个电子书对象并打印。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：学生列表（面向对象+循环）

写一个 Student 类（name、score）。创建 3 个学生对象放在列表里，用 for 循环打印每个学生的 name 和 score，并找出分数最高的学生。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 4：矩形类（挑战题）

写一个 Rectangle 类，属性 width 和 height，方法：
- area()：返回面积
- __str__：显示"矩形宽X高Y，面积Z"
创建两个矩形对象，比较面积大小（提示：直接调用 area() 比），打印结果。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第三阶段就过关了！"""),
]

# ============================================================
# answers/practice_03_answer.ipynb
# ============================================================
answer_cells = [
    md("""# 第三阶段综合练习参考答案

先自己写，运行通过后再对照。重点看：__init__ 的 self、方法定义、继承时 super() 的用法。"""),
    md("""## 题 1 参考答案：银行账户类"""),
    code("""class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner}存入{amount}，余额{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance = self.balance - amount
            print(f"{self.owner}取出{amount}，余额{self.balance}")

acc = BankAccount("小明", 1000)
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(900)"""),
    md("""## 题 2 参考答案：图书类与继承"""),
    code("""class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"《{self.title}》-{self.author}"


class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

    def __str__(self):
        return f"《{self.title}》-{self.author}（{self.format}）"


b1 = Book("活着", "余华")
b2 = EBook("三体", "刘慈欣", "PDF")
print(b1)
print(b2)"""),
    md("""## 题 3 参考答案：学生列表"""),
    code("""class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


students = [
    Student("小明", 85),
    Student("小红", 92),
    Student("小刚", 78),
]

top = students[0]
for s in students:
    print(f"{s.name}：{s.score}分")
    if s.score > top.score:
        top = s

print(f"最高分：{top.name}，{top.score}分")"""),
    md("""## 题 4 参考答案：矩形类"""),
    code("""class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"矩形宽{self.width}高{self.height}，面积{self.area()}"


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 2)

print(r1)
print(r2)

if r1.area() > r2.area():
    print("矩形1面积更大")
else:
    print("矩形2面积更大或相等")"""),
]

# ============================================================
# 写出文件
# ============================================================
files = {
    "lesson_01_类与对象.ipynb": lesson01_cells,
    "lesson_02_继承与魔法方法.ipynb": lesson02_cells,
    "practice_03.ipynb": practice_cells,
    os.path.join("answers", "practice_03_answer.ipynb"): answer_cells,
}

for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
