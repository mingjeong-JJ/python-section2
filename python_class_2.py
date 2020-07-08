import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest():
    def function1():
        print("function1 called")

    def function2(self):
        print(id(self))
        print("function2 called")

f = SelfTest() #인스턴스를 생성해서 인스턴스 자기자신을 self의 매개변수로 넘겨서 호출하는 방법
print(dir(f))
f.function2()

print(SelfTest.function1()) #클래스의 이름.함수의 이름 //으로 호출하는 방법
