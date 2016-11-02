# -*- coding:utf-8 -*-

# 测试代理
import urllib2
import urllib
import random
import time
import re
from socket import error as SocketError
from cookielib import CookieJar


try:

    proxy = urllib2.ProxyHandler({'http' : '101.200.169.110:80'})
    opener = urllib2.build_opener(proxy)
    opener.addheaders = [('User-Agent' ,'Opera/9.25 (Windows NT 5.1; U; en)')]
    r=opener.open('http://pv.sohu.com/cityjson?ie=utf-8', timeout=10)
    print r.read()

except urllib2.HTTPError, e:
    print 'HTTPError: ' + str(e.code)
except urllib2.URLError, e:
    print 'URLError: ' + str(e.reason)
except SocketError as e:
    print 'SocketError: ' + str(e.errno)