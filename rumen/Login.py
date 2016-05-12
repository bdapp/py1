# coding: utf-8
# post 请求

import urllib
import urllib2

values = {"username":"efew", "password":"efawef", "phonenumber":"1569852654"}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

headers = {"User-Agent":user_agent}
data = urllib.urlencode(values)
url = "http://note.budor.cn:88/aE?action=Login"


# 获取异常
try:
    request = urllib2.Request(url, data, headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
    
except urllib2.HTTPError, e:
    print e.code
    print e.reason

# get 请求

# values = {"username":"admin","password":"12345","phonenumber":"13800138000"}
# data = urllib.urlencode(values)
# url = "http://note.budor.cn:88/a?action=Login"
# geturl = url + "?" + data

# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()
