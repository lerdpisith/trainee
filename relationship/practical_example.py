from abc import ABC, abstractmethod
from typing import List

# --- 5. Implementation (Interface) ---
# กำหนดมาตรฐานให้ทุกคนที่ทำงานในโรงพยาบาล
class Staff(ABC):
    @abstractmethod
    def work(self):
        pass

# --- 1. Dependency ---
# บริการสั่งยา (PharmacyService) เป็นสิ่งที่หมอเรียกใช้ชั่วคราวตอนสั่งยา
class PharmacyService:
    def process_order(self, doctor_name: str, medicine: str):
        print(f"[Pharmacy]: Processing order for '{medicine}' requested by Dr. {doctor_name}")

# --- 6. Inheritance ---
# หมอทั่วไป (Doctor) เป็นคลาสพื้นฐาน
class Doctor(Staff):
    def __init__(self, name: str):
        self.name = name
        # --- 2. Association ---
        # หมอรู้จักคนไข้ (Patient) เชื่อมโยงกันผ่านฟิลด์ (List of patients)
        self.patients: List['Patient'] = []

    def work(self):
        print(f"Dr. {self.name} is checking patients...")

    def order_medicine(self, medicine: str, pharmacy: PharmacyService):
        # PharmacyService ถูกส่งเข้ามาเป็น parameter (Dependency)
        pharmacy.process_order(self.name, medicine)

# หมอผ่าตัด (Surgeon) สืบทอดจาก Doctor
class Surgeon(Doctor):
    def work(self):
        # Override เมธอดเดิมจาก Doctor
        print(f"Dr. {self.name} is performing surgery...")

# --- 2. Association ---
class Patient:
    def __init__(self, name: str):
        self.name = name
        # คนไข้ก็รู้จักหมอเจ้าของไข้
        self.primary_doctor = None

# --- 4. Composition (Whole-Part: แข็งแกร่ง) ---
# แผนกฉุกเฉิน (EmergencyRoom) เป็นส่วนหนึ่งของโรงพยาบาลและสลายไปพร้อมโรงพยาบาล
class EmergencyRoom:
    def __init__(self, capacity: int):
        self.capacity = capacity

# --- 3. Aggregation (Whole-Part: อ่อนโยน) ---
# โรงพยาบาล (Hospital) ประกอบด้วยหมอหลายคน
# แต่หมอยังสามารถดำรงอยู่ได้แม้ไม่มีโรงพยาบาลนี้ (ย้ายไปที่อื่น)
class Hospital:
    def __init__(self, name: str):
        self.name = name
        # Aggregation: เก็บ List ของ Doctor
        self.doctors: List[Doctor] = []
        # Composition: โรงพยาบาลสร้าง ER ขึ้นมาเอง (Internal life cycle management)
        self.er_unit = EmergencyRoom(capacity=10)

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)

    def status(self):
        print(f"Hospital: {self.name}")
        print(f"- ER Capacity: {self.er_unit.capacity}")
        print(f"- Doctors: {[d.name for d in self.doctors]}")

if __name__ == '__main__':
    print("🏥 --- จำลองระบบโรงพยาบาล (Hospital System Simulation) ---")
    
    # 1. สร้างโรงพยาบาล
    hospital = Hospital("City Central Hospital")
    
    # 2. สร้างหมอ (และหมอผ่าตัด)
    dr_smith = Doctor("Smith")
    dr_jones = Surgeon("Jones") # Inheritance
    
    # 3. เพิ่มหมอเข้าโรงพยาบาล (Aggregation)
    hospital.add_doctor(dr_smith)
    hospital.add_doctor(dr_jones)
    
    # 4. สร้างคนไข้และเชื่อมโยงกับหมอ (Association)
    alice = Patient("Alice")
    alice.primary_doctor = dr_smith
    dr_smith.patients.append(alice)
    
    # 5. หมอสั่งยา (Dependency)
    pharmacy = PharmacyService()
    dr_smith.order_medicine("Aspirin", pharmacy)
    
    # 6. ทุกคนทำงานตามหน้าที่ (Implementation & Polymorphism)
    staff_members: List[Staff] = [dr_smith, dr_jones]
    for staff in staff_members:
        staff.work()
    
    # 7. ตรวจสอบสถานะโรงพยาบาล
    print("\n📊 --- Hospital Summary ---")
    hospital.status()
