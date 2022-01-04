# -*- coding = UTF-8 #-*-
# @Time : 2021/12/13 3:08 下午
# @Author : 李宇博
# @File : testurllib.py
# @SoftWare : PyCharm

import urllib.request, urllib.parse, urllib.error

# get请求
'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("UTF-8"))
'''
# post请求
'''
data = bytes(urllib.parse.urlencode({"message":"hello"}), encoding="UTF-8")
response = urllib.request.urlopen("https://www.httpbin.org/post", data=data)
print(response.read().decode("UTF-8"))
'''
# timeout
'''
try:
    response = urllib.request.urlopen("https://www.httpbin.org/get", timeout=1)
    print(response.read().decode("UTF-8"))
except urllib.error.URLError as e:
    print("time out!")
'''

# getheaders
'''
response = urllib.request.urlopen("https://www.httpbin.org/get")
print(response.status)
print(response.getheader("Date"))
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}
url = "https://movie.douban.com/top250?start="
req = urllib.request.Request(url=url, headers=headers, method="GET")
response = urllib.request.urlopen(req)
print(response.read().decode("UTF-8"))



