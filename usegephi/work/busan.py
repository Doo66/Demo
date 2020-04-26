import os,sys
import jieba, codecs, math
import jieba.posseg as pseg
import wordcloud

names = {}              # 姓名字典
relationships = {}      # 关系字典
lineNames = []          # 每段内人物关系

# 对剧本进行分行读取
# 对每一行进行分词并判断词性是否为人名
# 提取该行出现的人物集，存入 lineName 中
# 更新人物在 names 中出现的次数
jieba.load_userdict("dict.txt") # 加载字典
with codecs.open("busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line) # 分词并返回该词词性
        lineNames.append([])  # 为新读入的一段添加人物名称列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue # 当分词长度小于2或该词语词性不为nr时,认为该词不为人名
            lineNames[-1].append(w.word) # 为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1 # 该人物出现次数加1

# 打印生成的 names 集合 ，观察人物出现的次数
# for name, times in names.items():
#     print(name, times)

# 将 lineNames 中每一行出现的人物进行两两相连
# 两个人物尚未连接，则将新建的边权值设为1
# 已连接，将权值加1
for line in lineNames: # 对于每一段
    for name1 in line:
        for name2 in line:  # 每一段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None: # 若两人未同时出现，则新建一项
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1   # 两人共同出现次数 +1

# 将建好的 names 和 relationships 输出到文本
# 方便使用 gephi 进行可视化处理
# 尽可能过滤掉冗余边
# 输出节点集合保存为 busan_node.txt，边集合保存为 busan_edge.txt

# 保存节点集合
with codecs.open("busan_node.txt", "w", "utf8") as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")
# 保存边集合
with codecs.open("busan_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")
# 数据可视化分析
# 词云
# wf = open("busan_node.txt", "r")
# wt = wf.read()
# wf.close()

# 分词
# ls = jieba.lcut(wt)
# txt = " ".join(ls)

# 生成词云
# w = wordcloud.WordCloud(font_path = "msyh.ttc", width = 1000, height = 700, \
#        background_color = "white")
# w.generate(txt)
# 生成词云图片
# w.to_file("fushanxing.png")

print("end")
















