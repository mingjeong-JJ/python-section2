import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#html이 필요, """으로 묶는건 줄바꿈이 포함된 문자열을 적을 수 있게 됨
html = """
<html>
<body>
<h1>파이썬 BeautifulSoup study</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
#print('soup', soup)
#print('prettify', soup.prettify()) #자동으로 들여쓰기 해줌

h1 = soup.html.body.h1 #순서대로 접근 가능
#print(h1) #아직 문자열만 가져온게 아님(class형태이다.)
#print(h1.string) #문자열만 가져올 수 있게 됨

p1 = soup.html.body.p #p가 두개 있는데, 첫번째 노드만 가져오게 됨
p2 = p1.next_sibling.next_sibling #줄바꿈이 되어 있어서 한 번 더 적어야 함(커서 이동 두번)
#next_sibling은 자주 쓰는 것이 아님 변경되는 경우가 많아서

print("h1 >> ", h1.string)
print("p1 >> ", p1.string)
print("p2 >> ", p2.string)

#직접접근한거! 
