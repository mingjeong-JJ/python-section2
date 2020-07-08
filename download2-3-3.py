import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Get방식으로 어떤 url에 요청을해서 출력을 하는 것이 목표
#행정안전부 홈페이지의 알립니다(뉴스 소식) 정보 가져오기

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?"

values = {
    'ctxCd': '1012'
}

print('before',values)
params = urlencode(values) #값에 맞게 변환 시켜줌
print('after',params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
