#! /usr/bin/python
http://m.budejie.com/text/8174

http://m.budejie.com/pic/11854
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

        self.baseUrl = 'http://www.laifudao.com/wangwen/index_'
        self.baseUrl2 = '.htm'
        self.tool = tools.Tool()

        self.oldDatas = ''
        # 是否中断更新
        self.isClose = False


    def queryYesterday(self):
        try:

            sql = 'select `title` from `lf_wangwen` where `online_time` = (select `online_time` from `lf_wangwen` order by `create_time` desc limit 1);'
            names = self.db.selectDB(sql)

            self.oldDatas = names;

            return names

        except Exception as e:

            return

    def wang(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'

            # 中断打开链接
            if self.isClose:
                return

            # proxy = urllib2.ProxyHandler({'http': '' + ip + ''})
            # opener = urllib2.build_opener(proxy)

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
            #     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
            #     ('Accept-Encoding', 'gzip, deflate, sdch'),
            #     ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
            #     ('Cache-Control', 'max-age=0'),
            #     ('Connection', 'keep-alive'),
            #     ('DNT', '1'),
            #     ('Upgrade-Insecure-Requests', '1'),
            #     ('Host', 'www.laifudao.com'),
            #     ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')
            ]

            url = self.baseUrl + str(value) + self.baseUrl2
            print url
            o = opener.open(url, timeout=10)
            d = o.read()

            pattern = re.compile('<header class="post-header">(.*?)</a></h1>.*?title="(.*?)".*?<time>(.*?)</time>.*?<span class="cats">.*?>(.*?)</a>.*?"article-content">(.*?)</section>', re.S)
            results = re.findall(pattern, d)
            for i in results:

                # 中断打开链接
                if self.isClose:
                    return

                title = self.tool.replace(i[0])
                author = self.tool.replace(i[1])
                online = self.tool.replace(i[2])
                type = self.tool.replace(i[3])
                content = self.tool.replace(i[4])


                # 比较数据库最新一条数据,如果相同则跳出
                for old in self.oldDatas:
                    # 数据库查询出来的是unicode编码,要转成utf-8
                    o =old[0].encode('utf-8')
                    if title == o:
                        # 通知中断
                        self.isClose = True
                        return

                # 插入新数据
                time.sleep(0.1)
                sql = "insert into `lf_wangwen` (`pid`, `title`, `content`, `online_time`, `author`, `type`, `create_by`, `update_by`, `create_time`, `update_time`, `status`) values (uuid(), '"+title+"','"+content+"','"+online+"','"+author+"','"+type+"','admin','admin',now(),now(),0);"
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

# 先查出数据库最新一天的数据
lf.queryYesterday()


# 爬网站前两页数据
for i in range(1, 3, 1):
    print '\n页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + str(i)
    lf.wang(i)


lf.close()

end = time.time() - start
print '总共用时：' + str(end)


