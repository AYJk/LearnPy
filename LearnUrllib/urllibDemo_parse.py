import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://movie.douban.com'
data = {
    'value': 'true'
}
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data=data)
html = response.read().decode('utf-8')
f = open('code4.txt', 'w', encoding='utf-8')
f.write(html)
f.close()

url = '%2523%25E7%25BC%2596%25E7%25A8%258B%2523'
first = urllib.parse.unquote(url)
print(first)
second = urllib.parse.unquote(first)
print(second)
