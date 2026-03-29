class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(price for name, price in self.items)


class ReceiptPrinter:
    def print_receipt(self, order):
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