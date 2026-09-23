# -*- coding: utf-8 -*-
"""生成第九阶段（Transformer 原理与实现）的 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\stage_09_transformer原理与实现"
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
    md("""# 第九阶段第一课：注意力机制

Transformer 的核心是注意力（Attention）。理解它只需要一个直觉：句子里的每个词，在看别的词时，应该"注意"到什么程度。这一课从零实现缩放点积注意力。"""),
    md("""## 1. Q、K、V 是什么

每个词都会生成三个向量：
- Query（Q）：我想找什么
- Key（K）：我是什么
- Value（V）：我实际提供的内容

注意力分数 = Q 和 K 的相似度。相似度高的词，它的 V 会占更大权重。"""),
    code("""import torch

# 3 个词，每个词用 4 维向量表示
# 这里的 Q K V 是简化版，直接随机生成演示
Q = torch.randn(3, 4)   # 3 个词的查询
K = torch.randn(3, 4)   # 3 个词的键
V = torch.randn(3, 4)   # 3 个词的值
print(Q)"""),
    md("""## 2. 计算注意力分数

分数 = Q 和 K 的点积，再除以 sqrt(d)（缩放，防止分数过大）。"""),
    code("""d = Q.shape[-1]
scores = Q @ K.T / (d ** 0.5)   # 3x3 的相似度矩阵
print(scores)"""),
    md("""## 3. 转成权重：softmax

softmax 把分数变成概率分布（每行加起来等于 1），表示每个词注意谁。"""),
    code("""import torch.nn.functional as F

weights = F.softmax(scores, dim=-1)
print(weights)
print(weights.sum(dim=-1))     # 每行和为 1"""),
    md("""## 4. 加权求和得到输出

用权重对 V 加权求和，得到每个词的注意力输出。"""),
    code("""output = weights @ V     # 3x4
print(output)"""),
    md("""## 5. 封装成一个函数：缩放点积注意力"""),
    code("""def scaled_dot_product_attention(Q, K, V):
    d = Q.shape[-1]
    scores = Q @ K.T / (d ** 0.5)
    weights = F.softmax(scores, dim=-1)
    return weights @ V, weights

out, w = scaled_dot_product_attention(Q, K, V)
print("输出形状：", out.shape)
print("注意力权重：")
print(w)"""),
    md("""## 6. 多头注意力：多个"视角"

多头注意力 = 把 Q K V 切成几份，各算各的注意力，再拼起来。每个头关注不同类型的关系。"""),
    code("""import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=16, n_head=4):
        super().__init__()
        self.n_head = n_head
        self.d_head = d_model // n_head
        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)
        self.Wo = nn.Linear(d_model, d_model)

    def forward(self, x):
        # x: (batch, seq_len, d_model)
        batch, seq, _ = x.shape
        q = self.Wq(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        k = self.Wk(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        v = self.Wv(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        scores = q @ k.transpose(-1, -2) / (self.d_head ** 0.5)
        weights = F.softmax(scores, dim=-1)
        attn = weights @ v
        attn = attn.transpose(1, 2).contiguous().view(batch, seq, -1)
        return self.Wo(attn)

mha = MultiHeadAttention()
x = torch.randn(2, 5, 16)    # 2 句话，每句 5 个词，16 维
print(mha(x).shape)          # 形状不变：2, 5, 16"""),
    md("""## 7. 练习（自己动手写）

练习 1：把上面的注意力函数抄一遍，输入 4 个词（Q K V 都是 4x8），确认输出是 4x8。

练习 2：解释一下为什么注意力要除以 sqrt(d)（提示：d 大时点积会很大，softmax 梯度会消失）。"""),
    code("""# 在这里写你的练习代码
"""),
]

