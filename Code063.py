# 클래스 상속
# 상속 선언 형식
# class 클래스명(상속받을 클래스명)

# 부모클래스 생성자 호출 선언 형식
# 부모클래스명.__init__(self)

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__메서드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test 메서드가 호출되었습니다.")

class Child(Parent):
    def __init__(self):
        #Parent.__init__(self)
        super().__init__()
        print("Child 클래스의 __init__ 메서드가 호출되었습니다.")

  
child = Child()
print()

child.test()
print()

print(child.value)  