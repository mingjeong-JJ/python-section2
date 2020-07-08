from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os #window에 접근해서 os의 명령어를 실행할 수 있는 모듈

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "C:/imagedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath)) #절대경로 가져옴
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더가 이미 존재합니다.")
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(img_list,1):
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath,savePath+str(i) + '.jpg')
    req.urlretrieve(img_list['data-source'],fullFileName)