lesson02 = [
    md("""# 第九阶段第二课：小型 Transformer 实现

把注意力 + 位置编码 + 前馈网络 + 残差连接拼起来，就是一个 Transformer。这一课实现一个能生成文本的字符级小型 Transformer。"""),
    md("""## 1. 位置编码

注意力本身不关心词的位置，所以要给每个位置加上位置信息。用 sin/cos 编码。"""),
    code("""import torch
import torch.nn as nn
import torch.nn.functional as F

def position_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    pos = torch.arange(seq_len).unsqueeze(1).float()
    div = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
    pe[:, 0::2] = torch.sin(pos * div)
    pe[:, 1::2] = torch.cos(pos * div)
    return pe

pe = position_encoding(10, 32)
print(pe.shape)     # 10 个位置，每个 32 维"""),
    md("""## 2. Transformer 块：注意力 + 前馈 + 残差 + 归一化

一个块 = 多头注意力 + LayerNorm + 前馈网络，中间都用残差连接。先补上多头注意力的定义（第一课学过，这里独立可运行）。"""),
    code("""import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=16, n_head=4):
        super().__init__()
        self.n_head = n_head
        self.d_head = d_model // n_head
        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)
        self.Wo = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch, seq, _ = x.shape
        q = self.Wq(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        k = self.Wk(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        v = self.Wv(x).view(batch, seq, self.n_head, self.d_head).transpose(1, 2)
        scores = q @ k.transpose(-1, -2) / (self.d_head ** 0.5)
        weights = F.softmax(scores, dim=-1)
        attn = weights @ v
        attn = attn.transpose(1, 2).contiguous().view(batch, seq, -1)
        return self.Wo(attn)"""),
    code("""class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_head, d_ff):
        super().__init__()
        self.attn = MultiHeadAttention(d_model, n_head)
        self.norm1 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model),
        )
        self.norm2 = nn.LayerNorm(d_model)

    def forward(self, x):
        x = x + self.attn(self.norm1(x))   # 残差 + 注意力
        x = x + self.ffn(self.norm2(x))    # 残差 + 前馈
        return x

block = TransformerBlock(d_model=32, n_head=4, d_ff=64)
x = torch.randn(2, 8, 32)
print(block(x).shape)"""),
    md("""## 3. 组装完整的 Transformer 语言模型

输入一串字符，预测下一个字符。用 one-hot 或嵌入把字符变成向量，经过几个 Transformer 块，输出每个位置下一个字符的概率。"""),
    code("""class CharTransformer(nn.Module):
    def __init__(self, vocab_size, d_model=32, n_head=4, n_layers=2, d_ff=64):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos = position_encoding(64, d_model)
        self.blocks = nn.Sequential(*[TransformerBlock(d_model, n_head, d_ff) for _ in range(n_layers)])
        self.out = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        # x: (batch, seq_len) 的字符编号
        x = self.embed(x) + self.pos[:x.size(1)].unsqueeze(0)
        x = self.blocks(x)
        return self.out(x)   # (batch, seq_len, vocab_size)"""),
    md("""## 4. 准备字符数据并训练

用一小段文本，让模型学会预测下一个字符。"""),
    code("""text = "hello world! this is a tiny transformer learning to generate text. "
chars = sorted(set(text))
char_to_idx = {c: i for i, c in enumerate(chars)}
idx_to_char = {i: c for i, c in enumerate(chars)}
vocab_size = len(chars)
print(f"字符表大小：{vocab_size}，字符：{chars}")"""),
    code("""def make_sequences(text, seq_len=16):
    ids = [char_to_idx[c] for c in text]
    xs, ys = [], []
    for i in range(len(ids) - seq_len):
        xs.append(ids[i:i+seq_len])
        ys.append(ids[i+1:i+seq_len+1])   # 每个位置的"下一个字符"
    return torch.tensor(xs), torch.tensor(ys)

seq_len = 16
xs, ys = make_sequences(text, seq_len)
print("样本数：", xs.shape, "标签形状：", ys.shape)"""),
    code("""model = CharTransformer(vocab_size, d_model=32, n_head=4, n_layers=2, d_ff=64)
optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
criterion = nn.CrossEntropyLoss()

for step in range(300):
    pred = model(xs)                       # (N, 16, vocab)
    loss = criterion(pred.reshape(-1, vocab_size), ys.reshape(-1))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if step % 100 == 0:
        print(f"step {step}, loss = {loss.item():.3f}")"""),
    md("""## 5. 用模型生成文本

从第一个字符开始，每步预测下一个字符，把预测结果接回去继续预测。"""),
    code("""def generate(model, start, length=50):
    model.eval()
    ids = [char_to_idx[c] for c in start]
    with torch.no_grad():
        for _ in range(length):
            input_ids = torch.tensor(ids[-seq_len:]).unsqueeze(0)
            logits = model(input_ids)[0, -1]
            next_id = logits.argmax().item()
            ids.append(next_id)
    return "".join(idx_to_char[i] for i in ids)

print(generate(model, "hello", 50))"""),
    md("""## 6. 练习（自己动手写）

练习 1：把训练步数从 300 改到 800，再生成一次文本，看是否更像原文。

练习 2：换一段更长的文本训练（自己写一段 200 字符的中文或英文），看模型能否学到一些规律。"""),
    code("""# 在这里写你的练习代码
"""),
]

