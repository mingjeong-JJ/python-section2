import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://siape.veta.naver.com/fxclick"

values = {
    'eu': 'EU10041892'
}

print('before',values)
params = urlencode(values) #값에 맞게 변환 시켜줌
print('after',params)

url = API + "?" + params
print("요청 url", url)

print(url)

reqData = req.urlopen(url).read()

savePath = "C:/work/homework1.jpg"

with open(savePath,'wb') as saveFile:
    saveFile.write(reqData)
