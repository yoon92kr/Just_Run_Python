# 가변 매개변수 함수
# 가변매개변수는 한번만 선언 가능하다
def printRepeat(count, *voice):
    for c in range(count):
        for v in voice:
            print(v)
        print()




printRepeat(5, "hello", "python", "and", "java")
