# ตัวอย่างที่สอดคล้องกับ SRP: Order ดูแลเฉพาะข้อมูล/ยอดรวม — การพิมพ์ใบเสร็จอยู่ที่ ReceiptPrinter
#
# --- สิ่งที่เปลี่ยนจากเดิม ---
# เดิม: คลาส Order ทำสองอย่าง — คำนวณยอด (calculate_total) และพิมพ์ใบเสร็จ (print_receipt) ในคลาสเดียว
# แก้: แยกคลาส ReceiptPrinter รับผิดชอบการพิมพ์; Order เหลือแค่ items + calculate_total
#      __main__ เรียก ReceiptPrinter().print_receipt(order) แทน order.print_receipt()


class Order:
    def __init__(self, items):
        self.items = items  # list ของสิ่งของที่สั่ง [('Apple', 10), ('Banana', 20)]

    def calculate_total(self):
        return sum(price for name, price in self.items)


class ReceiptPrinter:
    # ย้าย logic ที่เคยอยู่ใน Order.print_receipt มาไว้ที่นี่
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
    ReceiptPrinter().print_receipt(order)
