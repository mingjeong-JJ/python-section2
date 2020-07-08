import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20120616_247%2Fcronis1223_1339853552637yJrqx_JPEG%2F%25B5%25BF%25B9%25B0%25B9%25E8%25B0%25E6%252811%2529.jpg&type=b400"
htmlUrl = "http://google.com"

savePath1 = "c:/work/test1.jpg"
savePath2 = "c:/work/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")
