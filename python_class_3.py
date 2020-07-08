import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수 알아보기

class Warehouse:
    stock_num = 0 #재고량
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)

print(user1.__dict__)
print(user2.__dict__)

print(Warehouse.__dict__) #인스턴스의 네임스페이스를 먼저 확인하고, 없으면 클래스의 네임스페이스를 찾는다. 그래도 없으면 에러남

print(user1.stock_num)
print(user2.stock_num) #클래스 변수는 공유 됨을 알 수 있음.
