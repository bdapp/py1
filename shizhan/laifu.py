# coding: utf-8

# 来福网文

import urllib
import urllib2
import re

for a in range(4):

    url = "http://www.laifudao.com/wangwen/index_"+str(a)+".htm"

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')
    
    pattern = re.compile('<section class="article-content">\s(.*?)</section>', re.S)
    items = re.findall(pattern, content)
    
    for x in items:
        print x

