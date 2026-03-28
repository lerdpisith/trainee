# คู่มือการเรียนรู้ Object-Oriented Programming (OOP) ด้วย Python

ยินดีต้อนรับสู่โปรเจกต์สำหรับผู้เริ่มต้นศึกษาแนวคิดการเขียนโปรแกรมเชิงวัตถุ (OOP) และหลักการ SOLID ผ่านภาษา Python ในโปรเจกต์นี้จะรวบรวมตัวอย่างโค้ดที่แบ่งตามหัวข้อพื้นฐานไปจนถึงระดับที่สูงขึ้น เพื่อให้เข้าใจง่ายและนำไปประยุกต์ใช้ได้จริง

---

## 📂 โครงสร้างโปรเจกต์

โปรเจกต์นี้แบ่งไฟล์ตามแนวคิดหลักของ OOP ดังนี้:

1.  **`cat.py`**: พื้นฐาน Class และ Instance (วัตถุ)
2.  **`animal.py`**: การสืบทอด (Inheritance) และการเขียนทับเมธอด (Method Overriding)
3.  **`abstraction.py`**: การทำ Abstraction (คลาสโครงร่าง) โดยใช้ `ABC`
4.  **`encapsulate.py`**: การปกป้องข้อมูล (Encapsulation) และ Getter/Setter
5.  **`polymorphism.py`**: การพหุสัณฐาน (Polymorphism) และการ Override
6.  **[relationship/association.py](relationship/association.py)**: ความสัมพันธ์ระหว่างวัตถุ (Association) ([อ่านรายละเอียดเพิ่มเติมในไดเรกทอรี](relationship/README.md))
7.  **[solid/principle.py](solid/principle.py)**: หลักการออกแบบซอฟต์แวร์ที่ดี (SOLID Principles) ([อ่านรายละเอียดเพิ่มเติมในไดเรกทอรี](solid/README.md))

---

## 🔍 รายละเอียดในแต่ละบทเรียน

### 1. พื้นฐาน Class และ Instance (`cat.py`)
ไฟล์นี้แสดงวิธีการสร้างคลาสพื้นฐาน:
- **Class**: พิมพ์เขียวหรือแบบแปลน (เช่น คลาส `Cat`)
- **Instance**: วัตถุที่สร้างขึ้นจากคลาส (เช่น `luna` และ `oscar`)
- **`__init__`**: ฟังก์ชันพิเศษที่ใช้กำหนดค่าเริ่มต้นให้กับวัตถุ

```python
# ตัวอย่างการสร้าง Object จาก Class
luna = Cat("Luna", "Female", 2)
print(luna.name) # ผลลัพธ์: Luna
```

### 2. การสืบทอดและการทำงานร่วมกัน (`animal.py`)
เรียนรู้วิธีการลดความซ้ำซ้อนของโค้ด:
- **Inheritance**: คลาส `Cat` และ `Dog` สืบทอดคุณสมบัติมาจาก `Animal`
- **Method Overriding**: คลาสลูกสามารถเปลี่ยนแปลงการทำงานของเมธอด `breathe()` ให้เหมาะสมกับตัวเองได้

```python
# ตัวอย่างการ Override เมธอด
class Cat(Animal):
    def breathe(self):
        # เปลี่ยนการทำงานของคลาสแม่ (Override)
        print(f"{self.name} says: Meow!")
```

### 3. การทำ Abstraction (`abstraction.py`)
เรียนรู้การกำหนด "มาตรฐาน" ให้กับคลาส:
- **ABC (Abstract Base Class)**: คลาส `Airplane` ถูกกำหนดเป็นคลาสแม่ที่ไม่สามารถสร้างวัตถุได้โดยตรง แต่ใช้บังคับให้คลาสลูก (`Airbus`, `Boeing`) ต้องมีเมธอด `fly()` เสมอ

```python
# ตัวอย่างการใช้ Abstract Method
class Airbus(Airplane):
    def fly(self):
        print(f"Airbus {self.flight_number} is flying to {self.route}")
```

### 4. การปกป้องข้อมูล (`encapsulate.py`)
เรียนรู้การซ่อนข้อมูลเพื่อความปลอดภัย:
- **Private Variables**: ตัวแปรที่ขึ้นต้นด้วย `__` (เช่น `__salary`) จะไม่สามารถเข้าถึงได้โดยตรงจากภายนอก
- **Getter/Setter**: ใช้เมธอดในการอ่านและแก้ไขข้อมูลแทน เพื่อควบคุมความถูกต้องของข้อมูล

```python
# ตัวอย่างการใช้ Private Variable และ Getter
class HumanResource:
    def __init__(self, name, salary):
        self.__salary = salary # Private variable
    def get_salary(self):
        return self.__salary
```

### 5. การพหุสัณฐาน (`polymorphism.py`)
เรียนรู้วิธีการทำให้วัตถุต่างชนิดกันทำงานผ่านคำสั่งเดียวกันได้:
- **Polymorphism**: คลาส `Square` และ `Circle` มีเมธอด `area()` เหมือนกัน แต่มีสูตรการคำนวณที่ต่างกัน เราสามารถเรียกใช้ `area()` ผ่านตัวแปรที่เป็นประเภท `Shape` ได้โดยไม่ต้องสนใจว่าเป็นรูปทรงไหน

```python
# ตัวอย่างการใช้ Polymorphism
def print_area(shape: Shape):
    print(f"The area is: {shape.area():.2f}")

shapes = [Square(5), Circle(3)]
for s in shapes:
    print_area(s) # เรียกใช้เมธอดเดียวกัน แต่ทำงานต่างกันตามประเภทวัตถุ
```

### 6. ความสัมพันธ์ระหว่างวัตถุ ([relationship/association.py](relationship/association.py))
เรียนรู้ว่าวัตถุต่างๆ ทำงานร่วมกันอย่างไร:
- **Association**: คลาส `Professor` มีความสัมพันธ์กับ `Student` และ `Course`
- **อ่านรายละเอียดเพิ่มเติมและตัวอย่างโค้ดได้ที่: [relationship/README.md](relationship/README.md)**

### 7. หลักการ SOLID ([solid/principle.py](solid/principle.py))
ไฟล์นี้รวบรวมหลักการออกแบบที่สำคัญ 5 ประการ:
- **SRP, OCP, LSP, ISP, DIP**: หลักการที่ช่วยให้โค้ดขยายและบำรุงรักษาได้ง่าย
- **อ่านรายละเอียดเพิ่มเติมและตัวอย่างโค้ดได้ที่: [solid/README.md](solid/README.md)**

---

## 🚀 วิธีการเริ่มต้นใช้งาน

1.  **ติดตั้ง Python**: ตรวจสอบว่าเครื่องของคุณมี Python 3.x ติดตั้งอยู่
2.  **อ่านโค้ด**: เริ่มอ่านจาก `cat.py` เรียงไปจนถึง `solid/principle.py`
3.  **ลองรันโค้ด**: ใช้คำสั่งในเทอร์มินัลเพื่อดูผลลัพธ์ เช่น:
    ```bash
    python3 cat.py
    python3 animal.py
    python3 polymorphism.py
    ```
4.  **ลองแก้ไข**: ลองเพิ่ม Attributes หรือ Methods ใหม่ๆ ลงในคลาสเพื่อทดสอบความเข้าใจของคุณ

---
*จัดทำขึ้นเพื่อการศึกษาแนวคิด OOP เบื้องต้น*
