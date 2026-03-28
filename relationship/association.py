from typing import List

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Student(Human):
    # Student สืบทอดมาจาก Human เพื่อใช้ name และ age
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def take_course(self, course_name: str):
        print(f"{self.name} is learning {course_name}")

class Course:
    def __init__(self, name: str):
        self.name = name

    def get_knowledge(self):
        return self.name

class Professor(Human):
    # Association: Professor มีกลุ่มของ Student และ Course เพื่อทำงานร่วมกัน
    def __init__(self, name: str, age: int, students: List[Student], course: Course):
        super().__init__(name, age)
        self.students = students
        self.course = course

    def teach(self):
        print(f"Professor {self.name} is teaching {self.course.name}")
        for student in self.students:
            student.take_course(self.course.get_knowledge())

if __name__ == '__main__':
    # สร้างข้อมูลเบื้องต้น
    math_course = Course("Mathematics")
    s1 = Student("Alice", 20)
    s2 = Student("Bob", 21)
    
    # สร้างอาจารย์และให้รายชื่อนักเรียน พร้อมวิชาที่จะสอน
    prof = Professor("Dr. Smith", 45, [s1, s2], math_course)
    
    # เริ่มการสอน
    prof.teach()
