# python / mysql 연동
# pymysql pip install 할것

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')
# 데이터베이스 커넥션 객체 생성
cur = conn.cursor()
# 커서 객체 생성

cur.execute("create table if not exists userTable (id char(4), userName char(15), email char(20), birthYear int)")
# 쿼리문 실행

cur.execute("insert into usertable values('john', 'john bann', 'john@naver.com', 1990)")
cur.execute("insert into usertable values('yoon', 'sang hyun', 'yoon92@naver.com', 1992)")
cur.execute("insert into usertable values('ahn', 'youmi', 'yumi@naver.com', 1995)")
cur.execute("insert into usertable values('park', 'park su', 'park@gmail.com', 1980)")
conn.commit()
conn.close()