# -*- coding: utf-8 -*-
"""验证 stage_02 讲义与答案 notebook 可执行。"""
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor

base = r"C:\Users\26643\Desktop\古法编程\stage_02_控制流与函数"
files = [
    "lesson_01_if条件判断.ipynb",
    "lesson_02_for循环与while.ipynb",
    "lesson_03_函数与lambda.ipynb",
]
for name in files:
    path = os.path.join(base, name)
    nb = nbformat.read(path, as_version=4)
    try:
        ExecutePreprocessor(timeout=60, kernel_name="python3").preprocess(
            nb, {"metadata": {"path": base}}
        )
        print(name, "-> 讲义代码块全部执行成功")
    except Exception as e:
        print(name, "-> 失败:", e)

# 答案：把含 input 的猜数字 cell 换成固定输入再执行
path = os.path.join(base, "answers", "practice_02_answer.ipynb")
nb = nbformat.read(path, as_version=4)
for c in nb.cells:
    if c.cell_type == "code" and "input(" in c.source:
        c.source = """secret = 33
times = 0
for guess in [20, 40, 33]:
    times = times + 1
    if guess > secret:
        print("大了")
    elif guess < secret:
        print("小了")
    else:
        print(f"猜对了！共猜了{times}次")
        break"""
try:
    ExecutePreprocessor(timeout=60, kernel_name="python3").preprocess(
        nb, {"metadata": {"path": base}}
    )
    print("practice_02_answer.ipynb -> 答案代码块全部执行成功")
except Exception as e:
    print("practice_02_answer.ipynb -> 失败:", e)
