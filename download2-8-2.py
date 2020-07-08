from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("")
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

img_list = soup.select("a.course_card_front > dir.card-image > figure.is_thumbnail > img")

for i, img_list in enumerate(img_list,1):
    print(img_list['src'])
    #fullFileName = os.path.join(savePath,savePath+str(i) + '.png')
    #req.quote(e.select_one("figure.is_thumbnail > img")['src'][25:]
    #req.urlretrieve(img_list['data-source'],fullFileName)
