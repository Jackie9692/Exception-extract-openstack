# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import re 
import json

def login():
    auth_url = "http://www.v2ex.com/signin"
    home_url = "http://www.v2ex.com"
    # 登陆用户名和密码
    data={
      "u":"chendaxu_9692@163.com",
      "p":"1152762"
    }
    # urllib进行编码
    post_data=urllib.urlencode(data)
    # 发送头信息
     
    headers ={
              "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    # 初始化一个CookieJar来处理Cookie
     
    cookieJar=cookielib.CookieJar()
    # 实例化一个全局opener
     
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
     
    # 获取cookie
    req=urllib2.Request(auth_url,post_data,headers)
    result = opener.open(req)
    # 访问主页 自动带着cookie信息
    result = opener.open(home_url)
    # 显示结果
    print result.read()
    
def loginToupiao():
    cookieJar=cookielib.CookieJar()
    # 实例化一个全局opener
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    
    # 登陆用户名和密码
    data1={
      "loginUserId":"chendaxu_9692@163.com",
      "p":"1152762"
    }
    
    mem_mobile = "13517081199"
    password = "13517081199"
    
#     #进入访问---------------------------------------------
#     welcomeURL = "http://www.cn-healthcare.com/handler/service/pbcaseMedicalshow.xhtml?caseId=787"
#     data={
#       "caseId": "787"
#     }
#     post_data = urllib.urlencode(data)
#     headers ={
#               "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.3",
#               "content-type": "text/html;charset=UTF-8"
#     }
#     req=urllib2.Request(welcomeURL,post_data,headers)
#     result = opener.open(req)
    #initilize---------------------------------------------
    iniUrl = "http://www.cn-healthcare.com/handler/service/selectplMedicalshow.xhtml"
    data = None
    data = {
      "caseid": "787" + "",
      "jsoncallback": "jQuery18307974041672423482_1441430974642",
      "_": "1441430974871"
    }
    post_data = None
    post_data=urllib.urlencode(data)
    headers = None
    headers ={
              "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    } 
    req=urllib2.Request(iniUrl,post_data,headers)
    result = opener.open(req)
    print(result.read())
    
    
    # get real name----------------------------------------
    realName = ""
    jsonUrl = "http://www.cn-healthcare.com/handler/json/isExistBy_mobile.xhtml"

    data = None
    data={
      "jsoncallback":"jQuery18307974041672423482_1441430974642",
      "mem_mobile": mem_mobile + "",
      "_": "1441431777133"
    }
    post_data = None
    post_data=urllib.urlencode(data)
    headers = None
    headers ={
              "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
              "content-type": "application/json;charset=UTF-8"
    }
    
    # 获取cookie
    req=urllib2.Request(jsonUrl,post_data,headers)
    
    
    result = opener.open(req)
    
    jsonData = result.read()
    
    s = json.loads(jsonData)
    print(s)
    print(s["code"])
    print(s["mem_userid"])
    
#     print(result.read())
    
    
#     # 访问主页 自动带着cookie信息
#     result = opener.open(home_url)
#     # 显示结果
#     print result.read()  
    
      
# login()
loginToupiao()







    
         


