#문자열 범위 선택 연산자

print('"안녕하세요"[0:2] :', "안녕하세요"[0:2])
print('"안녕하세요"[1:3] :', "안녕하세요"[1:3])
print('"안녕하세요"[2:4] :', "안녕하세요"[2:4])
print()

#초기 포함 index, 혹은 최종 비포함 index 는 한쪽이 생략 가능하다.
#단, 생략시 처음부터 ~ 혹은 어디부터 끝까지의 의미를 갖는다.
print('"안녕하세요"[:3] : ', "안녕하세요"[:3])
print('"안녕하세요"[3:] : ', "안녕하세요"[3:])