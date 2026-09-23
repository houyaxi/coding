# -*- coding: utf-8 -*-
"""生成第十阶段（大模型应用）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_10_大模型应用"
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
    md("""# 第十阶段第一课：HuggingFace 入门

HuggingFace 的 transformers 库是使用大模型的标准方式。核心概念：Tokenizer（把文字变数字）和 Model（把数字变预测）。从上往下一块一块运行。

注意：第一次运行会从网上下载模型，需要联网，下载一次后本地有缓存。"""),
    md("""## 1. pipeline：一行代码用模型

pipeline 把加载、预处理、预测、后处理全封装了，是最简单的入口。"""),
    code("""from transformers import pipeline

# 下载一个小型情感分析模型（首次运行会联网下载）
classifier = pipeline("sentiment-analysis")
print(classifier("I love this course!"))
print(classifier("This is so boring..."))"""),
    md("""## 2. AutoTokenizer：文字变成编号

大模型只认识数字。Tokenizer 把文字切成词（token），再变成编号。"""),
    code("""from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

ids = tokenizer("Hello, how are you?")["input_ids"]
print(ids)                    # 每个词/子词的编号
print(tokenizer.decode(ids))  # 编号还原回文字"""),
    md("""## 3. AutoModel：加载模型本体"""),
    code("""from transformers import AutoModel

model = AutoModel.from_pretrained("distilbert-base-uncased")
print(type(model))
print(model.config.hidden_size)   # 模型的向量维度"""),
    md("""## 4. 把文本变成向量（嵌入）"""),
    code("""import torch

inputs = tokenizer("machine learning is fun", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

print(outputs.last_hidden_state.shape)  # (1, 词数, 768)
# 每个词被表示成一个 768 维向量，这就是模型"理解"文本的方式"""),
    md("""## 5. 练习（自己动手写）

练习 1：用 pipeline 试试其他任务：text-classification、fill-mask（提示：pipeline("fill-mask")，输入 "The capital of France is [MASK]."）。

练习 2：用 AutoTokenizer 把你自己的中文名字编码成 input_ids，再 decode 回来看是否一致。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第十阶段第二课：文本生成与提示工程

这一课用生成式模型，体验"给模型一句话，它接着往下写"。大模型的能力很大程度上取决于你怎么提问（prompt）。"""),
    md("""## 1. 加载一个生成模型

用一个小的文本生成模型（gpt2 很小，几秒能加载）。首次运行需联网下载。"""),
    code("""from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", max_new_tokens=50)
print("模型加载完成")"""),
    md("""## 2. 最简单的生成"""),
    code("""result = generator("Once upon a time,")
print(result[0]["generated_text"])"""),
    md("""## 3. 生成参数的影响

temperature 控制随机性（越高越发散），do_sample 开启随机采样。"""),
    code("""print(generator("The best way to learn programming is", temperature=0.9)[0]["generated_text"])
print("---")
print(generator("The best way to learn programming is", temperature=0.1)[0]["generated_text"])"""),
    md("""## 4. 提示工程：用提示词引导输出

模型不知道任务，要靠 prompt 说明。对比下面两种问法的差异。"""),
    code("""# 不引导：模型自由发挥
print(generator("China is", max_new_tokens=30)[0]["generated_text"])

print("======")

# 明确任务式 prompt
prompt = "Translate the following English to Chinese. English: 'I love Python.' Chinese:"
print(generator(prompt, max_new_tokens=30)[0]["generated_text"])"""),
    md("""## 5. 用 pipeline 做文本摘要/问答（可选体验）

transformers 里还有很多任务 pipeline，机制都一样。"""),
    code("""# 文本摘要（首次运行会下载模型）
# summarizer = pipeline("summarization")
# text = "Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data."
# print(summarizer(text, max_length=30)[0]["summary_text"])"""),
    md("""## 6. 练习（自己动手写）

练习 1：给 generator 三个不同的开头，观察生成结果的差异（比如 "In 2050, humans"、"My favorite food is"、"The weather today is"）。

练习 2：用提示词让模型写出一个"列出 3 个学习 Python 的理由"的列表。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第十阶段综合练习

覆盖 pipeline、Tokenizer、文本生成、提示工程。模型下载需要联网，首次运行耐心等待。"""),
    md("""## 题 1：多任务 pipeline

用 pipeline 分别体验：情感分析、完形填空（fill-mask）。各给一个输入，打印结果。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：分词与还原

加载 AutoTokenizer（用 distilbert-base-uncased），把你喜欢的一句话编码再解码，对比原文。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：生成对比（挑战）

用 gpt2 对同一个开头分别用 temperature=0.1 和 1.5 生成，对比两次结果的差异，用注释说明你观察到了什么。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第十阶段就过关了！"""),
]

answer = [
    md("""# 第十阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""from transformers import pipeline

sa = pipeline("sentiment-analysis")
print(sa("Python is my favorite language"))

fm = pipeline("fill-mask")
print(fm("I like to [MASK] in my free time"))"""),
    md("""## 题 2 参考答案"""),
    code("""from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
sentence = "deep learning changes the world"
ids = tokenizer(sentence)["input_ids"]
print(ids)
print(tokenizer.decode(ids))"""),
    md("""## 题 3 参考答案"""),
    code("""from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", max_new_tokens=40)

print("低温（0.1）：")
print(generator("The future of AI is", temperature=0.1)[0]["generated_text"])
print("高温（1.5）：")
print(generator("The future of AI is", temperature=1.5)[0]["generated_text"])
# 观察：低温更保守重复，高温更跳跃甚至跑题"""),
]

files = {
    "lesson_01_HuggingFace入门.ipynb": lesson01,
    "lesson_02_文本生成与提示工程.ipynb": lesson02,
    "practice_10.ipynb": practice,
    os.path.join("answers", "practice_10_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
