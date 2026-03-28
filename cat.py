class Cat:
    name: str # field ชื่อ เพื่อสำหรับการระบุชื่อของแมว
    gender: int = 0 # field เพศ เพื่อสำหรับการระบุเพศของแมว (0 = ไม่ระบุ, 1 = ผู้ชาย, 2 = ผู้หญิง)
    age: int = 0 # field อายุ เพื่อสำหรับการระบุอายุของแมว
    def __init__(self, name: str, gender: str, age: int): # constructor เพื่อสำหรับการสร้างวัตถุแมวใหม่
        self.name = name # กำหนดค่าให้กับ field ชื่อของแมว
        self.gender = gender # กำหนดค่าให้กับ field เพศของแมว
        self.age = age # กำหนดค่าให้กับ field อายุของแมว

if __name__ == '__main__':
    # สร้าง Instance (วัตถุ) จากคลาส Cat
    luna = Cat("Luna", "Female", 2)
    oscar = Cat("Oscar", "Male", 3)

    print(f"Cat 1: {luna.name}, Gender: {luna.gender}, Age: {luna.age}")
    print(f"Cat 2: {oscar.name}, Gender: {oscar.gender}, Age: {oscar.age}")