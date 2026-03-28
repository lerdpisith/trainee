from typing import List

class Student:
    def __init__(self, name: str):
        self.name = name

    def remember(self, knowledge: str):
        print(f"Student {self.name} remembered: {knowledge}")

class Course:
    def __init__(self, name: str, knowledge: str):
        self.name = name
        self.__knowledge = knowledge

    def get_knowledge(self):
        return self.__knowledge

class Professor:
    def __init__(self, name: str, student: Student):
        self.name = name
        # --- 1. Association (ความเชื่อมโยง) ---
        # เก็บ Student ไว้เป็นฟิลด์ (field) ถาวร
        # Professor รู้จัก Student คนนี้ตลอดเวลา
        self.student = student

    def teach(self, course: Course):
        # --- 2. Dependency (ความพึ่งพา) ---
        # รับ Course เข้ามาเป็นพารามิเตอร์ของเมธอดเท่านั้น (ใช้งานชั่วคราว)
        # หากโครงสร้างคลาส Course เปลี่ยน (เช่น เปลี่ยนชื่อเมธอด get_knowledge) 
        # เมธอด teach นี้จะพังทันที
        print(f"\nProfessor {self.name} is teaching {course.name}")
        knowledge = course.get_knowledge()
        self.student.remember(knowledge)

if __name__ == '__main__':
    print("--- 📚 Association vs Dependency Example ---")
    
    # สร้างวัตถุ
    alice = Student("Alice")
    prof = Professor("Dr. Smith", alice) # Alice ถูกเชื่อมโยงกับ Professor (Association)
    
    math = Course("Mathematics", "Calculus and Algebra")
    physics = Course("Physics", "Quantum Mechanics")
    
    # การสอนแต่ละครั้งเป็นการสร้าง Dependency กับวิชานั้นๆ
    prof.teach(math)
    prof.teach(physics)
    
    print("\n✅ สรุป:")
    print("- Association: 'student' เป็นฟิลด์ถาวรใน Professor (รู้จักกันตลอด)")
    print("- Dependency: 'course' เป็นเพียงพารามิเตอร์ใน teach() (รู้จักกันชั่วคราว)")
