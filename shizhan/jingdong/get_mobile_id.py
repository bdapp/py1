# -*- coding:utf-8 -*-
'''
获取手机品牌对应ID、名称

'''
import urllib2
import  os
import time
from socket import error as SocketError
import re


class GETID:

    def __init__(self):
        self.baseUrl='http://list.jd.com/list.html?cat=9987,653,655&page=1&ext=57050::1943^^&go=0&md=1&my=list_brand'

    # 开启网络请求
    def requestOpener(self):
        flag = 0
        while True:
            try:
                opener = urllib2.build_opener(urllib2.HTTPHandler())
                if flag != 0:
                    opener.addheaders = [('User_Agent',
                                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
                                         ('Referer','http://list.jd.com/list.html?cat=9987%2C653%2C655&go=0')]
                else:
                    opener.addheaders = [('User_Agent',
                                          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'),
                                         ('Referer', 'http://list.jd.com/list.html?cat=9987%2C653%2C655&go=0')]

                response = opener.open(self.baseUrl, timeout=20)
                return response.read()
            except urllib2.HTTPError, e:
                print e.code
                # return ''
            except urllib2.URLError, e:
                print e.reason
                # return ''
            except SocketError, e:
                print 'SocketError: ' + str(e.errno)
                # return ''
            flag += 1
            time.sleep(3)
            if flag == 3:
                return ''


    def start(self):
        mob_id = []
        content = self.requestOpener()
        p = re.compile('{"id":(.*?),.*?"name":"(.*?)"', re.S)
        s = re.findall(p, content)
        print len(s)
        for i in s:
            # print i[0] + ' deddddddddd ' + i[1]
            mob_id.append([i[0], i[1]])

        return mob_id


# get_id = GETID()
# get_id.start()