#! /usr/bin/python
# -*- coding:utf-8 -*-


import urllib2
import urllib
import re
from socket import error as SocketError
from cookielib import CookieJar
import time
import gzip, zlib
import json

import time


url = 'https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=1479958451947'
cj = CookieJar()
cookieHandle = urllib2.HTTPCookieProcessor(cj)

opener = urllib2.build_opener()
opener.addheaders = [('User_Agent',
                      'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36')]
postData = urllib.urlencode({
    '_json': 'true',
    'callback': 'https://account.xiaomi.com',
    'sid': 'passport',
    'qs': '%3Fsid%3Dpassport',
    '_sign': '2&V1_passport&wqS4omyjALxMm//3wLXcVcITjEc=',
    'serviceParam': '{"checkSafePhone":false}',
    'user': 'app_dev@hsfinance.cn',
    'hash': 'DF6F2BE3D9A1E3F563A6F56BC5D41B7A'
})
o = opener.open(url,postData, timeout=10)

# req = urllib2.Request(url,data,headers=)
# urllib2.urlopen(req)
d = o.read()
print d

# print o.info().getheaders('dict')
# print o.info().getheaders('Server')
cookie = o.info().getheaders('Set-Cookie')
a = ''
for i in cookie:
    a = a + i + ';'
print a

opener.addheaders.append(('Cookie',a))

u = 'https://dev.mi.com/sts?sign=NUzuBPDqs94TS1jFRue%2BFtqq%2BrA%3D&followup=https%3A%2F%2Fdev.mi.com%2Fhome&pwd=1&d=wb_f2a08e6c-b49b-4c71-8631-d43793dfbb9f&auth=XjomiZAUs%2Fm5JuLXWmmLN6Vb1mWK0iSgMrxUymkG9Lacx7gk7bWbyIL%2Fn1CYgemiTsVlwSIBscjCcEDthEvVx8jDfSYlNpbWdOFC6Yh45TEErZb6OJrM4thamEbM%2B9OVMnimIyqsxe505n0qdtvikGe79rs9ZSx3zFaoGq%2Fj%2BE4%3D&m=1&pass_eas=2.0&pass_uas=1.0&pass_ss=4.0&nonce=jVY9RZg8HE8BeGa0&_ssign=R25i96rbEKJsNkqloc6q3ROqYuY%3D'
u1 = opener.open(u, timeout=10)
print u1.read()
cookie1 = u1.info().getheaders('Set-Cookie')
b = ''
for i in cookie1:
    b = b + i + ';'
print b
opener.addheaders.append(('Cookie',b))

# url2 = 'https://account.xiaomi.com/pass/auth/security/home?userId=702242108'
url2 = 'https://dev.mi.com/home?userId=702242108'
u2 = opener.open(url2, timeout=10)
print u2.read()
cookie2 = u2.info().getheaders('Set-Cookie')
b = ''
for i in cookie2:
    b = b + i + ';'
print b

opener.addheaders.append(('Cookie',b))
opener.addheaders.append(('Host', 'dev.mi.com'))
u = 'https://dev.mi.com/datacenter/appview/2882303761517288980?userId=702242108'
r = opener.open(u, timeout=10)
print r.read()






