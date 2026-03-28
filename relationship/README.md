# 📦 ความสัมพันธ์ระหว่างวัตถุ (Object Relationships)

ในบทนี้เราจะมาทำความเข้าใจว่าวัตถุและคลาสต่างๆ มีปฏิสัมพันธ์และเชื่อมโยงกันอย่างไร โดยแบ่งระดับจาก **อ่อนแอที่สุดไปหาแข็งแกร่งที่สุด**

## 📂 ไฟล์ภายในไดเรกทอรี
- `association.py`: ตัวอย่างความสัมพันธ์เบื้องต้น (อาจารย์, นักเรียน และวิชาเรียน)
- `object_relationships.py`: ตัวอย่างความสัมพันธ์ครบทั้ง 6 ระดับ (Dependency -> Inheritance)
- `practical_example.py`: ตัวอย่างเชิงปฏิบัติ (ระบบโรงพยาบาล) ที่รวมความสัมพันธ์หลายแบบเข้าด้วยกัน
- `composition_vs_inheritance.py`: ตัวอย่างการเปรียบเทียบ Composition และ Inheritance (Runtime Flexibility)

---

## 🔍 ระดับความสัมพันธ์ (The Big Picture)

ในการออกแบบซอฟต์แวร์ ความสัมพันธ์ของวัตถุสามารถสรุปตามระดับความผูกพัน (Coupling) ได้ดังนี้:

### 1. Dependency (ความพึ่งพา) 🟡 *อ่อนแอที่สุด*
เกิดเมื่อคลาส A ใช้งานคลาส B ในช่วงเวลาสั้นๆ (เช่น เป็น parameter ในเมธอด) หากคลาส B เปลี่ยนแปลง คลาส A อาจได้รับผลกระทบ
```python
def register(self, logger: Logger): # Dependency on Logger
    logger.log("Registered")
```

### 2. Association (ความเชื่อมโยง) 🟢
วัตถุหนึ่ง "รู้จัก" และเชื่อมโยงกับอีกวัตถุหนึ่งอย่างถาวรผ่านการใช้ "ฟิลด์" (field)
```python
class Car:
    def __init__(self):
        self.driver = None # Association: Car รู้จัก Driver
```

### 3. Aggregation (การรวมกลุ่ม) 🔵
ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย" (Whole-Part) โดยที่ **ส่วนย่อยสามารถดำรงอยู่ได้ด้วยตัวเอง** แม้ไม่มีคอนเทนเนอร์
- เช่น: มหาวิทยาลัย กับ คณะ (ถ้ามหาวิทยาลัยปิด คณะยังอาจไปตั้งที่อื่นได้)
```python
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments # Aggregation: รับ Object จากภายนอก
```

### 4. Composition (องค์ประกอบ) 🟣
ความสัมพันธ์แบบ "ส่วนรวม-ส่วนย่อย" ที่เข้มงวด โดยที่ **ส่วนย่อยจะสลายไปพร้อมกับคอนเทนเนอร์** (คอนเทนเนอร์จัดการ Life Cycle)
- เช่น: บ้าน กับ ห้อง (ถ้าบ้านถูกทำลาย ห้องก็หายไปด้วย)
```python
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # Composition: สร้าง Object ภายในคลาสเอง
        self.rooms = [Room("Kitchen"), Room("Bedroom")]
```

### 5. Implementation (การนำอินเทอร์เฟซไปใช้งาน) 🟠
คลาสกำหนดรายละเอียดการทำงาน (Implementation) ตามที่ Interface ระบุไว้
```python
class Printable(ABC):
    @abstractmethod
    def print_content(self): pass

class Document(Printable): # Implementation
    def print_content(self):
        print("Printing document...")
```

### 6. Inheritance (การสืบทอด) 🔴 *แข็งแกร่งที่สุด*
คลาสลูกสืบทอดทั้งคุณสมบัติและการทำงานจากคลาสแม่ เป็นความสัมพันธ์ที่มีความผูกพัน (Coupling) สูงที่สุด
```python
class Animal:
    def eat(self): print("Eating...")

class Dog(Animal): # Inheritance
    def bark(self): print("Woof!")
```

