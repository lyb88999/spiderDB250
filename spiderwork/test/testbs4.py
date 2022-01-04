# -*- coding = UTF-8 #-*-
# @Time : 2021/12/13 3:58 下午
# @Author : 李宇博
# @File : testbs4.py
# @SoftWare : PyCharm
import re

from bs4 import BeautifulSoup

'''
bs4 将复杂的HTML文档转换成一个复杂的树形对象，每个节点都是python对象
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

file = open("baidu.html", "rb")
html = file.read().decode("UTF-8")
bs = BeautifulSoup(html, "html.parser")

'''
# 1.Tag标签及其内容，拿到所找到的第一个内容
# print(bs.title)
# print(bs.a)
# print(bs.head)
print(type(bs.head))

# 2.NavigableString 不包含标签，只包括内容(字符串)
print(bs.title.string)

# 拿到一个标签里所有属性
print(bs.a.attrs)
# 3.Beautiful 表示整个文档
print(type(bs))

# 4.Comment 是一个特殊的NavigableString类型，不包含注释符号
print(type(bs.a.string))
print(bs.a.string)
'''
file.close()

'''
# 文档的遍历
print(bs.head.contents)    # 返回的是列表
'''
# 文档的搜索

# 1.find_all
'''
# 字符串过滤 查找与字符串完全匹配的内容
t_list = bs.find_all("a")
for i in range(len(t_list)):
    print(t_list[i])
'''

'''
# 正则表达式搜索：使用search()来匹配内容
t_list = bs.find_all(re.compile("a"))
for i in range(len(t_list)):
    print(t_list[i])
'''

'''
# 方法：传入一个函数，根据函数的要求来搜索 (了解)
def name_is_exists(tag):
    return tag.has_attr("name")


t_list = bs.find_all(name_is_exists)
for i in range(len(t_list)):
    print(t_list[i])
'''

# 2.kwargs 参数
'''
t_list = bs.find_all(id="head")
for i in range(len(t_list)):
    print(t_list[i])
t_list = bs.find_all(class_=True)
for i in range(len(t_list)):
    print(t_list[i])
t_list = bs.find_all(href="https://www.hao123.com")
for i in range(len(t_list)):
    print(t_list[i])
'''

# 3.text参数
'''
t_list = bs.find_all(text=re.compile("\d"))
for i in range(len(t_list)):
    print(t_list[i])
t_list = bs.find_all(text=["贴吧", "地图"])
for i in range(len(t_list)):
    print(t_list[i])
'''

# 4.limit参数
'''
t_list = bs.find_all("a", limit=5)
for i in range(len(t_list)):
    print(t_list[i])
'''


# css选择器
# t_list = bs.select('title')
# t_list = bs.select(".mnav")
# t_list = bs.select("#u1")
# t_list = bs.select("a[class='bri']")
# t_list = bs.select("div > div > div > div > a")
t_list = bs.select(".mnav ~ .bri")       # 兄弟节点
for i in range(len(t_list)):
    print(t_list[i])
