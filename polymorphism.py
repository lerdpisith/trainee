from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # เมธอดแม่ที่คลาสลูกจะนำไป Override
        pass

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        # Polymorphism: การ Override เมธอด area สำหรับสี่เหลี่ยม
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        # Polymorphism: การ Override เมธอด area สำหรับวงกลม
        import math
        return math.pi * (self.radius ** 2)

def print_area(shape: Shape):
    # ฟังก์ชันนี้แสดงถึง Polymorphism: มันรับ Object ประเภทใดก็ได้ที่เป็น Shape
    # และเรียกใช้เมธอด area() โดยไม่สนใจว่าข้างในจะเป็นสี่เหลี่ยมหรือวงกลม
    print(f"The area is: {shape.area():.2f}")


# --- 🏢 ตัวอย่างการประยุกต์ใช้ Polymorphism ในระบบจริง: บริษัทพัฒนาซอฟต์แวร์ ---

# 1. อินเทอร์เฟซส่วนกลาง (Employee)
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def do_work(self):
        """กำหนดพฤติกรรมหลักร่วมกัน"""
        pass

# 2. คลาสพนักงานเฉพาะเจาะจงแต่ละตำแหน่ง (Concrete Classes)
class Designer(Employee):
    def do_work(self):
        return f"🎨 {self.name} (Designer) is designing user interface."

class Programmer(Employee):
    def do_work(self):
        return f"💻 {self.name} (Programmer) is writing code."

class Tester(Employee):
    def do_work(self):
        return f"🧪 {self.name} (Tester) is testing software bugs."

# 3. คลาสบริษัท (Company)
class Company:
    def __init__(self, name: str):
        self.name = name
        # จัดเก็บพนักงานทั้งหมดไว้รวมกันในฐานะพนักงานทั่วไป (Employee)
        self.employees: list[Employee] = []

    def hire(self, employee: Employee):
        self.employees.append(employee)
        print(f">> [System]: {employee.name} has joined {self.name}!")

    def start_work_day(self):
        print(f"\n--- วันทำงานของบริษัท {self.name} เริ่มต้นขึ้นแล้ว ---")
        # กลไกของ Polymorphism จะตรวจจับคลาสที่แท้จริงของพนักงานแต่ละคนโดยอัตโนมัติ
        for emp in self.employees:
            print(emp.do_work())

if __name__ == '__main__':
    # --- ส่วนที่ 1: ตัวอย่างพื้นฐาน (Shapes) ---
    print("--- 1. Polymorphism with Shapes ---")
    shapes = [Square(5), Circle(3)]
    for s in shapes:
        print_area(s)

    # --- ส่วนที่ 2: ตัวอย่างระบบบริษัทพัฒนาซอฟต์แวร์ ---
    print("\n--- 2. Polymorphism in Software Company (Decoupling) ---")
    
    # สร้างบริษัท
    tech_corp = Company("Tech Solutions")

    # จ้างพนักงานประเภทต่างๆ
    tech_corp.hire(Designer("Alice"))
    tech_corp.hire(Programmer("Bob"))
    tech_corp.hire(Tester("Charlie"))

    # สั่งให้ทุกคนทำงาน (Polymorphism จะเรียก Method ที่ถูกต้องตามหน้าที่ของแต่ละคน)
    tech_corp.start_work_day()

    print("\n✅ สรุป: Polymorphism ช่วยให้คลาส Company ไม่ต้องขึ้นตรงกับประเภทพนักงานที่เฉพาะเจาะจง (Tightly Coupled)")
    print("และเราสามารถเพิ่มพนักงานประเภทใหม่ได้โดยไม่ต้องแก้ไขโค้ดของคลาส Company เลย")
