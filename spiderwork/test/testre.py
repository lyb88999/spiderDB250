# -*- coding = UTF-8 #-*-
# @Time : 2021/12/14 12:19 上午
# @Author : 李宇博
# @File : testre.py
# @SoftWare : PyCharm

import re

'''
# 正则表达式：字符串模式
# 有模式对象
pattern = re.compile("AA")
print(pattern.search("BBBBAAAS"))

# 无模式对象
# 前为规则，后为校验对象
m = re.search("asd", "Aasd")
print(m)
'''
m = re.findall("[a-z]+", "ASDakjanmB")
print(m)

# sub
print(re.sub("a", "A", "abcdcafd"))  # 第一个是被替换的，第二个是替换后的，第三个是对象

# 建议在正则表达式中，被比较的字符串前面加上r,不用担心转义字符的问题
