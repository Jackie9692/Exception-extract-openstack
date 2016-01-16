# -*- coding:utf-8 -*-

import urllib                                                     #导入urllib模块  
import urllib2                                                    #导入urllib2模块  
import re                                                         #导入正则表达式模块：re模块  
import gzip
import json
import re
#from http.client import HTTPConnection
#import httputils as utils
 

def getCookiesFromHeaders(headers):
    '''从http响应中获取所有cookie'''
    cookies = list()
    for header in headers:
        if "Set-Cookie" in header:
            cookie = header[1].split(";")[0]
            cookies.append(cookie)
    return cookies
         
def saveCookies(headers, cookies):
    '''保存cookies'''
    for cookie in cookies:
        headers["Cookie"] += cookie + ";"
 
def getCookieValue(cookies, cookieName):
    '''从cookies中获取指定cookie的值'''
    for cookie in cookies:
        if cookieName in cookie:
            index = cookie.index("=") + 1
            value = cookie[index:]
            return value
         
def parseQueryString(queryString):
    '''解析查询串'''
    result = dict()
    strs = queryString.split("&")
    for s in strs:
        name = s.split("=")[0]
        value = s.split("=")[1]
        result[name] = value
    return result

# 请求头
headers = dict()
headers["Connection"] = "keep-alive"
headers["Cache-Control"] = "no-cache"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en;q=0.6"
headers["Cookie"] = ""
tieBaName=787
# cookie
cookies = list()
 
# 个人信息
userInfo = {}
 
def login(account, password):
    '''登录'''
    global cookies
    headers["Host"] = "cas.cn-healthcare.com"
    body = "username=qianl19840216%40ask.com&password=13517081199&isajax=true&isframe=true&callback=feedBackUrlCallBack&lt=LT-5540388-NMkz2tFNKTe757gfHHAXPeRpYQloth&execution=e1s1&_eventId=submit&localurl=&J_Username_t=13517081199&_eventId=submit"
    body = body.format(account, password)
    conn = HTTPConnection("cas.cn-healthcare.com", 80)
    conn.request("POST", "/login", body, headers)
    resp = conn.getresponse()
    print(resp.getheaders())
    cookies += getCookiesFromHeaders(resp.getheaders())
    saveCookies(headers, cookies)

    
    
    # 登录成功会返回302
    return True if resp.code == 302 else False
         
def signIn(tieBaName):
    '''签到''' 
    # 签到
    conn2 = HTTPConnection("cas.cn-healthcare.com", 80)
    body = urllib.parse.urlencode({"caseId":tieBaName, "memCard":memCard})
    conn2.request("POST", "/handler/service/voteMedicalshow.xhtml" , body , headers)
    resp2 = conn2.getresponse()
    data = json.loads((gzip.decompress(resp2.read())).decode())
    return data
    
 
if __name__ == "__main__":
    account = input("请输入帐号:")
    password = input("请输入密码:") 
    
    ok = login(account, password)
    
    if ok:
        conn1 = HTTPConnection("cas.cn-healthcare.com", 80)
        conn1.request("GET", "/handler/sso/action.jsp?ticket=ST-2735393-Ztzz72d0AXST1dsnige4-sso_server", "", headers)
        resp1 = conn1.getresponse()
        print(resp1.getheaders())
        cookies += getCookiesFromHeaders(resp1.getheaders())
        print (cookies)
        signInfo = signIn(tb)
    else:
        print("登录失败")
