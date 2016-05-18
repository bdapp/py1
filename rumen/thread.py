# -*- coding: utf-8 -*-
"""
http://www.mzitu.com/model/page/
"""

from multiprocessing import Pool
from time import sleep
import urllib
import time

# 下载图片
def downPic(path):
    try:
        list = path.split('/')
        urllib.urlretrieve(path, '/home/ubt/aa/' + list[len(list) - 1])
    except Exception:
        print '下载图片异常'

def f(x):
    print '%s --- %s ' % (33, x)
    downPic(x)


def main():
    pool = Pool(processes=8)    # set the processes max number 3
    for i in list:
        result = pool.apply_async(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'

list = [
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/a1_copy.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/android.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/dribbble.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/material_profile.jpg',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/Menu.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/Message.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/payments.jpg',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/presentation_dribble_001.png',
    'http://www.uisheji.com/wp-content/uploads/2016/05/16/profile.png'
]

if __name__ == "__main__":
    a = time.time()
    main()
    print time.time() - a