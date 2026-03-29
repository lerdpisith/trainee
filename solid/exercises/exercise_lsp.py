# ✅ แก้ไขแล้ว: ปฏิบัติตามหลักการ LSP (Liskov Substitution Principle)
# "คลาสลูกต้องสามารถใช้แทนคลาสแม่ได้เสมอ โดยไม่ทำให้โปรแกรมพัง"
# Pattern ที่ใช้: Interface Segregation + Class Hierarchy Redesign

from abc import ABC, abstractmethod


# --- Step 1: แยก Abstraction ตามความสามารถที่ "แชร์กันได้จริง" ---

class Bird(ABC):
    """
    Base class: สิ่งที่นกทุกตัวทำได้จริง (ไม่บังคับให้บิน)
    """
    @abstractmethod
    def make_sound(self) -> None:
        pass


# --- Step 2: แยก interface "การบิน" ออกมาต่างหาก ---

class Flyable(ABC):
    """
    Mixin interface: ติดให้เฉพาะนกที่บินได้จริงๆ เท่านั้น
    """
    @abstractmethod
    def fly(self) -> None:
        pass


# --- Step 3: คลาสลูก inherit เฉพาะสิ่งที่ตัวเองทำได้จริง ---

class Sparrow(Bird, Flyable):
    """นกกระจอก: บินได้ ✅"""
    def make_sound(self) -> None:
        print("Sparrow: Tweet tweet!")

    def fly(self) -> None:
        print("Sparrow: Flap flap... I'm flying!")


class Eagle(Bird, Flyable):
    """นกอินทรี: บินได้ ✅"""
    def make_sound(self) -> None:
        print("Eagle: Screech!")

    def fly(self) -> None:
        print("Eagle: Soaring high in the sky!")


class Ostrich(Bird):
    """นกกระจอกเทศ: บินไม่ได้ → ไม่ต้อง inherit Flyable เลย ✅"""
    def make_sound(self) -> None:
        print("Ostrich: Boom boom!")

    def run(self) -> None:
        print("Ostrich: Running at 70 km/h!")


# --- Step 4: ฟังก์ชันรับ type ที่ถูกต้อง ไม่เกิด Error อีกต่อไป ---

def make_bird_sound(bird: Bird) -> None:
    """ทุก Bird ทำได้ → ปลอดภัย 100%"""
    bird.make_sound()

def make_bird_fly(bird: Flyable) -> None:
    """รับเฉพาะ Flyable → LSP ไม่ถูกละเมิดแน่นอน"""
    bird.fly()


if __name__ == "__main__":
    birds = [Sparrow(), Eagle(), Ostrich()]

    print("=== ทุกตัวส่งเสียงได้ (Bird) ===")
    for bird in birds:
        make_bird_sound(bird)

    print("\n=== เฉพาะตัวที่บินได้ (Flyable) ===")
    for bird in birds:
        if isinstance(bird, Flyable):
            make_bird_fly(bird)

    print("\n=== นกกระจอกเทศวิ่งแทน ===")
    ostrich = Ostrich()
    ostrich.run()