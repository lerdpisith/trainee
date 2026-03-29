# ตัวอย่างที่สอดคล้องกับ LSP: ไม่บังคับ fly() ที่คลาสลูกทำตามพฤติกรรมจริงไม่ได้
# แยก FlyingBird สำหรับนกที่บินได้ — ฟังก์ชัน make_bird_fly รับเฉพาะสายพันธุ์ที่บินได้จริง
#
# --- สิ่งที่เปลี่ยนจากเดิม ---
# เดิม: Bird มี fly(); Ostrich(Bird) override fly() แล้ว raise NotImplementedError — แทนที่ Bird ใน make_bird_fly ไม่ได้
# แก้: Bird ไม่มี fly(); เพิ่ม FlyingBird(Bird) ที่มี fly(); Ostrich(Bird) ใช้ walk() แทน
#      make_bird_fly รับพารามิเตอร์เป็น FlyingBird; __main__ ไม่ส่ง Ostrich เข้า make_bird_fly


class Bird:
    """ฐานร่วมของนก — ไม่ประกาศ fly() เพื่อไม่ให้ Ostrich ต้องโกหกว่าบินได้"""
    pass


class FlyingBird(Bird):
    def fly(self):
        print("I am flying")


class Ostrich(Bird):
    def walk(self):
        print("I am walking")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


if __name__ == "__main__":
    flying = FlyingBird()
    make_bird_fly(flying)

    ostrich = Ostrich()
    ostrich.walk()
