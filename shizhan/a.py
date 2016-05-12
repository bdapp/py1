# -*- coding:utf-8 -*-

# 抓取‘糗事百科’一页内容

import urllib
import urllib2
import re


page = 3
url = "http://www.qiushibaike.com/textnew/page/" + str(page) + "/"
useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
headers = {'User-Agent' : useragent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    
    content = response.read()
    patten = re.compile('<span class="c-bl touch-user-name">(.*?)</span>.*?<div class="mlr mt10 content-text">(.*?)</div>.*?data-votes=".*?">(.*?)</span>', re.S)
    items = re.findall(patten, content)
    strs = ''
    for x in items:
        strs += "auth:" + x[0] + "content:"  + x[1] + 'fine:' + x[2] + '\n----------\n'
        print "auth:" + x[0] + "content:"  + x[1] + 'fine:' + x[2] + '\n----------\n'
        
    with open('q.txt', 'w') as f:
        f.write(strs)    
        
except urllib2.HTTPError, e:
    print e.code    
    print e.reason