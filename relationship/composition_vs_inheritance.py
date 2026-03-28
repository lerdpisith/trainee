from abc import ABC, abstractmethod

# --- 1. ปัญหาสามัญ: Class Explosion ด้วยการสืบทอด (Inheritance) ---
# สมมติว่าเราต้องการสร้างรถที่มี "ชนิดของเครื่องยนต์" และ "ชนิดของเชื้อเพลิง" ที่ต่างกัน
# หากใช้ Inheritance เราจะต้องสร้างคลาสย่อยจำนวนมากเพื่อรองรับทุกๆ รูปแบบที่เป็นไปได้ (2x2 = 4 คลาส)
# และหากเพิ่มมิติที่ 3 เข้ามา เช่น "ระบบขับเคลื่อน" (2x2x2 = 8 คลาส) จะทำให้เกิด Class Explosion ทันที

class Car:
    def drive(self): pass

class ElectricGasolineCar(Car): pass # ไฮบริด? 
class DieselTruck(Car): pass
# ... การจัดการจะเริ่มซับซ้อนและมีโค้ดที่ซ้ำซ้อนกันมาก


# --- 2. ทางเลือกที่ยืดหยุ่น: การประกอบวัตถุ (Composition) ---
# เปลี่ยนจากความสัมพันธ์แบบ "เป็น (is-a)" มาเป็น "มี (has-a)"
# รถยนต์ "มี" เครื่องยนต์

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class GasolineEngine(Engine):
    def start(self):
        return "Vroom! Gasoline engine started."

class ElectricEngine(Engine):
    def start(self):
        return "Zzz... Electric motor started silently."

class DieselEngine(Engine):
    def start(self):
        return "Rumble! Diesel engine started."

class CarWithComposition:
    def __init__(self, model: str, engine: Engine):
        self.model = model
        # Car has an Engine (Composition/Aggregation)
        self.engine = engine

    def start_car(self):
        print(f"Starting {self.model}...")
        # Delegation: มอบหมายหน้าที่ให้วัตถุส่วนประกอบทำงานแทน
        status = self.engine.start()
        print(f"Status: {status}")

    def change_engine(self, new_engine: Engine):
        # Runtime Flexibility: เปลี่ยนพฤติกรรมของวัตถุได้ขณะรันไทม์!
        print(f"\n--- Changing engine for {self.model} ---")
        self.engine = new_engine

if __name__ == '__main__':
    print("--- 🚗 ตัวอย่าง Composition: รถยนต์และการเปลี่ยนเครื่องยนต์ ---")
    
    # 1. เริ่มต้นด้วยรถยนต์ที่ใช้เครื่องยนต์น้ำมัน
    my_car = CarWithComposition("Sedan X", GasolineEngine())
    my_car.start_car()

    # 2. Runtime Flexibility: เปลี่ยนเครื่องยนต์เป็นมอเตอร์ไฟฟ้าได้ทันทีโดยไม่ต้องสร้าง Object รถใหม่
    my_car.change_engine(ElectricEngine())
    my_car.start_car()

    # 3. ลองเปลี่ยนเป็นเครื่องยนต์ดีเซล
    my_car.change_engine(DieselEngine())
    my_car.start_car()

    print("\n✅ สรุป: Composition ช่วยให้เราผสมความสามารถ (Mix and Match) ได้อย่างอิสระ "
          "\nและเปลี่ยนพฤติกรรมได้ในขณะที่โปรแกรมกำลังทำงาน (Runtime Flexibility)")
