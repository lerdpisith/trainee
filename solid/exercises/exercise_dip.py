# ตัวอย่างที่สอดคล้องกับ DIP (Dependency Inversion Principle)
# High-level (Register) ขึ้นกับ abstraction (Database) ไม่สร้าง concrete DB ภายในคลาส
#
# --- สิ่งที่เปลี่ยนจากเดิม ---
# เดิม: Register.__init__ สร้าง PostgreSQLDatabase() เอง — ผูกติด concrete class
# แก้: นิยาม abstract Database + PostgreSQLDatabase สืบทอด; Register(db) รับ DB ทาง constructor (DI)
#      __main__ สร้าง Register(PostgreSQLDatabase()) ภายนอกคลาส Register
from abc import ABC, abstractmethod


# Interface ระดับ abstraction — กำหนดว่า "ที่เก็บข้อมูล" ต้องทำอะไรได้
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


# Implementation ระดับต่ำ — หนึ่งในหลายชนิดของ Database (แลกเป็น PostgreSQL ได้โดยไม่แก้ Register)
class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving '{data}' to PostgreSQL Database...")


class Register:
    def __init__(self, db: Database):
        # Dependency injection: รับ DB จากภายนอก ไม่ new PostgreSQLDatabase() ในที่นี่
        self.db = db

    def sign_up(self, user):
        self.db.save(user)


if __name__ == "__main__":
    # composition root: จุดเดียวที่ผูกกับ concrete class (อยากเปลี่ยน DB แก้แค่ตรงนี้หรือส่งคนละ instance)
    reg = Register(PostgreSQLDatabase())
    reg.sign_up("Alice")
