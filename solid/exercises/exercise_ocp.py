# ตัวอย่างที่สอดคล้องกับ OCP: เพิ่มประเภทส่วนลดใหม่ได้โดยเพิ่มคลาสลูกของ Discount
# ไม่ต้องแก้ DiscountCalculator ทุกครั้งที่เพิ่มประเภท (เช่น Premium)
#
# --- สิ่งที่เปลี่ยนจากเดิม ---
# เดิม: DiscountCalculator.calculate ใช้ if / elif กับสตริง customer_type ("VIP", "Standard") — เพิ่มประเภทต้องแก้เมธอดเดิม
# แก้: นิยาม abstract Discount + คลาสลูก (VIPDiscount, StandardDiscount, PremiumDiscount)
#      DiscountCalculator รับอ็อบเจ็กต์ Discount ผ่าน __init__ แล้ว delegate ไปที่ apply() เท่านั้น
#      __main__ สร้าง DiscountCalculator(VIPDiscount()) แทนการส่งสตริงประเภทลูกค้า
from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        pass


class VIPDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount * 0.8  # ลด 20%


class StandardDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount * 0.9  # ลด 10%


class PremiumDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount * 0.85  # ลด 15%


class DiscountCalculator:
    def __init__(self, discount: Discount):
        self._discount = discount

    def calculate(self, amount: float) -> float:
        return self._discount.apply(amount)


if __name__ == "__main__":
    print(f"VIP price: {DiscountCalculator(VIPDiscount()).calculate(100)}")
    print(f"Standard price: {DiscountCalculator(StandardDiscount()).calculate(100)}")
    print(f"Premium price: {DiscountCalculator(PremiumDiscount()).calculate(100)}")
