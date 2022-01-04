# -*- coding = UTF-8 #-*-
# @Time : 2022/1/4 4:04 下午
# @Author : 李宇博
# @File : test_wc.py
# @SoftWare : PyCharm


import jieba                             # 分词
from matplotlib import pyplot as plt     # 绘图
from wordcloud import WordCloud          # 词云
from PIL import Image                    # 图片处理
import numpy as np                       # 矩阵运算
import sqlite3                           # 数据库操作


con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = "select introduction from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text += item[0]
# print(text)
cur.close()
con.close()
cut = jieba.cut(text)
string = " ".join(cut)
print(len(string))
# print(string)


img = Image.open("tree.jpeg")       # 打开masked图片
img_array = np.array(img)           # 将图片转化为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="/System/Library/Fonts/PingFang.ttc",
    stopwords=["的", '电影']
).generate_from_text(string)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")
# plt.show()
plt.savefig("./word.jpg", dpi=600)


