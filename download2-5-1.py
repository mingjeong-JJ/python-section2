from urllib.parse import urljoin

# urljoin = 절대경로는 묶어놓고 나머지 파일들 위치 지정이 가능함
baseUrl = "http://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.html")) #치환됨
print(">>", urljoin(baseUrl, "sub/b.html")) #html경로 아래에 치환
