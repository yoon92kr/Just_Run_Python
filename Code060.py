# 비교연산자 오버라이딩
# 객체를 비교하고자 할때, 비교연산자 기준을 재정의 할 수 있다

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

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
        
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

student_a = Student("윤상현", 87, 98, 88, 95)
student_b = Student("윤하현", 92, 98, 96, 98)

print("student_a == student_b : ",student_a == student_b)
print("student_a != student_b : ",student_a != student_b)
print("student_a > student_b : ",student_a > student_b)
print("student_a >= student_b : ",student_a >= student_b)
print("student_a < student_b : ",student_a < student_b)
print("student_a <= student_b : ",student_a <= student_b)
