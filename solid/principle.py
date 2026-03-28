from relationship.association import Course
from typing import List
from abc import ABC, abstractmethod


# Open/Closed Principle (OCP): Customer เป็น Abstract Base Class (Interface)
# ทำให้เราสามารถขยาย (Open for extension) ไปเป็น Student หรือ V2Student ได้
# โดยไม่ต้องแก้ไขโค้ดส่วนอื่น
class Customer(ABC):
    def __init__(self):
        # กำหนด List สำหรับเก็บข้อมูลรายวิชา (instance attribute)
        self.courses: List[Course] = []

    @abstractmethod
    def register_course(self, course: Course):
        pass

    @abstractmethod
    def cancel_course(self, course: Course):
        pass

# Single Responsibility Principle (SRP): คลาสนี้ดูแลเฉพาะข้อมูลบุคคลพื้นฐาน
class Human:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

# Liskov Substitution Principle (LSP): Student สามารถไปใช้แทน Customer ได้เสมอ
class Student(Customer):
    def register_course(self, course: Course):
        self.courses.append(course)
        print(f"Student enrolled in: {course.name}")

    def cancel_course(self, course: Course):
        self.courses.remove(course)

# V2Student ก็สามารถใช้แทน Customer ได้เช่นกัน ตามหลัก LSP
class V2Student(Customer):
    def __init__(self):
        super().__init__()
        self.degrees: List[str] = []
        self.papers: List[str] = []

    def register_course(self, course: Course):
        self.courses.append(course)
        print(f"V2Student enrolled in: {course.name}")

    def cancel_course(self, course: Course):
        self.courses.remove(course)

# Dependency Inversion Principle (DIP): RegisterManager รับ Customer (Abstraction)
# ไม่ได้ยึดติดกับคลาส Student หรือ V2Student โดยตรง
class RegisterManager:
    def __init__(self, customer: Customer):
        # รับ Abstraction (Interface) แทนที่จะรับ Concrete Class
        self.customer = customer

    def register_course(self, course: Course):
        # การทำงานจะขึ้นอยู่กับว่า customer ที่ส่งเข้ามาเป็นใคร (Polymorphism)
        self.customer.register_course(course)

def apply_registration(manager: RegisterManager):
    # ฟังก์ชันนี้ใช้ RegisterManager ในการลงทะเบียนวิชาต่างๆ
    manager.register_course(Course("Math"))
    manager.register_course(Course("Physics"))

if __name__ == '__main__':
    # สร้าง Instance ของนักเรียนประเภทต่างๆ
    student1 = Student()
    student2 = V2Student()
    
    # ใช้ RegisterManager จัดการ (แสดงให้เห็น DIP และ LSP)
    manager_basic = RegisterManager(student1)
    manager_advanced = RegisterManager(student2)
    
    print("--- Basic Student Registration ---")
    apply_registration(manager_basic)
    
    print("\n--- Advanced Student Registration ---")
    apply_registration(manager_advanced)
