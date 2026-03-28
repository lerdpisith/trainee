# ❌ ตัวอย่างที่ละเมิด SRP (Single Responsibility Principle)
# โจทย์: ปรับปรุงโค้ดนี้โดยแยกคลาส ReceiptPrinter ออกมา และให้ Order ดูแลเฉพาะข้อมูลการสั่งซื้อ

class Order:
    def __init__(self, items):
        self.items = items  # list ของสิ่งของที่สั่ง [('Apple', 10), ('Banana', 20)]

    def calculate_total(self):
        return sum(price for name, price in self.items)

    # ฟังก์ชันนี้ทำให้ Order มีหน้าที่ "เกิน" ขอบเขต (Printing Responsibility)
    # ควรย้ายส่วนนี้ไปไว้ในคลาสใหม่!
    def print_receipt(self):
        total = self.calculate_total()
        print("--- Receipt ---")
        for name, price in self.items:
            print(f"{name}: {price}")
        print(f"Total: {total}")
        print("---------------")

if __name__ == "__main__":
    items = [('Apple', 10), ('Banana', 20)]
    order = Order(items)
    order.print_receipt()
