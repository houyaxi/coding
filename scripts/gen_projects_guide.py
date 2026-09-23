# -*- coding: utf-8 -*-
"""生成综合小项目的项目指南 notebook。"""
import os
import nbformat as nbf

BASE = r"C:\Users\26643\Desktop\古法编程\projects_综合小项目"
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


guide = [
    md("""# 综合小项目指南

前面 10 个阶段学完了，这里是检验成果的地方。选择一个项目独立完成，跑通整个流程：
数据 → 处理 → 建模（可选）→ 结果展示 → 写总结。

建议按难度顺序选：先做 1-2 个简单的建立信心，再做需要模型的。"""),
    md("""## 项目 1：成绩数据分析报告（简单）

用 stage_05 的 students.csv：
- 读取并用 Pandas 清洗缺失值
- 统计每个班的各科平均分
- 用 matplotlib 画出各班成绩对比柱状图和分布直方图
- 输出一段文字结论（哪个班数学最好、全班最弱的科目是什么）

涉及：Pandas、matplotlib、逻辑分析。"""),
    md("""## 项目 2：随机数统计实验（简单）

- 生成 10000 个 0-1 均匀随机数
- 分成 20 组求每组平均（提示：reshape(500, 20).mean(axis=1)）
- 画直方图，观察"平均值的分布"比"单个数的分布"更接近钟形
- 用文字解释你观察到的现象（这是中心极限定理的直观体验）

涉及：NumPy、matplotlib。"""),
    md("""## 项目 3：手写数字识别（中等）

用 stage_08 的知识：
- 用 sklearn digits 数据集
- 训练一个 MLP（隐层可以调）
- 画出训练过程中的损失下降曲线
- 随机挑 8 张测试图，预测并展示"图 + 预测 + 真实"的对比
- 用文字总结：准确率多少、哪些数字容易认错

涉及：PyTorch、matplotlib、模型评估。"""),
    md("""## 项目 4：字符级文本生成器（中等偏难）

用 stage_09 的 CharTransformer：
- 准备一段你自己的文本（比如你喜欢的歌词/诗，300 字以上）
- 训练模型
- 生成 100 字符的新文本
- 把生成结果画成"训练损失下降"曲线
- 用文字评价：模型学到了什么规律，哪些地方还不对

涉及：Transformer、PyTorch、matplotlib。"""),
    md("""## 项目 5：大模型应用小工具（中等）

用 stage_10 的知识：
- 选一个任务（情感分析、摘要、翻译任选）
- 写一个函数：输入文本，返回结果
- 准备 5 条测试文本，批量跑并整理成表格
- 用文字评价模型的优缺点

涉及：transformers、数据处理。"""),
    md("""## 项目完成清单（每个项目对照检查）

- 数据来源明确，读取正常
- 关键中间结果有 print 或图表展示
- 有至少一张 matplotlib 图（除非项目 5）
- 代码按逻辑分块，有注释
- 最后有一个 markdown 块写你的结论和心得

做完任何一个项目，都可以发给我，我帮你检查代码并给出改进建议。"""),
]

files = {
    "项目指南.ipynb": guide,
}
for name, cells in files.items():
    path = os.path.join(BASE, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        nbf.write(make_nb(cells), f)
    print(f"已生成：{path}")
