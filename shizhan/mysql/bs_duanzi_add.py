#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import ConnectMysql
import datetime
import time


class LF_WANGWEN:

    def __init__(self):

        self.baseUrl = 'http://m.budejie.com/text/'
        self.tool = tools.Tool()

        self.oldDatas = ''

    def queryLastData(self):
        try:

            sql = 'select online_time from bs_duanzi order by online_time desc limit 1;'
            online = self.db.selectDB(sql)

            self.oldDatas = online;

            return online

        except Exception as e:
            # print e
            return


    def wang(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'

            # proxy = urllib2.ProxyHandler({'http': '' + ip + ''})
            # opener = urllib2.build_opener(proxy)

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                # ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
                # ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                # ('Accept-Encoding', 'gzip, deflate, sdch'),
                # ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
                # ('Cache-Control', 'max-age=0'),
                # ('Connection', 'keep-alive'),
                # ('Host', 'm.budejie.com')
            ]

            url = self.baseUrl + str(value)
            print url
            o = opener.open(url, timeout=10)
            d = o.read()

            pattern = re.compile('<li class="ui-border-b">.*?<h4 class="ui-nowrap">(.*?)</h4>.*?<p class="ui-nowrap">(.*?)</p>.*?<section class="ui-row-flex">(.*?)</section>', re.S)
            results = re.findall(pattern, d)
            for i in results:
                author = self.tool.replace(i[0])
                onlineTime = self.tool.replace(i[1])
                content = self.tool.replace(i[2])

                # print author
                # print onlineTime
                # print content

                # 比较数据库最新一条数据,如果相同则跳出
                for old in self.oldDatas:
                    # 数据库查询出来的是unicode编码,要转成utf-8
                    o = datetime.datetime.strptime(onlineTime, '%Y-%m-%d %H:%M:%S')
                    if old[0] >= o :
                        # 通知中断
                        return

                sql = "insert into `bs_duanzi` (`tid`, `author`, `content`, `online_time`, `update_time`, `status`) values (uuid(), '"+author+"','"+content+"','"+onlineTime+"',now(),0);"
                print sql
                self.db.insertDB(sql)


        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False
        except Exception as e:
            print 'Exception' + str(e.message)
            return False


    def connect(self):
        self.db = ConnectMysql.SQLDB()
        self.db.connectDB();

    def close(self):
        self.db.closeDB()


lf = LF_WANGWEN()
lf.connect()
start = time.time()

# 先查出数据库最新一天的数据
lf.queryLastData()

for i in range(1, 3, 1):
    print '\n页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + str(i)
    lf.wang(i)
lf.close()

end = time.time() - start
print '总共用时：' + str(end)


