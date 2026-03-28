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
        self.driver = None # Association: Car สามารถมี Driver ได้ (รู้จักกันถาวร)

# 3. Aggregation (การรวมกลุ่ม) - ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย"
# ส่วนประกอบ (Part) สามารถดำรงอยู่ได้ด้วยตัวเองแม้ไม่มีคอนเทนเนอร์ (Whole)
class Passenger:
    def __init__(self, name: str):
        self.name = name

class Bus:
    def __init__(self, route: str):
        self.route = route
        self.passengers: List[Passenger] = [] # Aggregation: Bus มีหลาย Passenger
        # ถ้า Bus ถูกทำลาย Passenger ยังสามารถไปขึ้นคันอื่นได้

# 4. Composition (องค์ประกอบ) - แข็งแกร่งกว่า Aggregation
# ส่วนประกอบไม่สามารถดำรงอยู่ได้ถ้าไม่มีคอนเทนเนอร์ (จัดการ Life Cycle)
class Department:
    def __init__(self, name: str):
        self.name = name

class University:
    def __init__(self, name: str):
        self.name = name
        # Composition: University สร้าง Department ขึ้นมาเองภายใน
        self.departments = [Department("Computer Science"), Department("Engineering")]
        # ถ้า University ถูกทำลาย Department เหล่านี้ก็จะถูกทำลายไปด้วย

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
    p1 = Passenger("Alice")
    p2 = Passenger("Bob")
    bus = Bus("Route 101")
    bus.passengers = [p1, p2]
    print(f"Bus on {bus.route} has passengers: {[p.name for p in bus.passengers]}")

    print("\n--- 4. Composition ---")
    my_uni = University("Tech Uni")
    print(f"University {my_uni.name} has departments: {[d.name for d in my_uni.departments]}")

    print("\n--- 6. Inheritance ---")
    milo = Dog()
    milo.eat() # ใช้เมธอดจากคลาสแม่
    milo.bark()
