
#-*- coding: utf-8 -*-

import os
import urllib2
import urllib
import cookielib
import re
from PIL import Image

Img_URL='http://gs.uestc.edu.cn/wsxk/VerifyCodeGenServlet.do'
Login_URL='http://gs.uestc.edu.cn/wsxk/login.jsp'
Class_URL='http://gs.uestc.edu.cn/wsxk/jsp/T_PYGL_KWGL_WSXK_KXKC.jsp'
username='XXXX'
password='XXXX'
def login():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    #get img
    img_req=urllib2.Request(Img_URL)
    img_response=opener.open(img_req)
    try:
        out=open('code','wb')
        #print img_response.read()
        out.write(img_response.read())
        out.flush()
        out.close()
        print 'get code success'
        im = Image.open('code')
        im.show()

    except IOError:
        print 'file wrong'
    #input code
    img_code=raw_input("please input code: ")

    print 'your code is %s'%img_code
    #login
    LoginData = {
            'Login.Token1':username,
            'Login.Token2':password,
            'verifyCode':img_code,
            };
    login_req = urllib2.Request(Login_URL, urllib.urlencode(LoginData));
    login_req.add_header('User-Agent', "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36");
    login_response=opener.open(login_req)
    print 'login success'
    fout=open("tt.html","w")
    fout.write(login_response.read())
    fout.close()
    #load class info
    print 'load class'
    fout=open('t1.html','w')
    fout.write(opener.open(Class_URL).read())
    fout.close()
if __name__=='__main__':
    login()