#coding:utf-8

# 爬百度首页源码 
import urllib
import urllib2

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()


