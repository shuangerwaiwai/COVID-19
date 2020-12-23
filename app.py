# -*- coding = utf-8 -*-
# @Time : 2020/12/14 10:08
# @Author : 20108010
# @File : app.py
# @Software : PyCharm

from flask import Flask, render_template, request
import data_get
import data_wordcloud
import data_map

app = Flask(__name__)

data_dict = data_get.init()
data_get.china_total_data(data_dict)
data_get.global_total_data(data_dict)
data_get.china_daily_data(data_dict)
data_get.foreign_daily_data(data_dict)

data_wordcloud.china_wordcloud()
data_wordcloud.global_wordcloud()

data_map.all_map()

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
