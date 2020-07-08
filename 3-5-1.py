import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UesrAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#wishket에서는 아이디 비밀번호 포함 토큰 값(csrfmiddlewaretoken) 값 (K7gmlFzLHwJi5M0PDma59zdM9yCoKROg - 랜덤임)도 같아야 로그인이 된다. - 개발자 도구로 확인 가능
#파이썬 코드를 사용하기 때문에 K7gmlFzLHwJi5M0PDma59zdM9yCoKROg 값을 가져와야함 (첫번째 목표)

#Request URL https://www.wishket.com/accounts/login/
URL = 'https://www.wishket.com/accounts/login/'
#Fake User-Agent 생성
ua = UserAgent()
print(ua.ie)
print(ua.chrome)
print(ua.random)
#ua [ 'google chrome' ]
# Mozilla / 5.0 (X11; CrOS i686 2268.111.0) AppleWebKit / 536.11 (Gecko와 같은 KHTML) Chrome / 20.0.1132.57 Safari / 536.11
with requests.Session() as s:
    #URL연결
    s.get(URL)
    #Login 정보 페이로드
    LOGIN_INFO = {
        'identification': 'audtjd3181@gmail.com',
        'password': 'a90301011*',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    #print('token',s.cookies['csrftoken'])

    #요청
    #response = s.post(URL, data=LOGIN_INFO)
    #HTML 결과 확인
    #print('response', response.text)
