# 🛠️ หลักการออกแบบ SOLID (SOLID Principles)

ในไดเรกทอรีนี้จะรวบรวมตัวอย่างการนำหลักการ **SOLID** มาใช้ในการเขียนโปรแกรม เพื่อให้โค้ดมีความยืดหยุ่น ขยายได้ง่าย และบำรุงรักษาได้ดี

## 📂 ไฟล์ภายในไดเรกทอรี
- `principle.py`: แสดงตัวอย่างการใช้หลักการออกแบบ SOLID ในรูปแบบของ Python Code

---

## 🔍 หลักการ SOLID ทั้ง 5 ประการ

ในไฟล์ `principle.py` ได้ประยุกต์ใช้หลักการต่างๆ ดังนี้:

### 1. SRP: Single Responsibility Principle
**"หนึ่งคลาสควรมีหน้าที่รับผิดชอบเพียงอย่างเดียว"**
- คลาส `Human` ดูแลเฉพาะข้อมูลพื้นฐานส่วนบุคคล (ชื่อ, อายุ) เท่านั้น โดยไม่ไปยุ่งกับการลงทะเบียนเรียน

### 2. OCP: Open/Closed Principle
**"เปิดสำหรับการขยาย แต่ปิดสำหรับการแก้ไข"**
- คลาส `Customer` เป็น Abstract Class ที่ทำหน้าที่เป็น Interface ทำให้เราสามารถเพิ่มลูกค้าประเภทใหม่ (เช่น `V2Student`) ได้โดยไม่ต้องแก้ไขโค้ดที่เรียกใช้งาน `Customer` เดิม

### 3. LSP: Liskov Substitution Principle
**"คลาสลูกต้องสามารถใช้งานแทนคลาสแม่ได้เสมอ"**
- ทั้ง `Student` และ `V2Student` สามารถถูกส่งเข้าไปใน `RegisterManager` ได้เหมือนกัน เพราะทั้งคู่ทำตามข้อกำหนดของ `Customer`

### 4. DIP: Dependency Inversion Principle
**"ควรยึดติดกับ Abstraction (Interface) ไม่ใช่คลาสที่ทำงานเฉพาะเจาะจง"**
- คลาส `RegisterManager` รับค่าเป็น `Customer` (Abstraction) แทนที่จะรับเฉพาะ `Student` (Concrete class) ทำให้มันสามารถจัดการลูกค้าได้ทุกประเภทที่สืบทอดมาจาก `Customer`

---

## 💻 ตัวอย่างโค้ด (Code Example)

นี่คือตัวอย่างการใช้งานคลาสที่อยู่ใน `principle.py`:

```python
from principle import Student, V2Student, RegisterManager
from relationship.association import Course

# 1. เตรียมข้อมูลวิชาเรียน
math = Course("Math 101")

# 2. สร้างนักเรียน (ทั้งแบบธรรมดา และแบบ V2)
beginner = Student()
expert = V2Student()

# 3. ใช้ RegisterManager จัดการ (Dependency Inversion & Liskov Substitution)
# ไม่ว่าจะเป็น Student หรือ V2Student เราก็ใช้ RegisterManager ตัวเดียวกันจัดการได้
manager_1 = RegisterManager(beginner)
manager_2 = RegisterManager(expert)

manager_1.register_course(math)
manager_2.register_course(math)

print(f"Alice's courses: {[c.name for c in beginner.courses]}")
print(f"Bob's courses: {[c.name for c in expert.courses]}")
```

### ผลลัพธ์ที่คาดหวัง:
```text
Student enrolled in: Math 101
V2Student enrolled in: Math 101
Alice's courses: ['Math 101']
Bob's courses: ['Math 101']
```
