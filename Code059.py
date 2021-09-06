# __str__ 은 str클래스를 오버라이딩 하는것이다.
# 자바의 toString을 오버라이딩하는것과 동일하다
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

    def __str__(self):
       return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())
       #return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
       #return "%s\t%s\t%s"%(self.name, self.get_sum(), self.get_avg())
       

students = [Student("윤상현", 90, 80, 70, 60), Student("윤하현", 100, 10, 20, 30), Student("윤중현", 20, 60, 80, 70)]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))
