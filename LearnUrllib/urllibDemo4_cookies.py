import urllib.request
import ssl
from http import cookiejar
ssl._create_default_https_context = ssl._create_unverified_context
filename = 'cookie.txt'
# MozillaCookieJar保存cookie
cookie = cookiejar.MozillaCookieJar(filename)
# HTTPCookieProcessor创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建自定义opener
opener = urllib.request.build_opener(handler)
# open方法打开网页
response = opener.open('https://movie.douban.com/')
cookie.save()