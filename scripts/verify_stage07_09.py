# -*- coding: utf-8 -*-
"""验证第 7-9 阶段 notebook 可执行。"""
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor

jobs = [
    (r"C:\Users\26643\Desktop\古法编程\stage_07_pytorch张量与自动求导", ["lesson_01_张量基础.ipynb", "lesson_02_自动求导与数据加载.ipynb", os.path.join("answers", "practice_07_answer.ipynb")]),
    (r"C:\Users\26643\Desktop\古法编程\stage_08_深度学习模型构建", ["lesson_01_构建训练线性模型.ipynb", "lesson_02_MLP分类手写数字.ipynb", os.path.join("answers", "practice_08_answer.ipynb")]),
    (r"C:\Users\26643\Desktop\古法编程\stage_09_transformer原理与实现", ["lesson_01_注意力机制.ipynb", "lesson_02_小型Transformer实现.ipynb", os.path.join("answers", "practice_09_answer.ipynb")]),
]
for base, names in jobs:
    for name in names:
        path = os.path.join(base, name)
        nb = nbformat.read(path, as_version=4)
        try:
            ExecutePreprocessor(timeout=180, kernel_name="python3").preprocess(
                nb, {"metadata": {"path": base}}
            )
            print(os.path.basename(base), "/", name.split(os.sep)[-1], "-> 执行成功")
        except Exception as e:
            print(os.path.basename(base), "/", name.split(os.sep)[-1], "-> 失败:", type(e).__name__, e)
