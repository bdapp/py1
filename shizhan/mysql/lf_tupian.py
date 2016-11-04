#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import time
import ConnectMysql

import time


class LF_TUPIAN:

    def __init__(self):

        self.baseUrl = 'http://www.laifudao.com/tupian/index_'
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

            pattern = re.compile('<header class="post-header">(.*?)</a></h1>.*?title="(.*?)".*?<time>(.*?)</time>.*?<span class="cats">.*?>(.*?)</a>.*?"pic-content.*?src=(.*?)width', re.S)
            results = re.findall(pattern, d)
            for i in results:
                title = self.tool.replace(i[0])
                author = self.tool.replace(i[1])
                online = self.tool.replace(i[2])
                type = self.tool.replace(i[3])
                # print title
                # print author
                # print online
                # print type
                # print i[4]
                if i[4].find('data-gif=') == -1:
                    pic = self.tool.replace(i[4])
                    gif = ''
                else:
                    p = i[4].split('data-gif=')
                    pic = self.tool.replace(p[0])
                    gif = self.tool.replace(p[1])

                # print pic
                # print gif

                time.sleep(0.1)
                sql = "insert into `tupian` (`tid`, `title`, `online_time`, `pic`, `gif`, `author`, `type`, `create_by`, `update_by`, `create_time`, `update_time`, `status`) values (uuid(), '"+title+"','"+online+"','"+pic+"','"+gif+"','"+author+"','"+type+"','admin','admin',now(),now(),0);"
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


lf = LF_TUPIAN()
lf.connect()
start = time.time()

for i in range(3020, 0, -1):
    print '\n页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + str(i)
    lf.wang(i)
lf.close()

end = time.time() - start
print '总共用时：' + str(end)


