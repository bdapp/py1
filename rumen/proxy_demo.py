# -*- coding:utf-8 -*-

import urllib2

# proxy代理模拟
'''
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http':'http://45.32.36.215:80'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

print opener.open('http://www.baidu.com').read()

'''


for i in range(5, 10):
    if i==5:
        print 'aaa'
    print i