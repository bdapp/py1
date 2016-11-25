#! /usr/bin/python
# -*- coding:utf-8 -*-

# 跑全盘主力机构数据

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import time
import gzip, zlib
import DB

import time


class STOCK_POSITION:
    def __init__(self):
        self.baseUrl1 = 'http://basic.10jqka.com.cn/'
        self.baseUrl2 = '/position.html'
        self.tool = tools.Tool()

    def getCode(self):
        try:
            sql = 'SELECT s_code FROM t_stock_list ;'
            online = self.db.selectDB(sql)

            for i in online:
                print i[0]
                self.getStockPosition(i[0])

        except Exception as e:
            print e



    def getStockPosition(self, CODE):
        try:
            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            url = self.baseUrl1 + str(CODE) + self.baseUrl2
            print url
            o = opener.open(url, timeout=10)
            d = o.read()

            # 解压zip
            gzipped = o.headers.get('Content-Encoding')
            if gzipped:
                d = zlib.decompress(d, 16 + zlib.MAX_WBITS)
                # print d
            d = unicode(d, "gbk").encode("utf-8")

            self.replaceName(CODE, d)

            self.insertInfo(CODE, d)

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


    # 修改名称
    def replaceName(self, CODE, str):
        try:
            pattern = re.compile('<title>(.*?)\(', re.S)
            r = re.search(pattern, str)
            if r == None:
                return
            n = r.group(1)
            print n
            print CODE.encode("utf-8")

            CODE = CODE.encode("utf-8")

            sql = "update `t_stock_list` set `s_name` = '" + n + "' where `s_code` = '" + CODE + "';"

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

    # 新增数据
    def insertInfo(self,CODE, str):
        try:
            pattern = re.compile('targ="organ_1".*?>(.*?)</a>.*?<tbody id="organInfo_1">(.*?)</tbody>', re.S)
            r = re.findall(pattern, str)
            if r == None:
                return

            pTime = ''
            body = ''

            for o in r:
                pTime = o[0]
                body = o[1]

            p = re.compile(
                '<span style="float:left;width:280px;">(.*?)</span.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',
                re.S)
            f = re.findall(p, body)
            for i in f:
                name = self.tool.replace(i[0])  # 机构或基金名称
                type = self.tool.replace(i[1])  # 机构类型
                have = self.tool.replace(i[2])  # 持有数量(万股)
                value = self.tool.replace(i[3])  # 持股市值(亿元)
                per = self.tool.replace(i[4])  # 占流通股比例(%)
                status = self.tool.replace(i[5])  # 增减情况(万股)

                CODE = CODE.encode('ascii','utf-8')
                sql = "insert into `t_position` (`tid`, `p_name`, `p_type`, `p_have`, `p_value`, `p_percent`, `p_status`, `p_time`, `t_stock_id`) values (uuid(), '" \
                      + name + "','" + type + "','" + have + "','" + value + "','" + per + "' ,'" + status + "' ,'" + pTime + "' ,'" + CODE + "');"
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
        self.db = DB.SQLDB()
        self.db.connectDB();

    def close(self):
        self.db.closeDB()




ls = STOCK_POSITION()
ls.connect()

start = time.time()

ls.getCode()
# ls.getStockPosition('600219')

ls.close()

end = time.time() - start
print '总共用时：' + str(end)

