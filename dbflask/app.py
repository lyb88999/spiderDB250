from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/index")
def home():
    return index()


@app.route("/movie")
def movie():
    dataList = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        dataList.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=dataList)


@app.route("/score")
def score():
    score = []      # 评分
    num = []        # 每个评分电影数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score, count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score=score, num=num)


@app.route("/word")
def word():
    return render_template("word.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
