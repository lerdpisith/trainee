class Shape:
    def area(self):
        # เมธอดแม่ที่คลาสลูกจะนำไป Override
        pass

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        # Polymorphism: การ Override เมธอด area สำหรับสี่เหลี่ยม
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        # Polymorphism: การ Override เมธอด area สำหรับวงกลม
        import math
        return math.pi * (self.radius ** 2)

def print_area(shape: Shape):
    # ฟังก์ชันนี้แสดงถึง Polymorphism: มันรับ Object ประเภทใดก็ได้ที่เป็น Shape
    # และเรียกใช้เมธอด area() โดยไม่สนใจว่าข้างในจะเป็นสี่เหลี่ยมหรือวงกลม
    print(f"The area is: {shape.area():.2f}")

if __name__ == '__main__':
    shapes = [Square(5), Circle(3)]
    
    print("--- Polymorphism in Action ---")
    for s in shapes:
        print_area(s)
