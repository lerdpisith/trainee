class Animal:
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def run(self):
        print(f"{self.name} is running")

    def breathe(self):
        print(f"{self.name} is breathing")

class Cat(Animal):
    def breathe(self):
        # Method Overriding: เปลี่ยนจาก 'breathing' เป็น 'meow'
        print(f"{self.name} says: Meow!")

class Dog(Animal):
    def breathe(self):
        # Method Overriding: เปลี่ยนจาก 'breathing' เป็น 'bark'
        print(f"{self.name} says: Woof!")

if __name__ == '__main__':
    luna = Cat("Luna", "Female", 2)
    oscar = Dog("Oscar", "Male", 3)

    print(f"Cat: {luna.name}")
    luna.run()
    luna.breathe()

    print(f"Dog: {oscar.name}")
    oscar.run()
    oscar.breathe()