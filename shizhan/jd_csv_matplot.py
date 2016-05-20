# -*- coding:utf-8 -*-

import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import json
import webbrowser


def get_csv():
    ll = []
    with open('/home/ubt/mo.csv', 'rb') as f:
        rows = csv.reader(f, delimiter=',', quotechar='|')
        for r in rows:
            if r[len(r)-1]!='评价':
                ll.append((r[1], int(r[len(r)-1])))

    print   len(ll)

    # 反向排序
    #ll.sort(reverse=True)
    # 按第二个关键字排序
    ll.sort(lambda x,y:cmp(x[1],y[1]))
    ll.reverse()
    #ll.sort()
    print ll
    return ll

def getColors(value):
    # 获取随机颜色值
    colors = []
    for v in value:
        c = '#'
        for i in random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f'], 6):
            c = c + str(i)
        colors.append(c)

    return colors


def show_plot():
    l = get_csv()
    f = len(l)-1
    value = []
    pro = []
    for r in range(0, 20):
        print l[r]
        value.append(l[r][1])
        pro.append(l[r][0])

    # 写入json
    data = {}
    data["categories"] = pro
    data["data"] = value
    j = json.dumps(data)
    print j

    with open('../html/data.js', 'wb') as f:
        co = 'var c=' + j
        f.write(co)

    # 写入图片
    pos = np.arange(len(value))
    plt.bar(pos, value, color=getColors(value), alpha=1)
    plt.show()

    # 打开网页
    webbrowser.open('../html/py.html')



show_plot()