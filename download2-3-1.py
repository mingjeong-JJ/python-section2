import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"
mem = req.urlopen(url)

#print(type(mem))

#print("geturl", mem.geturl())
#print("status", mem.status) #200 OK, 404 Not Found, 403 거절, 500 서버 문제
#print("headers", mem.getheaders())

#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50)) #가져올 양을 숫자로 지정함

print(urlparse("http://www.encar.com"))
