# 예외처리 _ try - except

list_input_a = ["30", "50", "스파이", "40", "120"]

list_number = []

for item in list_input_a:
    try:
        float(item)     #float 캐스팅이 되는지 확인만 하는것, 실제로 item에 대입을 한것이 아니다.
        list_number.append(item)
    except:
        pass

    
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))