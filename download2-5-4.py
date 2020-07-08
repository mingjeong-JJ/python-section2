#css 선택자(selecter)을 활용해서 조건에 맞는 거 가져오기 / 가장 많이 쓰인다 /
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("div#main > h1")
print('h1', h1.string) #얘 타입은 list임(string 속성에 접근 불가), for문 접근해야함,  1개일 경우 select_one 쓰는게 낫다

list_li = soup.select("div#main > ul.lecs > li")  # id는 #, class는 . 으로 구분함! (검색했음)
for li in list_li:
    print(li.string)
