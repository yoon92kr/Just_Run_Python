#OS 모듈
import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소 : ",os.listdir())

os.mkdir("hello")   #폴더 생성
os.rmdir("hello")  #폴더 제거

with open("original.txt", "w") as file: #파일 생성 및 출력(w) 모드 선언
    file.write("hello")
os.rename("original.txt","new.txt")    # 파일 이름 변경 

os.remove("new.txt")    # 파일 삭제
os.unlink("new.txt")

os.system("dir")    #내부 요소 확인