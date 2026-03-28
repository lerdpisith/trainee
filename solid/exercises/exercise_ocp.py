# ❌ ตัวอย่างที่ละเมิด OCP (Open/Closed Principle)
# โจทย์: หากต้องการเพิ่มส่วนลด "Premium" ต้องมาแก้ที่คลาสเดิม
# ให้ปรับปรุงโดยการใช้ Abstraction (Abstract Class) และ Polymorphism

class DiscountCalculator:
    def calculate(self, amount, customer_type):
        if customer_type == "VIP":
            return amount * 0.8  # ลด 20%
        elif customer_type == "Standard":
            return amount * 0.9  # ลด 10%
        # หากต้องการเพิ่ม "Premium" จะต้องแก้ที่นี่ (ละเมิด OCP)
        else:
            return amount

if __name__ == "__main__":
    calc = DiscountCalculator()
    print(f"VIP price: {calc.calculate(100, 'VIP')}")
    print(f"Standard price: {calc.calculate(100, 'Standard')}")
