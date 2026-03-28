class HumanResource:
    def __init__(self, name: str, salary: int):
        self.name = name
        # Private Variable: เก็บเป็นความลับ ไม่ให้แก้ไขโดยตรงจากภายนอก
        self.__salary = salary

    def get_salary(self):
        # Getter: วิธีการขอดูเงินเดือนอย่างปลอดภัย
        return self.__salary

    def set_salary(self, new_salary: int):
        # Setter: วิธีการปรับเงินเดือน พร้อมตรวจสอบความถูกต้อง
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Error: Salary must be positive!")

if __name__ == '__main__':
    hr = HumanResource("Alice", 50000)
    
    # พยายามเข้าถึงโดยตรงจะ Error (ถ้าเป็น __salary)
    # print(hr.__salary) # AttributeError
    
    print(f"Name: {hr.name}")
    print(f"Original Salary: {hr.get_salary()}")

    hr.set_salary(55000)
    print(f"New Salary: {hr.get_salary()}")

    hr.set_salary(-1000) # ทดสอบเงื่อนไขผิดพลาด

