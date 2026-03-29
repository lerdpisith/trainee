# ✅ แก้ไขแล้ว: ปฏิบัติตามหลักการ OCP (Open/Closed Principle)
# "Open for Extension, Closed for Modification"
# → เพิ่ม discount type ใหม่ได้ โดยไม่ต้องแก้โค้ดเดิมเลย
# แก้ปัญหาด้วย Strategy Pattern + OCP

from abc import ABC, abstractmethod


# --- Abstraction Layer ---
class DiscountStrategy(ABC):
    """
    Abstract base class: กำหนด "สัญญา" ว่าทุก discount ต้องมี calculate()
    """
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


# --- Concrete Strategies (เพิ่มได้เรื่อยๆ โดยไม่แตะโค้ดเดิม) ---
class VIPDiscount(DiscountStrategy):
    """ลด 20%"""
    def calculate(self, amount: float) -> float:
        return amount * 0.8


class StandardDiscount(DiscountStrategy):
    """ลด 10%"""
    def calculate(self, amount: float) -> float:
        return amount * 0.9


class NoDiscount(DiscountStrategy):
    """ไม่มีส่วนลด"""
    def calculate(self, amount: float) -> float:
        return amount


# ✅ เพิ่ม Premium ใหม่ได้เลย โดยไม่แตะคลาสไหนเดิมเลย!
class PremiumDiscount(DiscountStrategy):
    """ลด 30%"""
    def calculate(self, amount: float) -> float:
        return amount * 0.7


# --- Calculator: ปิดการแก้ไข (Closed for Modification) ---
class DiscountCalculator:
    """
    รับ strategy เข้ามา → ไม่มี if/elif อีกต่อไป
    ไม่ว่าจะเพิ่ม discount ใหม่กี่แบบ คลาสนี้ไม่เปลี่ยนเลย
    """
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        return self.strategy.calculate(amount)


if __name__ == "__main__":
    amount = 100

    scenarios = [
        ("VIP",      VIPDiscount()),
        ("Standard", StandardDiscount()),
        ("Normal",   NoDiscount()),
        ("Premium",  PremiumDiscount()),   # ← เพิ่มใหม่ ไม่แตะโค้ดเดิมเลย!
    ]

    for label, strategy in scenarios:
        calc = DiscountCalculator(strategy)
        print(f"{label:10} price: {calc.calculate(amount):.2f}")