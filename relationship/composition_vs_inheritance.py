from abc import ABC, abstractmethod

# --- 1. ปัญหาสามัญ: Class Explosion ด้วยการสืบทอด (Inheritance) ---
# ลองจินตนาการว่าคุณต้องสร้างแอปพลิเคชันแคตตาล็อกสำหรับบริษัทผลิตรถยนต์
# ความต้องการของระบบมีการเปลี่ยนแปลงได้ใน 3 มิติ (Dimensions):
# 1. ชนิดของยานพาหนะ (รถยนต์, รถบรรทุก)
# 2. ชนิดของเครื่องยนต์ (ไฟฟ้า, สันดาป)
# 3. ระบบควบคุม (คนขับ, ออโต้ไพลอต)

# หากใช้ Inheritance ในการออกแบบ คุณจะต้องสร้างคลาสลูกสำหรับทุกการประกอบกันที่เป็นไปได้ (2x2x2 = 8 คลาส)
# ตัวอย่าง:
class Car: pass
class Truck: pass

# มิติที่ 2: เครื่องยนต์ (Engine)
class ElectricCar(Car): pass
class CombustionCar(Car): pass
class ElectricTruck(Truck): pass
class CombustionTruck(Truck): pass

# มิติที่ 3: ระบบควบคุม (Control) -> Class Explosion!
class AutopilotElectricCar(ElectricCar): pass
class ManualElectricCar(ElectricCar): pass
class AutopilotCombustionCar(CombustionCar): pass
class ManualCombustionCar(CombustionCar): pass
class AutopilotElectricTruck(ElectricTruck): pass
class ManualElectricTruck(ElectricTruck): pass
# ... และคลาสอื่นๆ อีกมากมายให้ครบทุกความเป็นไปได้ (Combinatorial Explosion)
# นอกจากจะบวมแล้ว ยังเกิดโค้ดซ้ำซ้อนกันมหาศาลระหว่างคลาสลูกต่างๆ

# --- 2. การแก้ปัญหาด้วยองค์ประกอบ (Composition) ---
# เปลี่ยนมุมมองจาก "เป็น (is-a)" มาเป็น "มี (has-a)"
# ยานพาหนะ "มี" เครื่องยนต์ และ "มี" ระบบควบคุม

class Engine(ABC):
    @abstractmethod
    def start(self): pass

class ElectricEngine(Engine):
    def start(self): return "Zzz... Electric motor started silently."

class CombustionEngine(Engine):
    def start(self): return "Vroom! Combustion engine started."

class ControlSystem(ABC):
    @abstractmethod
    def drive(self): pass

class HumanDriver(ControlSystem):
    def drive(self): return "คนขับกำลังขับรถอย่างระมัดระวัง (Manual)"

class Autopilot(ControlSystem):
    def drive(self): return "ออโต้ไพลอต (Autopilot) กำลังควบคุมรถอัตโนมัติ"

class Vehicle:
    def __init__(self, brand: str, model: str, engine: Engine, control: ControlSystem):
        self.brand = brand
        self.model = model
        # องค์ประกอบ (Composition): ยานพาหนะ "มี" เครื่องยนต์ และ "มี" ระบบควบคุม
        self.engine = engine
        self.control = control

    def operate(self):
        print(f"\n--- กำลังใช้งาน {self.brand} {self.model} ---")
        # การมอบหมาย (Delegation): มอบหมายงานให้ส่วนประกอบต่างๆ จัดการแทน
        print(f"เครื่องยนต์: {self.engine.start()}")
        print(f"ระบบควบคุม: {self.control.drive()}")

    def set_engine(self, new_engine: Engine):
        print(f">> [System]: Changing engine to {type(new_engine).__name__}")
        self.engine = new_engine

    def set_control(self, new_control: ControlSystem):
        print(f">> [System]: Changing control to {type(new_control).__name__}")
        self.control = new_control

class Car(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, control: ControlSystem):
        super().__init__(brand, model, engine, control)
        self.type = "รถยนต์ (Car)"

    def operate(self):
        print(f"ประเภท: {self.type}")
        super().operate()

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, control: ControlSystem):
        super().__init__(brand, model, engine, control)
        self.type = "รถบรรทุก (Truck)"

    def operate(self):
        print(f"ประเภท: {self.type}")
        super().operate()

if __name__ == '__main__':
    print("--- 🚗 Composition vs Inheritance: แก้ไขปัญหา Class Bloat ---")
    
    # แทนที่จะต้องสร้าง 8 คลาส (2x2x2) เรามีเพียงคลาสหลักและอินเทอร์เฟซสำหรับแต่ละมิติ
    # และนำส่วนประกอบ (Components) มาประกอบกัน (Mix and Match) อย่างอิสระ
    
    # 1. สร้างรถยนต์ไฟฟ้าแบบออโต้ไพลอต (AutopilotElectricCar)
    tesla = Car("Tesla", "Model 3", ElectricEngine(), Autopilot())
    tesla.operate()

    # 2. Runtime Flexibility: เปลี่ยนระบบควบคุมกลับมาเป็นคนขับได้ทันที (Manual)
    tesla.set_control(HumanDriver())
    tesla.operate()

    # 3. สร้างรถบรรทุกเครื่องยนต์สันดาปที่มีคนขับ (ManualCombustionTruck)
    truck = Truck("Isuzu", "Giga", CombustionEngine(), HumanDriver())
    truck.operate()

    # 4. เปลี่ยนรถบรรทุกเดิมให้เป็นออโต้ไพลอต และเปลี่ยนเครื่องยนต์เป็นไฟฟ้า (Future Concept)
    truck.set_engine(ElectricEngine())
    truck.set_control(Autopilot())
    truck.operate()

    print("\n✅ สรุป: Composition ช่วยป้องกันปัญหา Class Bloat (หรือ Combinatorial Explosion)")
    print("โดยการแยกมิติของการขยายความสามารถออกจากกัน (Separation of Dimensions)")
    print("และยังให้ความยืดหยุ่นสูงในการเปลี่ยนพฤติกรรมขณะรันไทม์ (Runtime Flexibility)")
