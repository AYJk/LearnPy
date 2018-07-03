#   导入urllib
import urllib.request
import ssl
#   全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context
#   打开url
response = urllib.request.urlopen('https://movie.douban.com/', None, 2)
#   读取返回的内容
html = response.read().decode('utf-8')
#   写入txt
f = open('code1.txt', 'w', encoding='utf-8')
f.write(html)
f.close()
