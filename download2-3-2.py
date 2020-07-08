import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Get방식으로 어떤 url에 요청을해서 출력을 하는 것이 목표

API = "https://api.ipify.org"

values = {
    'format': 'jsonp'
}

print('before',values)
params = urlencode(values) #값에 맞게 변환 시켜줌
print('after',params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)

#매우 간단하게 날씨라던지 xml 등 뉴스, 블로그 소식을 주기적으로 받고 싶을 때 이렇게 받을 수 있음
#특별히 브라우저를 열지 않아도 됨
