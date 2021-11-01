import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
# 데이터베이스 커넥션 객체 생성
cur = conn.cursor()
# 커서 객체 생성

# 쿼리문 실행

data1, data2, data3, data4 = "","","",""
sql = ""

while(True):
    data1 = input("사용자 ID : ")
    if data1 == "":
        break;
    data2 = input("사용자 이름 : ")
    data3 = input("사용자 이메일 : ")
    data4 = input("사용자 출생년도 : ")

    sql = "insert into usertable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)



conn.commit()
conn.close()