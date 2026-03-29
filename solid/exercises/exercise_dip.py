# ✅ แก้ไขแล้ว: ปฏิบัติตามหลักการ DIP (Dependency Inversion Principle)
# "High-level modules ไม่ควรขึ้นตรงกับ Low-level modules
#  ทั้งคู่ควรขึ้นกับ Abstraction แทน"
# Pattern ที่ใช้: Dependency Injection + Abstract Interface

from abc import ABC, abstractmethod


# --- Step 1: สร้าง Abstraction (Interface) ที่ทั้งคู่จะขึ้นอยู่กับมัน ---

class Database(ABC):
    """
    Abstraction layer: กำหนด "สัญญา" ว่า database ทุกตัวต้องมี save()
    ทั้ง Register (high-level) และ PostgreSQL/MySQL (low-level) ขึ้นกับตัวนี้
    """
    @abstractmethod
    def save(self, data: str) -> None:
        pass


# --- Step 2: Low-level modules implement จาก Abstraction ---

class PostgreSQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"[PostgreSQL] Saving '{data}'...")


class MySQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"[MySQL] Saving '{data}'...")


class MongoDBDatabase(Database):
    def save(self, data: str) -> None:
        print(f"[MongoDB] Saving '{data}' as document...")


# ทดสอบ: Mock database สำหรับ Unit Test (ไม่ต้องแตะ Register เลย!)
class MockDatabase(Database):
    def __init__(self):
        self.saved_data = []

    def save(self, data: str) -> None:
        self.saved_data.append(data)
        print(f"[Mock] Captured '{data}' (no real DB needed)")


# --- Step 3: High-level module รับ Abstraction ผ่าน Constructor Injection ---

class Register:
    """
    Register ไม่รู้จัก PostgreSQL, MySQL หรือ MongoDB โดยตรงอีกต่อไป
    รู้จักแค่ Database interface → เปลี่ยน DB ได้โดยไม่แตะ Register เลย
    """
    def __init__(self, db: Database):   # ← รับ Abstraction แทน Concrete class
        self.db = db

    def sign_up(self, user: str) -> None:
        print(f"Registering user: {user}")
        self.db.save(user)


if __name__ == "__main__":
    print("=== ใช้ PostgreSQL ===")
    reg = Register(db=PostgreSQLDatabase())
    reg.sign_up("Alice")

    print("\n=== เปลี่ยนเป็น MySQL (ไม่แตะ Register เลย!) ===")
    reg = Register(db=MySQLDatabase())
    reg.sign_up("Bob")

    print("\n=== เปลี่ยนเป็น MongoDB (ไม่แตะ Register เลย!) ===")
    reg = Register(db=MongoDBDatabase())
    reg.sign_up("Charlie")

    print("\n=== Unit Test ด้วย MockDatabase ===")
    mock_db = MockDatabase()
    reg = Register(db=mock_db)
    reg.sign_up("TestUser")
    assert "TestUser" in mock_db.saved_data
    print(f"Test passed! Saved data: {mock_db.saved_data}")