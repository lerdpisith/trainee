from abc import ABC, abstractmethod
from typing import List

# 1. Dependency (ความพึ่งพา) - อ่อนแอที่สุด
# เกิดขึ้นเมื่อคลาสหนึ่งใช้งานอีกคลาสหนึ่งในเมธอด (มักเป็น parameter)
# ไม่ได้เก็บเป็นฟิลด์ (field) ถาวร
class Logger:
    def log(self, message: str):
        print(f"[Log]: {message}")

class UserService:
    def register(self, username: str, logger: Logger): # Dependency on Logger
        # UserService พึ่งพา Logger แค่ในตอนที่ทำงานในเมธอดนี้
        logger.log(f"User {username} registered.")

# 2. Association (ความเชื่อมโยง)
# วัตถุหนึ่งรู้จักและเชื่อมโยงกับอีกวัตถุหนึ่งผ่าน "ฟิลด์" (field)
class Driver:
    def __init__(self, name: str):
        self.name = name

class Car:
    def __init__(self, model: str):
        self.model = model
        self.driver = None # Association: Car สามารถมี Driver ได้

# 3. Aggregation (การรวมกลุ่ม) - ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย"
# ส่วนประกอบ (Part) สามารถดำรงอยู่ได้ด้วยตัวเองแม้ไม่มีคอนเทนเนอร์ (Whole)
class Department:
    def __init__(self, name: str):
        self.name = name

class University:
    def __init__(self, name: str, departments: List[Department]):
        self.name = name
        self.departments = departments # Aggregation: University มีหลาย Department
        # ถ้า University ถูกทำลาย Department ยังสามารถดำรงอยู่ได้

# 4. Composition (องค์ประกอบ) - แข็งแกร่งกว่า Aggregation
# ส่วนประกอบไม่สามารถดำรงอยู่ได้ถ้าไม่มีคอนเทนเนอร์ (จัดการ Life Cycle)
class Room:
    def __init__(self, name: str):
        self.name = name

class House:
    def __init__(self):
        # Composition: House สร้าง Room ขึ้นมาเองภายใน
        self.rooms = [Room("Living Room"), Room("Kitchen")]
        # ถ้า House ถูกทำลาย Room เหล่านี้ก็จะถูกทำลายไปด้วย

# 5. Implementation (การนำอินเทอร์เฟซไปใช้งาน)
# คลาสกำหนดรายละเอียดการทำงานตามที่ Interface ระบุไว้
class Printable(ABC):
    @abstractmethod
    def print_content(self):
        pass

class Document(Printable): # Implementation
    def print_content(self):
        print("Printing document content...")

# 6. Inheritance (การสืบทอด) - แข็งแกร่งและผูกพันที่สุด
# สืบทอดทั้ง Interface และ Implementation
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal): # Inheritance
    def bark(self):
        print("Woof!")

if __name__ == '__main__':
    print("--- 1. Dependency ---")
    logger = Logger()
    service = UserService()
    service.register("Junie", logger)

    print("\n--- 3. Aggregation ---")
    hr_dept = Department("HR")
    it_dept = Department("IT")
    my_uni = University("Tech Uni", [hr_dept, it_dept])
    print(f"{my_uni.name} has departments: {[d.name for d in my_uni.departments]}")

    print("\n--- 4. Composition ---")
    my_house = House()
    print(f"House has rooms: {[r.name for r in my_house.rooms]}")

    print("\n--- 6. Inheritance ---")
    milo = Dog()
    milo.eat() # ใช้เมธอดจากคลาสแม่
    milo.bark()
