# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

# 登录页面
loginUrl = 'http://4g.if.qidian.com/Atom.axd/Api/BookMark/GetTopList'

cookies = cookielib.CookieJar()
postData = urllib.urlencode({
    'bookId': '1003306811'
})

opener = urllib2.build_opener(urllib2.HTTPHandler())

opener.addheaders = [
    ('User-Agent','Mozilla QDReaderAndroid/6.2.1/233/qq/000000000000000')
]

request = urllib2.Request(
    url=loginUrl,
    data=postData
)

result = opener.open(request)
print result.read()
