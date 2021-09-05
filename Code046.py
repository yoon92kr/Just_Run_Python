# 기본매개변수 중 필요값만 입력
# java에 비해 자유도를 갖는다.
def test(a, b=100, c=200):
    print(a+b+c)

test(10)
test(10, c=10, b=10)
test(10, c=10)