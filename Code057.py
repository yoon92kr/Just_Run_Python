# isinstance 메소드
# 객체가 클래스자료형인지 여부를 boolean 자료형으로 반환해준다 
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_avg(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())


student = Student("윤상현", 90, 80, 70, 60)

print("isinstance(student, Student : ",isinstance(student, Student))
print(student.to_string())