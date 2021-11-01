import matplotlib.pyplot as plt
# 그래프 생성/이미지화 모듈


x = [1,4,9,16,25,36,49,64]
y = [i for i in range(1, 9)]

plt.plot(x, y, 'r')
# 문자열은 색상/반환타입의 속성이다

plt.title('matplotlib sample')
plt.xlabel('x value')
plt.ylabel('y value')
plt.show()