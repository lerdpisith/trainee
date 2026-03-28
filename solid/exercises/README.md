# ✍️ แบบฝึกหัดหลักการ SOLID (SOLID Exercises)

ในไดเรกทอรีนี้จะประกอบด้วยแบบฝึกหัดที่เน้นการปรับปรุงโค้ดที่ **"ออกแบบไม่ดี"** ให้เป็นโค้ดที่ถูกต้องตามหลักการ **SOLID** โดยใช้ภาษา Python

---

## 📂 โครงสร้างแบบฝึกหัด
แบบฝึกหัดแต่ละไฟล์จะเป็นโค้ดที่ละเมิด (Violate) หลักการ SOLID อยู่ ให้ลองแก้ไฟล์เหล่านั้น:

1.  **`exercise_srp.py`**: (Single Responsibility Principle)
    *   **ปัญหา**: คลาส `Order` ทำหน้าที่คำนวณเงิน **และ** พิมพ์ใบเสร็จในคลาสเดียวกัน
    *   **โจทย์**: แยกคลาส `ReceiptPrinter` ออกมาเพื่อให้คลาส `Order` สนใจแค่เรื่องการคำนวณ (Calculation)

2.  **`exercise_ocp.py`**: (Open/Closed Principle)
    *   **ปัญหา**: คลาส `DiscountCalculator` ใช้ `if-elif` ในการตรวจสอบประเภทลูกค้า
    *   **โจทย์**: ใช้ Polymorphism โดยสร้าง Abstract Class `Discount` และ subclasses (เช่น `VIPDiscount`, `StandardDiscount`) เพื่อให้เราเพิ่มส่วนลดใหม่ได้โดยไม่ต้องแก้คลาสเดิม

3.  **`exercise_lsp.py`**: (Liskov Substitution Principle)
    *   **ปัญหา**: คลาสลูก `Ostrich` (นกกระจอกเทศ) สืบทอดมาจาก `Bird` แต่พ่น Error เมื่อเรียกใช้ `fly()`
    *   **โจทย์**: ปรับปรุงโครงสร้างคลาส (เช่น แยกคลาส `FlyingBird` และ `NonFlyingBird`) เพื่อไม่ให้คลาสลูกต้องมีพฤติกรรมที่ขัดแย้งกับคลาสแม่

4.  **`exercise_dip.py`**: (Dependency Inversion Principle)
    *   **ปัญหา**: คลาส `Register` เรียกใช้งาน `PostgreSQLDatabase` โดยตรง (High-level module depends on low-level module)
    *   **โจทย์**: สร้าง Interface (Abstract Class) ชื่อ `Database` และให้ `Register` รับคลาสที่สืบทอดมาจาก `Database` แทน

---

## ✅ วิธีการตรวจสอบ (GitHub Actions)
ในโปรเจกต์นี้มีไฟล์ `.github/workflows/solid_verify.yml` ซึ่งจะทำงานเมื่อมีการ Push โค้ดขึ้น GitHub เพื่อตรวจสอบว่าแบบฝึกหัดถูกแก้ไขอย่างถูกต้องหรือไม่

### การตรวจสอบในเครื่อง (Local Check):
คุณสามารถติดตั้ง `pytest` และรันคำสั่ง:
```bash
PYTHONPATH=. pytest solid/exercises/test_exercises.py
```

---
*คำแนะนำ: ลองอ่านคำใบ้ (Hint) ในคอมเมนต์ของแต่ละไฟล์แบบฝึกหัดก่อนเริ่มลงมือ!*
