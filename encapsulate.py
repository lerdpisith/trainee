class HumanResource:
    def __init__(self, name: str, salary: int):
        self.name = name
        # --- 1. การซ่อนสถานะ (Hiding State/Fields) ---
        # Private Variable: เก็บเป็นความลับ ไม่ให้แก้ไขโดยตรงจากภายนอก
        self.__salary = salary

    def get_salary(self):
        # Getter: วิธีการขอดูเงินเดือนอย่างปลอดภัย
        return self.__salary

    def set_salary(self, new_salary: int):
        # Setter: วิธีการปรับเงินเดือน พร้อมตรวจสอบความถูกต้อง
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("❌ Error: Salary must be positive!")

# --- 2. การซ่อนรายละเอียดพฤติกรรม (Hiding Behaviors/Mechanism) ---
# ตัวอย่างเปรียบเทียบ: การขับรถยนต์
class Car:
    def __init__(self, brand: str):
        self.brand = brand
        self.__is_engine_running = False  # Private State: สถานะเครื่องยนต์
        self.__fuel_level = 10            # Private State: ระดับน้ำมัน

    # --- อินเทอร์เฟซที่กำหนดไว้ (Exposing a Limited Public Interface) ---
    def start_engine(self):
        """ผู้ใช้เพียงแค่เรียกใช้เมธอดนี้ (เหมือนบิดกุญแจ) โดยไม่ต้องรู้กลไกภายใน"""
        print(f"\n>> กำลังสตาร์ทเครื่องยนต์ {self.brand}...")
        
        if self.__fuel_level > 0:
            # เรียกใช้พฤติกรรมภายในที่ถูกซ่อนไว้
            self.__inject_fuel()
            self.__ignite()
            self.__is_engine_running = True
            print("✅ เครื่องยนต์ทำงานแล้ว! บรื๊นๆ")
        else:
            print("❌ สตาร์ทไม่ติด: น้ำมันหมด!")

    # --- การกำหนดสิทธิ์การเข้าถึงเป็นส่วนตัว (Making it Private) ---
    def __inject_fuel(self):
        """กลไกการฉีดน้ำมัน: รายละเอียดที่ซับซ้อนที่ 'ซ่อนไว้ใต้ฝากระโปรงรถ'"""
        print("[System]: ฉีดน้ำมันเข้าห้องเผาไหม้...")

    def __ignite(self):
        """กลไกการจุดระเบิด: รายละเอียดที่ผู้ใช้ไม่ควร (และไม่จำเป็น) ต้องไปยุ่งเกี่ยว"""
        print("[System]: หัวเทียนทำงานเพื่อจุดระเบิด...")

    def get_status(self):
        status = "ติดเครื่องอยู่" if self.__is_engine_running else "ดับเครื่อง"
        return f"สถานะรถ {self.brand}: {status}, ระดับน้ำมัน: {self.__fuel_level}%"

if __name__ == '__main__':
    print("--- 🔒 การห่อหุ้ม (Encapsulation): การรักษาความปลอดภัยของข้อมูล ---")
    
    # 1. ตัวอย่าง HumanResource: การใช้ Private Fields
    hr = HumanResource("Alice", 50000)
    print(f"Name: {hr.name}")
    print(f"Original Salary: {hr.get_salary()}")

    hr.set_salary(55000)
    print(f"New Salary: {hr.get_salary()}")

    # 2. ตัวอย่าง Car: การซ่อนรายละเอียด (Hiding Mechanism)
    my_car = Car("Toyota")
    
    # ผู้ใช้งานโต้ตอบผ่านอินเทอร์เฟซสาธารณะ (Public Interface) เท่านั้น
    print(my_car.get_status())
    my_car.start_engine()
    
    # พยายามเรียกใช้กลไกภายในโดยตรง (จะเกิด AttributeError)
    # my_car.__inject_fuel() # ❌ ไม่สามารถทำได้: เปรียบเหมือนไปรื้อสายไฟใต้ฝากระโปรงเอง
    
    print(my_car.get_status())

    print("\n✅ สรุป: Encapsulation ช่วยซ่อนรายละเอียดที่ซับซ้อน (Under the hood)")
    print("ทำให้ใช้งานง่ายขึ้นและป้องกันการเข้าถึงข้อมูลที่สำคัญโดยไม่ตั้งใจ")