#### ⚠️ ข้อจำกัดและปัญหาของการสืบทอด (Inheritance)
แม้ว่าการสืบทอดจะเป็นวิธีที่ง่ายในการนำโค้ดกลับมาใช้ใหม่ แต่เมื่อระบบมีขนาดใหญ่ขึ้นจะพบปัญหาดังนี้:
*   **คลาสลูกไม่สามารถลดขนาดอินเทอร์เฟซได้:** คลาสลูกถูกบังคับให้ต้องนำเมธอดนามธรรม (abstract methods) ของคลาสแม่ไปอิมพลีเมนต์เสมอ แม้จะไม่ได้ใช้งานเลยก็ตาม
*   **ความเสี่ยงเรื่องความเข้ากันได้:** การเขียนทับ (override) เมธอด ต้องมั่นใจว่าพฤติกรรมใหม่เข้ากันได้กับคลาสแม่ (LSP) เพื่อไม่ให้โค้ดของไคลเอนต์ที่เรียกใช้พังลง
*   **การทำลายการห่อหุ้ม (Breaks Encapsulation):** รายละเอียดภายในของคลาสแม่ถูกเปิดเผยให้คลาสลูกเข้าถึงได้ ทำให้ความลับของข้อมูลเสียไป
*   **ความผูกพันที่แน่นแฟ้น (Tight Coupling):** คลาสลูกผูกติดกับคลาสแม่อย่างมาก การเปลี่ยนแปลงเพียงเล็กน้อยในคลาสแม่อาจทำให้คลาสลูกพังได้
*   **การขยายตัวของลำดับชั้นคลาส (Combinatorial Explosion):** หากต้องขยายความสามารถหลายมิติพร้อมกัน จะต้องสร้างคลาสลูกผสมผสานจำนวนมหาศาล (Class Explosion)
*   **มีลักษณะที่ตายตัว (Static):** ไม่สามารถเปลี่ยนพฤติกรรมของวัตถุได้ในขณะรันไทม์ ต้องสร้างวัตถุใหม่เท่านั้น
*   **ข้อจำกัดการสืบทอด:** ภาษาหลักส่วนใหญ่ (รวมถึง Python ในเชิงปฏิบัติ) มักเน้นการสืบทอดจากคลาสแม่หลักเพียงคลาสเดียว

### 💡 ทำไมควร "เลือกใช้ Composition มากกว่า Inheritance"?

**องค์ประกอบ (Composition)** เป็นทางเลือกที่ยืดหยุ่นกว่า โดยเปลี่ยนจากความสัมพันธ์แบบ **"เป็น (is a)"** มาเป็น **"มี (has a)"** (เช่น รถยนต์มีเครื่องยนต์)

#### ประโยชน์ของ Composition:
1.  **การมอบหมายงาน (Delegation):** แทนที่วัตถุจะทำทุกอย่างเอง มันสามารถมอบหมายหน้าที่เฉพาะทางไปให้วัตถุส่วนประกอบ (Component) ที่มันบรรจุไว้ทำงานแทนได้
2.  **ความยืดหยุ่นขณะรันไทม์ (Runtime Flexibility):** คุณสามารถ**เปลี่ยนแปลงพฤติกรรมของวัตถุได้ตลอดเวลา**เพียงแค่สลับวัตถุส่วนประกอบตัวใหม่มาแทนที่ตัวเดิม
3.  **ลดความซ้ำซ้อน:** ไม่ต้องสร้างคลาสลูกจำนวนมากเพื่อรองรับทุกการผสมผสานความสามารถ

---

### 🚀 Composition vs Inheritance (ตัวอย่างการเปรียบเทียบ)

ดูตัวอย่างการออกแบบระบบรถยนต์ที่ต้องการเปลี่ยนเครื่องยนต์ได้:

**แบบ Inheritance (Class Explosion):**
```python
class Car: pass
class GasolineCar(Car): pass
class ElectricCar(Car): pass
class DieselCar(Car): pass
# หากเพิ่ม "ระบบเกียร์" (Manual/Auto) จะต้องสร้างคลาสเพิ่มเป็น 3x2 = 6 คลาส!
```

**แบบ Composition (ยืดหยุ่นกว่า - ดูใน `composition_vs_inheritance.py`):**
```python
class Car:
    def __init__(self, engine):
        self.engine = engine # Car HAS AN engine

    def change_engine(self, new_engine):
        self.engine = new_engine # เปลี่ยนได้ทันทีขณะรันไทม์!
```

---

## 🏥 ตัวอย่างเชิงปฏิบัติ: ระบบโรงพยาบาล (`practical_example.py`)

เพื่อให้เห็นภาพการทำงานจริง ไฟล์นี้ได้รวมความสัมพันธ์ต่างๆ ไว้ในระบบเดียว:
- **Hospital (Aggregation)** มี **Doctors** (หมออยู่ได้แม้ไม่มีโรงพยาบาลนี้)
- **Hospital (Composition)** มี **EmergencyRoom** (ER ถูกสร้างและสลายไปพร้อมโรงพยาบาล)
- **Doctor (Association)** รู้จักกับ **Patient**
- **Doctor (Dependency)** เรียกใช้ **PharmacyService** เพื่อสั่งยา
- **Surgeon (Inheritance)** สืบทอดมาจาก **Doctor**
- **Doctor (Implementation)** ทำงานตามมาตรฐานของ **Staff** (Interface)

---

---

## 💻 ตัวอย่างการรันโค้ด
คุณสามารถรันไฟล์เพื่อดูตัวอย่างการทำงานของความสัมพันธ์แต่ละระดับได้:
```bash
python3 relationship/object_relationships.py
python3 relationship/practical_example.py
python3 relationship/composition_vs_inheritance.py
```
