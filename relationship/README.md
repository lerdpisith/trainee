# 📦 ความสัมพันธ์ระหว่างวัตถุ (Object Relationships)

ในไดเรกทอรีนี้จะเน้นเรื่องการทำงานร่วมกันระหว่าง Object ต่างๆ ในระบบ (Association) โดยใช้ตัวอย่างของ ระบบการศึกษา (อาจารย์, นักเรียน และวิชาเรียน)

## 📂 ไฟล์ภายในไดเรกทอรี
- `association.py`: แสดงตัวอย่างความสัมพันธ์แบบ Association, Inheritance และการใช้งาน List ของ Object

---

## 🔍 แนวคิดหลัก: Association
**Association** คือความสัมพันธ์ที่วัตถุหนึ่ง "รู้จัก" หรือ "ใช้งาน" อีกวัตถุหนึ่ง แต่ไม่ได้เป็นเจ้าของกันและกันโดยสมบูรณ์ ในที่นี้คือ:
- `Professor` (อาจารย์) มีความสัมพันธ์กับ `Student` (นักเรียน) ผ่านการสอน
- `Professor` ใช้งาน `Course` (วิชาเรียน) เพื่อส่งต่อความรู้ให้นักเรียน

---

## 💻 ตัวอย่างโค้ด (Code Example)

นี่คือตัวอย่างการใช้งานคลาสที่อยู่ใน `association.py`:

```python
from association import Student, Professor, Course

# 1. สร้างวิชาและกลุ่มของนักเรียน
math = Course("Calculus")
s1 = Student("Somchai", 20)
s2 = Student("Somsri", 21)

# 2. สร้างอาจารย์ (Professor) โดยกำหนดนักเรียนและวิชาให้
# นี่คือการทำ Association (การเชื่อมโยง Object เข้าด้วยกัน)
p_bird = Professor("Dr. Bird", 45, [s1, s2], math)

# 3. อาจารย์ทำการสอน (teach)
print("--- เริ่มทำการสอน ---")
p_bird.teach()
```

### ผลลัพธ์ที่คาดหวัง:
```text
--- เริ่มทำการสอน ---
Professor Dr. Bird is teaching Calculus
Somchai is learning Calculus
Somsri is learning Calculus
```

---

## 💡 สิ่งที่น่าสนใจในโค้ด
1. **Inheritance**: ทั้ง `Student` และ `Professor` สืบทอดมาจาก `Human` เพื่อใช้งานคุณสมบัติพื้นฐานร่วมกัน (เช่น ชื่อ และ อายุ)
2. **Composition/Aggregation**: คลาส `Professor` เก็บข้อมูล `Course` และ `List[Student]` ไว้ภายในตัว เพื่อใช้ในการทำงานร่วมกัน
3. **Inter-object Interaction**: เมธอด `teach()` ของอาจารย์ มีการเรียกใช้งานเมธอด `take_course()` ของนักเรียน แสดงถึงการสื่อสารระหว่าง Object
