import csv, re

def opencsv(fileName):
    f = open(fileName, 'r')
    reader = csv.reader(f)
    # 파일을 읽어줄 reader 객체 생성
    output= []
    # 읽은 데이터를 보관할 배열객체 생성
    for i in reader:
        output.append(i)
    return output
    

def writecsv(fileName, the_list):
    with open(fileName, 'w', newline='') as f:
        # 파이썬에서 스트림을 열어줄때 필히 닫아주어야 하는데, with open as 구문을 사용하면 자동으로 close를 진행해준다.
        a=csv.writer(f, delimiter=',')
        # 파일을 쓸[W] 위치에 writer 객체를 생성
        a.writerows(the_list)
        # 실제 write 해주는 코드


def switch(listName):
    # 읽어들인 데이터를 수정(재배치) 하는 메소드
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
                # j의 ','를 ''로 replace
            except:
                pass
    return listName

