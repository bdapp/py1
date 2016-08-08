#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import ConnectMysql

import time


class LF_WANGWEN:

    def __init__(self):

        self.baseUrl = 'http://www.laifudao.com/wangwen/index_'
        self.baseUrl2 = '.htm'
        self.tool = tools.Tool()


    def wang(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'

            # proxy = urllib2.ProxyHandler({'http': '' + ip + ''})
            # opener = urllib2.build_opener(proxy)

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
                ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                ('Accept-Encoding', 'gzip, deflate, sdch'),
                ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
                ('Cache-Control', 'max-age=0'),
                ('Connection', 'keep-alive'),
                ('Host', 'www.laifudao.com')
            ]

            url = self.baseUrl + str(value) + self.baseUrl2
            print url
            o = opener.open(url, timeout=10)
            d = o.read()

            pattern = re.compile('<header class="post-header">(.*?)</a></h1>.*?title="(.*?)".*?<time>(.*?)</time>.*?<span class="cats">.*?>(.*?)</a>.*?"article-content">(.*?)</section>', re.S)
            results = re.findall(pattern, d)
            for i in results:
                title = self.tool.replace(i[0])
                author = self.tool.replace(i[1])
                time = self.tool.replace(i[2])
                type = self.tool.replace(i[3])
                content = self.tool.replace(i[4])


                # print title + "  " + author + "  " + time + "  " + type + "  " + content
                sql = "insert into `wangwen` (`pid`, `title`, `content`, `online`, `author`, `type`, `create_by`, `update_by`, `create_time`, `update_time`, `status`) values (uuid(), '"+title+"','"+content+"','"+time+"','"+author+"','"+type+"','admin','admin',now(),now(),0);"
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

for i in range(1710, 0, -1):
    print '页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + str(i)
    lf.wang(i)
lf.close()

end = time.time() - start
print '总共用时：' + str(end)


