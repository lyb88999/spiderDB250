# -*- coding = UTF-8 #-*-
# @Time : 2021/12/13 2:28 下午
# @Author : 李宇博
# @File : spider.py
# @SoftWare : PyCharm
import requests
from bs4 import BeautifulSoup  # 网页解析
import re
import urllib.request, urllib.error
import xlwt  # excel操作
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    dataList = getData(baseurl)
    # print(dataList)
    savePath = "./豆瓣电影Top250.xls"
    # 3.保存数据
    saveData(dataList, savePath)
    # 4.dbPath
    dbpath = 'movie.db'
    # saveData2DB(dataList, dbpath)


# 影片详情规则
findLink = re.compile(r'<a href="(.*?)">')
# 图片
findImgSrc = re.compile(r'<img .* src="(.*?)"', re.S)  # re.S 忽视换行符
# 片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d+)人评价</span')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 2.解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item)
            data = []  # 保存一部电影所有信息
            item = str(item)
            # 影片详情的链接
            link = re.findall(findLink, item)[0]  # 通过正则表达式查找指定字符串
            data.append(link)
            # 图片的链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 片名
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                etitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(etitle)
            else:
                data.append(titles[0])
                data.append(" ")  # 外名为空
            # 分数
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 概述
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")
            # 影片相关内容
            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)  # 去掉br
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())
            dataList.append(data)
    return dataList


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("UTF-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(dataList, savePath):
    book = xlwt.Workbook(encoding="UTF-8")
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(8):
        sheet.write(0, i, col[i])
    for i in range(250):
        data = dataList[i]
        for j in range(8):
            sheet.write(i + 1, j, data[j])
    book.save(savePath)
    print("爬取完毕")


# 创建数据库
def init_db(dbpath):
    sql = "create table movie250" \
          "(id integer primary key autoincrement," \
          "info_link text," \
          "pic_link text," \
          "cname varchar," \
          "ename varchar," \
          "score numeric," \
          "rated numeric," \
          "introduction text," \
          "info text)"
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def saveData2DB(dataList, dbPath):
    init_db(dbPath)
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    for data in dataList:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = 'insert into movie250 (info_link,pic_link,cname,ename,score,rated,introduction,info)' \
              'values(%s)' % ",".join(data)
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # 调用函数
    # init_db(dbpath='movie.db')
    main()
    # askURL("https://movie.douban.com/top250?start=")
