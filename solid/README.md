# 🛠️ หลักการออกแบบ SOLID (SOLID Principles)

ในไดเรกทอรีนี้จะรวบรวมตัวอย่างการนำหลักการ **SOLID** มาใช้ในการเขียนโปรแกรม เพื่อให้โค้ดมีความยืดหยุ่น ขยายได้ง่าย และบำรุงรักษาได้ดี

## 📂 ไฟล์ภายในไดเรกทอรี
- `principle.py`: แสดงตัวอย่างการใช้หลักการออกแบบ SOLID ในรูปแบบของ Python Code
- `notification_case.py`: Case Study ระบบแจ้งเตือน (Practical Application of SOLID & Composition)
- `payment_case.py`: Case Study ระบบชำระเงิน (Strategy Pattern & OCP)

---

## 🔍 หลักการ SOLID ทั้ง 5 ประการ

ในไฟล์ `principle.py` ได้ประยุกต์ใช้หลักการต่างๆ ดังนี้:

### 1. SRP: Single Responsibility Principle
**"หนึ่งคลาสควรมีหน้าที่รับผิดชอบเพียงอย่างเดียว"**
- คลาส `Human` ดูแลเฉพาะข้อมูลพื้นฐานส่วนบุคคล (ชื่อ, อายุ) เท่านั้น โดยไม่ไปยุ่งกับการลงทะเบียนเรียน
```python
class Human:
    def __init__(self, name): self.name = name
    def get_name(self): return self.name
    # ไม่ควรมี def save_to_db() ที่นี่
```

### 2. OCP: Open/Closed Principle
**"เปิดสำหรับการขยาย แต่ปิดสำหรับการแก้ไข"**
- คลาส `Customer` เป็น Abstract Class ที่ทำหน้าที่เป็น Interface ทำให้เราสามารถเพิ่มลูกค้าประเภทใหม่ (เช่น `V2Student`) ได้โดยไม่ต้องแก้ไขโค้ดที่เรียกใช้งาน `Customer` เดิม
```python
class Customer(ABC):
    @abstractmethod
    def register(self): pass

class Student(Customer):
    def register(self): print("Student Registering...")
```

### 3. LSP: Liskov Substitution Principle
**"คลาสลูกต้องสามารถใช้งานแทนคลาสแม่ได้เสมอ"**
- ทั้ง `Student` และ `V2Student` สามารถถูกส่งเข้าไปใน `RegisterManager` ได้เหมือนกัน เพราะทั้งคู่ทำตามข้อกำหนดของ `Customer`
```python
def process_register(customer: Customer):
    customer.register() # ใส่ Student หรือ V2Student ก็ทำงานได้เหมือนกัน
```

### 4. DIP: Dependency Inversion Principle
**"ควรยึดติดกับ Abstraction (Interface) ไม่ใช่คลาสที่ทำงานเฉพาะเจาะจง"**
- คลาส `RegisterManager` รับค่าเป็น `Customer` (Abstraction) แทนที่จะรับเฉพาะ `Student` (Concrete class) ทำให้มันสามารถจัดการลูกค้าได้ทุกประเภทที่สืบทอดมาจาก `Customer`
```python
class RegisterManager:
    def __init__(self, customer: Customer):
        self.customer = customer # ยึดติดกับ Interface
```

---

## 🏗️ Case Study: ระบบแจ้งเตือน (`notification_case.py`)

ตัวอย่างการนำ SOLID มาประยุกต์ใช้ร่วมกันในระบบเดียว เพื่อให้เห็นภาพการทำงานจริง:

### โจทย์:
เราต้องการระบบส่งการแจ้งเตือนที่รองรับ Email, SMS และสามารถเพิ่มช่องทางใหม่ๆ (เช่น Line) ได้ในอนาคตโดยไม่กระทบโค้ดเดิม

