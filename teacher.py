class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1
    
    def __init__(self, name, number, studentType):
        super().__init__(name,number)
        self.studentType = studentType
        self.classes = []
        self.gpa = 0

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return f'이름 = {self.name} 학번 = {self.number} 수강과목 = {self.classes} 월급 = {self.gpa}'
    
class Teacher(Person):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.courses = []
        self.salary = 3000000

    def assignTeaching(self, course):
        self.courses.append(course)

    def __str__(self):
        return f'이름 = {self.name} 주민번호 = {self.number} 강의과목 = {self.courses} 월급 = {self.salary}'

hong = Student('홍길동', '12345678', Student.UNDERGRADUATE)
hong.enrollCourse('자료구조')
print(hong)

kim = Teacher('김철수', '123456790')
kim.assignTeaching('Python')
print(kim)
