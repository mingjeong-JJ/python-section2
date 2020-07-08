#과제를 위해 다시 듣는 중
#웹에서 원하는 이미지를 다운로드하는 코드
import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1290/1290162/9e450d9733cd77730b01_20200612093931526.jpg"
savePath = "C:/work/test2.jpg"

urllib.request.urlretrieve(imgUrl, savePath)

print("다운로드 완료")
