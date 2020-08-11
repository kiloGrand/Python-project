from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return index()


@app.route('/movie')
def movie():
    datalist = []
    sql = "select * from movieTop250"
    con = sqlite3.connect("movie.db")   # 连接数据库
    cur = con.cursor()      # 生成游标
    data = cur.execute(sql)     # 执行sql语句
    for item in data:       # 拷贝数据到datalist中
        datalist.append(item)
    cur.close()     # 关闭游标
    con.close()     # 关闭数据库
    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score():
    num = []
    scores = []
    sql = "select score,count(score) from movieTop250 group by score"
    con = sqlite3.connect("movie.db")  # 连接数据库
    cur = con.cursor()  # 生成游标
    data = cur.execute(sql)  # 执行sql语句
    for item in data:  # 拷贝数据到datalist中
        scores.append(item[0])
        num.append(item[1])
    cur.close()  # 关闭游标
    con.close()  # 关闭数据库
    return render_template("score.html", scores=scores, num=num)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
