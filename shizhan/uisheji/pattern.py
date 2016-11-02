# -*- coding:utf-8 -*-

import re

ss ='<div class="wp-page-nav">页面: 1 <a href="http://www.uisheji.com/247007.html/2">2</a> <a href="http://www.uisheji.com/247007.html/3">33ee</a></div>'

pat = re.compile('</a> <a href=.*?>(\d+).*?</a></div>', re.S)
res = re.search(pat, ss)
print res.group(1)
