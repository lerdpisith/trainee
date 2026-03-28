# ❌ ตัวอย่างที่ละเมิด DIP (Dependency Inversion Principle)
# โจทย์: ปรับปรุงให้ Register รับ Abstraction (เช่น Database Interface) แทน
# จะได้เปลี่ยน Database ได้โดยไม่ต้องแก้ที่ Register

class PostgreSQLDatabase:
    def save(self, data):
        print(f"Saving '{data}' to PostgreSQL Database...")

class Register:
    def __init__(self):
        # คลาส Register (High-level) ยึดติดกับ PostgreSQL (Low-level) โดยตรง
        self.db = PostgreSQLDatabase()

    def sign_up(self, user):
        self.db.save(user)

if __name__ == "__main__":
    reg = Register()
    reg.sign_up("Alice")
