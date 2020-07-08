from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func",soup.select_one(selector).string)

car_func("#ge")
car_func("li#ge")
car_func("#cars #ge")
car_func("li[id='ge']")

print(soup.select("li")[3].string)
print(soup.findAll("li")[1].string)


#람다식
car_lambda = lambda q : print("car_lambda",soup.select_one(q).string)

car_lambda("#ge")
car_lambda("li#ge")
car_lambda("#cars #ge")
car_lambda("li[id='ge']")