### การออกแบบ:
- **`NotificationChannel` (Interface)**: กำหนดมาตรฐานการส่งข้อความ
- **`EmailNotification`, `SMSNotification`**: แต่ละคลาสรับผิดชอบช่องทางตัวเอง (**SRP**)
- **`NotificationService`**:
    - ใช้ **Composition** เพื่อบรรจุช่องทางที่ต้องการ
    - ยึดติดกับ Interface แทน Concrete Class (**DIP**)
    - สามารถเปลี่ยนช่องทางได้ขณะรันไทม์ (**Runtime Flexibility**)
    - เพิ่มช่องทางใหม่ได้ทันทีโดยไม่ต้องแก้โค้ด Service เดิม (**OCP**)

```python
# ตัวอย่างการใช้งานจริง
email_service = NotificationService(EmailNotification())
email_service.notify("Hello!", "user@email.com")

# สลับเป็น SMS ได้ทันที
email_service.set_channel(SMSNotification())
email_service.notify("OTP: 1234", "081-xxx-xxxx")
```

---

## 💳 Case Study: ระบบชำระเงิน (`payment_case.py`)

ใช้ **Strategy Pattern** ร่วมกับ **SOLID** เพื่อสร้างระบบชำระเงินที่ยืดหยุ่น:

- **`PaymentMethod` (Interface)**: สัญญา (Contract) ว่าทุกวิธีจ่ายเงินต้องมีเมธอด `pay()`
- **`CreditCard`, `PromptPay`, `Crypto`**: แต่ละคลาสมี Logic การจ่ายเงินต่างกัน (**Polymorphism**)
- **`OrderProcessor`**: ไม่ต้องรู้ว่าลูกค้าจ่ายด้วยอะไร แค่เรียก `payment_method.pay()` (**Delegation**)

```python
# เพิ่ม CryptoPayment ได้โดยไม่ต้องแก้ OrderProcessor (OCP)
order = OrderProcessor(CryptoPayment())
order.process_order("ORD001", 5000.0)
```

---

## ⚖️ การเปรียบเทียบ Interface vs Abstract Class

ในการออกแบบซอฟต์แวร์ การเลือกใช้ระหว่าง Interface และ Abstract Class มีผลต่อความยืดหยุ่นของระบบ:

### 1. อินเทอร์เฟซ (Interface)
มุ่งเน้นไปที่ **พฤติกรรม (Behavior)** และการทำสัญญา (Contract)
- ✅ **ข้อดี**:
    - **Multiple Implementation**: หนึ่งคลาสสามารถทำตามหลายสัญญาได้พร้อมกัน
    - **Interface Segregation**: สามารถแบ่งอินเทอร์เฟซใหญ่ๆ ออกเป็นส่วนย่อยๆ ที่เฉพาะเจาะจงได้
- ❌ **ข้อเสีย**:
    - **ไม่มีสถานะ (No State)**: ไม่สามารถประกาศฟิลด์หรือตัวแปรเพื่อเก็บข้อมูลในอินเทอร์เฟซได้

### 2. คลาสนามธรรม (Abstract Class)
มุ่งเน้นไปที่ **โครงสร้างพื้นฐาน (Base Template)** และการนำโค้ดกลับมาใช้ใหม่
- ✅ **ข้อดี**:
    - **Code Reuse**: สามารถมีทั้งฟิลด์ (State) และเมธอดพื้นฐาน (Behavior) ให้คลาสลูกนำไปใช้ได้ทันที
- ❌ **ข้อเสีย**:
    - **Single Inheritance**: สืบทอดได้เพียงคลาสเดียวเท่านั้น
    - **Unnecessary Implementation**: คลาสลูกถูกบังคับให้ต้อง Implement เมธอดนามธรรมทั้งหมด แม้จะไม่ได้ใช้งาน
    - **Tight Coupling**: การเปลี่ยนแปลงในคลาสแม่ส่งผลกระทบต่อคลาสลูกอย่างรุนแรง

> **สรุป**: ใช้ **Interface** เมื่อต้องการกำหนดความสามารถที่หลากหลายและยืดหยุ่น และใช้ **Abstract Class** เมื่อต้องการสร้างแม่แบบพื้นฐานเพื่อลดความซ้ำซ้อนของโค้ดในกลุ่มวัตถุที่ใกล้เคียงกัน

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
