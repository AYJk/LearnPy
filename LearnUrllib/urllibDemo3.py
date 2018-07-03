import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com/'
# 设置代理ip
proxy_handler = urllib.request.ProxyHandler({
    'http': '218.56.132.157:8080',
    'https': '14.155.113.38:9000'
})
# 必须使用build_opener()函数来创建带有代理ip功能的opener对象
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url)
html = response.read().decode('utf-8')
f = open('code3.txt', 'w', encoding='utf-8')
f.write(html)
f.close()
