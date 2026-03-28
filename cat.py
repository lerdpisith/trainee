class Cat:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

if __name__ == '__main__':
    # สร้าง Instance (วัตถุ) จากคลาส Cat
    luna = Cat("Luna", "Female", 2)
    oscar = Cat("Oscar", "Male", 3)

    print(f"Cat 1: {luna.name}, Gender: {luna.gender}, Age: {luna.age}")
    print(f"Cat 2: {oscar.name}, Gender: {oscar.gender}, Age: {oscar.age}")