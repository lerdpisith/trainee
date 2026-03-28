# ❌ ตัวอย่างที่ละเมิด LSP (Liskov Substitution Principle)
# โจทย์: ปรับปรุงการออกแบบเพื่อไม่ให้คลาสลูก (Ostrich) ต้องโยน Error
# เพราะคลาสแม่ Bird สั่งให้ fly() ได้ แต่นกกระจอกเทศบินไม่ได้

class Bird:
    def fly(self):
        print("I am flying")

class Ostrich(Bird):
    def fly(self):
        # ละเมิด LSP: คลาสลูกไม่สามารถทำงานแทนคลาสแม่ได้ (บินไม่ได้)
        raise NotImplementedError("Ostriches cannot fly")

def make_bird_fly(bird: Bird):
    bird.fly()

if __name__ == "__main__":
    my_bird = Bird()
    make_bird_fly(my_bird)

    # ตรงนี้จะ Error! เพราะ Ostrich ไม่สามารถทำงานแทน Bird ได้สมบูรณ์
    ostrich = Ostrich()
    make_bird_fly(ostrich)
