# -*- coding:utf-8 -*-

import urllib2

# opener方式请求sina img

url = 'http://ww3.sinaimg.cn/large/e4e2bea6jw1f3q38klc8ng207c04jb29.gif'

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0')]
resp = opener.open(url)
result = resp.read()

with open('/home/ubt/a.gif', 'wb') as f:
    f.write(result)


