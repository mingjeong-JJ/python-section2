import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""
#href 속성의 url 주소를 연속으로 가져와서 출력해보는 예제
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a") #a 태그를 한번에 담음
#print('links', type(links)) #ResultSet 확인 가능

a = soup.find_all("a",string="daum")
print('a',a) #string이 daum이 인것만 가져오게 할 수도 있음.

b = soup.find_all("a", limit=3) #갯수 제한 걸 수도 있음
print('b',b)

c = soup.find_all(string=["naver","google"])
print('c',c)

for a in links:
    #노드가 여러개이기 때문에 반복문으로 돌면서 접근해야함.
    #print('a',type(a),a)
    href = a.attrs['href']      #a의 속성(attrs)
    txt = a.string
    print('txt >> ', txt,'href >> ',href)

#태그선택자를 활용해서 가져오는 스타일
