# 객체 활용 예시

# 인자값을 dictionary{} 형태로 변형 후 반환해주는 메소드
def creatStudent(name, korean, math, english, science):
    return {
        "name" :name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# dictionary를 매개변수로 받아, 필요한 key에 해당하는 값을 더해 반환하는 메소드
def student_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

# dictionary를 매개변수로 받아, student_sum 메소드를 호출 한 뒤, len값 만큼 나눈 뒤 반환하는 메소드
def student_avg(student):
    return student_sum(student) / (len(student)-1)


def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_sum(student), student_avg(student))


students = [
    creatStudent("윤인성", 87, 98, 88, 95),
    creatStudent("연하진", 92, 98, 96, 98),
    creatStudent("구지연", 76, 96, 94, 90),
    creatStudent("나선주", 98, 92, 96, 92),
    creatStudent("윤아린", 95, 98, 98, 98),
    creatStudent("윤명월", 64, 88, 92, 92),
    creatStudent("김미화", 82, 86, 98, 88),
    creatStudent("김연화", 88, 74, 78, 92),
    creatStudent("박아현", 97, 92, 88, 95),
    creatStudent("서준서", 45, 52, 72, 78)
   ]


print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))