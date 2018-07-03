import urllib.request
from http import cookiejar
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

filename = 'cookie.txt'
# 创建MozillaCookieJar对象
cookie = cookiejar.MozillaCookieJar(filename)
# 创建cookie内容到变量
cookie.load(filename)
# HTTPCookieProcessor创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener
opener = urllib.request.build_opener(handler)
# opener打开网页
response = opener.open('https://movie.douban.com/')
# 输出结果
print(cookie)