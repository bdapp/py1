# coding:utf-8

# Cookie模拟登录
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'

# 获取cookie到文件
#cookie = cookielib.MozillaCookieJar(filename)
#handler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handler)
#response = opener.open("http://note.budor.cn:88/login.jsp")
#cookie.save(filename, ignore_discard=True, ignore_expires=True)

# 读取cookie从文件
cookie = cookielib.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://note.budor.cn:88/index.jsp")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
rsp = opener.open(req)
print rsp.read()