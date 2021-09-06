# suepr
class Person:
    def __init__(self, name, birth, id):
        self.name, self.birth, self.id = name, birth, id

    def __str__(self):
        return "이름 : {}, 생일 : {}, 아이디 : {}".format(self.name, self.birth, self.id)

    def __repr__(self):
        return "이름 : {}, 생일 : {}, 아이디 : {}".format(self.name, self.birth, self.id)

class Employee(Person):
    def __init__(self, name, birth, id, salary, carre_year):
        Person.__init__(self, name, birth, id)
        #super().__init__(name, birth, id)
        self.salary, self.carre_year = salary, carre_year

    def __str__(self):
        return super().__str__() + ", 연봉 : {}, 경력 연차 : {}".format(str(self.salary), str(self.carre_year))

    def __repr__(self):
        return super().__repr__() + ", 연봉 : {}, 경력 연차 : {}".format(str(self.salary), str(self.carre_year))

    
employee = Employee("윤상현", "11월 14일", "Yoon", 10000, 1)
print(str(employee))