practice = [
    md("""# 第九阶段综合练习

覆盖注意力计算、Transformer 组件、字符级生成。先自己写，运行通过后再对照 answers。"""),
    md("""## 题 1：手工注意力计算

不用库，用手写代码计算 3 个词（d=2）的缩放点积注意力权重。Q K V 自己定值，打印每行的权重和（应为 1）。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 2：位置编码理解

生成 20 个位置、16 维的位置编码，打印第 5 个位置的前 6 个数值，观察 sin/cos 规律。"""),
    code("""# 你的代码写在这里：
"""),
    md("""## 题 3：文本生成（挑战）

用本课第二课的 CharTransformer，训练你自己的文本（至少 200 字符），训练 500 步，生成 80 字符的新文本。"""),
    code("""# 你的代码写在这里：
"""),
    md("""全部做完并运行通过，第九阶段就过关了！"""),
]

answer = [
    md("""# 第九阶段综合练习参考答案"""),
    md("""## 题 1 参考答案"""),
    code("""import torch
import torch.nn.functional as F

Q = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
K = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
V = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

d = Q.shape[-1]
scores = Q @ K.T / (d ** 0.5)
weights = F.softmax(scores, dim=-1)
print("权重：")
print(weights)
print("每行和：", weights.sum(dim=-1))"""),
    md("""## 题 2 参考答案"""),
    code("""import torch

def position_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    pos = torch.arange(seq_len).unsqueeze(1).float()
    div = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
    pe[:, 0::2] = torch.sin(pos * div)
    pe[:, 1::2] = torch.cos(pos * div)
    return pe

pe = position_encoding(20, 16)
print(pe[5, :6])
print("奇数位是 cos，偶数位是 sin")"""),
    md("""## 题 3 参考答案

完整训练代码较长，直接参考 lesson_02 第 3-5 块，把 text 换成你自己的文本，step 改成 500 即可。关键点：字符表、训练循环、generate 三个部分缺一不可。"""),
    code("""# 提示：复制 lesson_02 的 CharTransformer 类和训练代码，
# 换成自己的文本即可。示例文本：
my_text = "the quick brown fox jumps over the lazy dog. machine learning is fun. practice makes perfect. "
# 然后用同样的流程：字符表 -> 序列 -> 训练 500 步 -> generate"""),
]

files = {
    "lesson_01_注意力机制.ipynb": lesson01,
    "lesson_02_小型Transformer实现.ipynb": lesson02,
    "practice_09.ipynb": practice,
    os.path.join("answers", "practice_09_answer.ipynb"): answer,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
