from typing import List

# --- 1. Aggregation (การรวมกลุ่ม) ---
# ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย" ที่หลวมๆ
# ส่วนประกอบ (Part) สามารถดำรงอยู่ได้ด้วยตัวเองโดยไม่ต้องพึ่งพาคอนเทนเนอร์ (Whole)

class Driver:
    def __init__(self, name: str):
        self.name = name

class Car:
    def __init__(self, model: str):
        self.model = model
        # Car "มี" Driver (Aggregation)
        self.driver = None

    def set_driver(self, driver: Driver):
        self.driver = driver
        print(f"Driver {driver.name} is now driving {self.model}.")

    def remove_driver(self):
        if self.driver:
            print(f"Driver {self.driver.name} left the car.")
            self.driver = None

# --- 2. Composition (องค์ประกอบ) ---
# ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย" ที่เข้มงวด
# ส่วนประกอบไม่สามารถดำรงอยู่ได้หากไม่มีคอนเทนเนอร์ (จัดการ Life Cycle)

class Department:
    def __init__(self, name: str):
        self.name = name
        print(f"Department '{self.name}' was established.")

    def __del__(self):
        # แสดงให้เห็นว่าเมื่อถูกทำลาย (Delete) ภาควิชาก็จะหายไปด้วย
        print(f"Department '{self.name}' was closed.")

class University:
    def __init__(self, name: str, dept_names: List[str]):
        self.name = name
        # Composition: สร้าง Department ขึ้นมาภายใน University เอง
        # University รับผิดชอบการสร้างและทำลาย Department
        self.departments = [Department(name) for name in dept_names]
        print(f"University '{self.name}' was founded.")

    def __del__(self):
        print(f"University '{self.name}' was dissolved.")
        # ใน Python เมื่อ University หายไป (Garbage Collected) 
        # departments ที่เป็นฟิลด์ภายในก็จะถูกทำลายตามไปด้วย (Composition)

if __name__ == '__main__':
    print("--- 🔵 ตัวอย่าง Aggregation (รถยนต์กับคนขับ) ---")
    driver_alice = Driver("Alice")
    toyota = Car("Toyota Corolla")
    
    toyota.set_driver(driver_alice)
    toyota.remove_driver()
    
    print(f"Check: Driver {driver_alice.name} is still here! (อิสระจากรถ)")
    
    print("\n--- 🟣 ตัวอย่าง Composition (มหาวิทยาลัยกับภาควิชา) ---")
    def create_and_destroy_uni():
        my_uni = University("Tech University", ["Computer Science", "Engineering"])
        print(f"University {my_uni.name} is active.")
        # เมื่อจบฟังก์ชัน my_uni จะถูกทำลาย (Dissolved)
    
    create_and_destroy_uni()
    
    print("\n✅ สรุป:")
    print("1. Aggregation: คนขับ (Driver) อยู่นอกรถได้ สลับไปขับคันอื่นได้")
    print("2. Composition: ภาควิชา (Department) ถูกสร้างและตายไปพร้อมกับมหาวิทยาลัย")
