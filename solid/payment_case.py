from abc import ABC, abstractmethod

# --- Case Study: ระบบชำระเงิน (Payment System) ---
# โจทย์: พัฒนาระบบชำระเงินของร้านค้าออนไลน์ที่ต้องรองรับช่องทางที่หลากหลาย
# เช่น บัตรเครดิต, PromptPay และในอนาคตอาจจะมีคริปโต
# โดยที่ตัวประมวลผลคำสั่งซื้อ (OrderProcessor) ไม่ต้องแก้ไขโค้ดเมื่อมีวิธีชำระเงินใหม่

# 1. Abstraction (Interface)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# 2. Concrete Strategies (SRP)
class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"💳 ชำระเงินจำนวน {amount} บาท ผ่านบัตรเครดิต (Processing...)")

class PromptPayPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"📱 ชำระเงินจำนวน {amount} บาท ผ่าน PromptPay QR Code")

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"₿ ชำระเงินจำนวน {amount} บาท ผ่าน Bitcoin Wallet")

# 3. Context (High-level Module - DIP)
class OrderProcessor:
    def __init__(self, payment_method: PaymentMethod):
        # Composition & Dependency Inversion
        self.payment_method = payment_method

    def process_order(self, order_id: str, amount: float):
        print(f"\n[Order {order_id}]: กำลังประมวลผล...")
        # Delegation
        self.payment_method.pay(amount)
        print(f"[Order {order_id}]: ชำระเงินสำเร็จ!")

if __name__ == '__main__':
    print("--- 🛒 Payment System (SOLID & Strategy Pattern) ---")

    # ลูกค้าเลือกจ่ายด้วยบัตรเครดิต
    order1 = OrderProcessor(CreditCardPayment())
    order1.process_order("ORD001", 1500.00)

    # ลูกค้าเลือกจ่ายด้วย PromptPay
    order2 = OrderProcessor(PromptPayPayment())
    order2.process_order("ORD002", 250.50)

    # เพิ่ม Crypto ได้ง่ายๆ (OCP)
    order3 = OrderProcessor(CryptoPayment())
    order3.process_order("ORD003", 50000.00)

    print("\n✅ ข้อดีของการออกแบบนี้:")
    print("1. ยืดหยุ่น: เปลี่ยนวิธีจ่ายเงินได้โดยไม่ต้องแก้คลาส OrderProcessor")
    print("2. ขยายได้: เพิ่มช่องทางใหม่แค่สร้าง Class ใหม่ที่สืบทอด PaymentMethod")
    print("3. ทดสอบง่าย: สามารถใช้ Mock Payment ในการทำ Unit Test ได้")
