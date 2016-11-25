#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import time
import gzip, zlib
import DB

import time


class STOCK_LIST:
    def __init__(self):
        self.baseUrl1 = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/'
        self.baseUrl2 = '/ajax/1/'
        self.tool = tools.Tool()


    def getStockList(self, pageNum):

        cj = CookieJar()
        cookieHandle = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookieHandle)

        url = self.baseUrl1 + str(pageNum) + self.baseUrl2
        print url
        o = opener.open(url, timeout=10)
        d = o.read()


        # 解压zip
        gzipped = o.headers.get('Content-Encoding')
        if gzipped:
            d = zlib.decompress(d, 16 + zlib.MAX_WBITS)
            # print d
        d = unicode(d, "gbk").encode("utf-8")
        pattern = re.compile('<tbody>(.*?)</tbody>', re.S)
        r = re.search(pattern, d)
        body = r.group(1)



        p = re.compile('<tr>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', re.S)
        f = re.findall(p, body)
        for i in f:
            i0 = self.tool.replace(i[0])    # 序号
            code = self.tool.replace(i[1])    # 代码
            name = self.tool.replace(i[2])    # 名称
            price = self.tool.replace(i[3])    #现价
            i4 = self.tool.replace(i[4])    #涨跌幅
            i5 = self.tool.replace(i[5])    #涨跌
            i6 = self.tool.replace(i[6])    #涨速(%)
            i7 = self.tool.replace(i[7])    #换手(%)
            i8 = self.tool.replace(i[8])    #量比
            i9 = self.tool.replace(i[9])    #振幅(%)
            deal = self.tool.replace(i[10])  #成交额
            flow = self.tool.replace(i[11])  #流通股
            i12 = self.tool.replace(i[12])  #流通市值
            i13 = self.tool.replace(i[13])  #市盈率

            sql = "insert into `t_stock_list` (`tid`, `s_code`, `s_name`, `s_price`, `s_deal`, `s_flow`, `s_time`) values (uuid(), '" + code + "','" + name + "','" + price + "','" + deal + "','" + flow + "' ,now());"
            print sql
            self.db.insertDB(sql)



    def connect(self):
        self.db = DB.SQLDB()
        self.db.connectDB();

    def close(self):
        self.db.closeDB()




ls = STOCK_LIST()
ls.connect()

start = time.time()

# 爬所有stock列表数据
for i in range(1, 138, 1):
    print '\n页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ' + str(i) + ' ~~~~~\n'

    ls.getStockList(i)

ls.close()

end = time.time() - start
print '总共用时：' + str(end)