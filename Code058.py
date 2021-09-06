# isinstace 활용
# if, elif를 활용하여 list 내 참조값들이 해당 클래스인지를 확인할 수 있다.

class Student:
    def study(self):
        print("공부를 합니다.")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

