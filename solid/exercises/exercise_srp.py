# ✅ แก้ไขแล้ว: ปฏิบัติตามหลักการ SRP (Single Responsibility Principle)
# แต่ละคลาสมีหน้าที่รับผิดชอบเพียงอย่างเดียว

class Order:
    """
    รับผิดชอบเฉพาะ: ข้อมูลการสั่งซื้อ และการคำนวณ (Calculation)
    """
    def __init__(self, items):
        self.items = items  # list ของสิ่งของที่สั่ง [('Apple', 10), ('Banana', 20)]

    def calculate_total(self):
        return sum(price for name, price in self.items)


class ReceiptPrinter:
    """
    รับผิดชอบเฉพาะ: การพิมพ์ใบเสร็จ (Printing Responsibility)
    """
    def print_receipt(self, order: Order):
        total = order.calculate_total()
        print("--- Receipt ---")
        for name, price in order.items:
            print(f"{name}: {price}")
        print(f"Total: {total}")
        print("---------------")


if __name__ == "__main__":
    items = [('Apple', 10), ('Banana', 20)]
    order = Order(items)

    printer = ReceiptPrinter()
    printer.print_receipt(order)