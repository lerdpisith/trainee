from abc import ABC, abstractmethod

# --- 1. อินเทอร์เฟซ (Interface) ---
# ใน Python เราใช้ Abstract Base Class (ABC) ที่มีแต่ @abstractmethod
# มุ่งเน้นไปที่ "สัญญา (Contract)" ว่าต้องทำอะไรได้บ้าง (Behavior)
# ข้อดี: สามารถนำไปใช้งาน (Implement) ได้หลายอินเทอร์เฟซพร้อมกัน และแบ่งย่อยได้ (Segregation)
# ข้อเสีย: ไม่สามารถเก็บข้อมูลสถานะ (No State) หรือฟิลด์ได้

class Flyable(ABC):
    @abstractmethod
    def fly(self): pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass

# ตัวอย่าง: ปลาบินที่ทำงานได้ทั้งบินและว่ายน้ำ (Multiple Implementation)
class FlyingFish(Flyable, Swimmable):
    def fly(self):
        print("Flying fish is gliding over the water!")
    
    def swim(self):
        print("Flying fish is swimming deep in the ocean.")

# --- 2. คลาสนามธรรม (Abstract Class) ---
# มุ่งเน้นไปที่ "โครงสร้างพื้นฐาน (Base Template)" เพื่อลดความซ้ำซ้อนของโค้ด
# ข้อดี: มีฟิลด์เก็บสถานะ (State) และเมธอดที่มีการทำงานจริง (Concrete Method) ได้
# ข้อเสีย: สืบทอดได้เพียงคลาสเดียว (Single Inheritance) และถูกบังคับให้อิมพลีเมนต์พฤติกรรมทั้งหมด

class Animal(ABC):
    def __init__(self, name: str):
        # เก็บสถานะ (State) ไว้ในคลาสแม่ได้
        self.name = name
    
    def breathe(self):
        # เมธอดที่มีการทำงานจริงเพื่อแชร์ให้คลาสลูก (Code Reuse)
        print(f"{self.name} is breathing.")

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    # สืบทอด Animal มา (is-a relationship)
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

if __name__ == '__main__':
    print("--- 🔵 อินเทอร์เฟซ (Interface) ---")
    fish = FlyingFish()
    fish.fly()
    fish.swim()

    print("\n--- 🟢 คลาสนามธรรม (Abstract Class) ---")
    dog = Dog("Buddy")
    dog.breathe()    # ใช้โค้ดจากคลาสแม่ (Code Reuse)
    dog.make_sound() # ทำงานตามพฤติกรรมของตัวเอง

    print("\n--- 💡 สรุปเปรียบเทียบ ---")
    print("1. Interface: เน้น 'พฤติกรรม' (Behavior) - วัตถุทำอะไรได้บ้าง?")
    print("2. Abstract Class: เน้น 'โครงสร้าง' (Structure) - วัตถุคืออะไร?")
