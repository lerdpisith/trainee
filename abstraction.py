from abc import ABC, abstractmethod

# --- 🛰️ แนวคิดของการนามธรรม (Abstraction) ในเชิงลึก ---
# อ็อบเจกต์ในโปรแกรมไม่จำเป็นต้องเป็นตัวแทนของสิ่งที่มีอยู่ในโลกความเป็นจริงด้วยความแม่นยำ 100%
# แต่เราควรจำลองเฉพาะคุณลักษณะ (Attributes) และพฤติกรรม (Behaviors) ที่สำคัญ
# ใน "บริบทที่เฉพาะเจาะจง" (Specific Context) เท่านั้น และละทิ้งรายละเอียดที่ไม่เกี่ยวข้องออกไป

# ตัวอย่าง: คลาส Airplane ใน 2 บริบทที่แตกต่างกัน

# --- 1. บริบท: แอปพลิเคชันจำลองการบิน (Flight Simulator Application) ---
# ในบริบทนี้ เราสนใจการควบคุมเครื่องบินและพฤติกรรมทางการบินจริงๆ
class SimulatorAirplane(ABC):
    def __init__(self, model: str, speed: float, altitude: float):
        self.model = model
        self.speed = speed
        self.altitude = altitude
        # รายละเอียดที่สำคัญ: มุมการบิน (Pitch)
        self.pitch = 0.0

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def change_altitude(self, new_altitude: float):
        pass

# --- 2. บริบท: แอปพลิเคชันจองตั๋วเครื่องบิน (Flight Booking Application) ---
# ในบริบทนี้ เราไม่สนใจว่าเครื่องบินจะบินอย่างไร แต่สนใจแค่ "ใครนั่งตรงไหน" และ "จองได้ไหม"
class BookingAirplane(ABC):
    def __init__(self, flight_number: str, seating_map: dict):
        self.flight_number = flight_number
        self.seating_map = seating_map  # เช่น {"A1": True, "A2": False}

    @abstractmethod
    def check_availability(self, seat_number: str):
        pass

    @abstractmethod
    def reserve_seat(self, seat_number: str):
        pass

# --- ส่วนของการนำไปใช้งาน (Implementation) ---

class AirbusA320Simulator(SimulatorAirplane):
    def fly(self):
        print(f"Airbus {self.model} is cruising at {self.speed} km/h, altitude: {self.altitude} ft.")

    def change_altitude(self, new_altitude: float):
        self.altitude = (self.altitude + new_altitude) / 2 # simplified change
        self.altitude = new_altitude
        print(f"Changing altitude to {self.altitude} ft...")

class AirbusA320Booking(BookingAirplane):
    def check_availability(self, seat_number: str):
        available = self.seating_map.get(seat_number, False)
        status = "Available" if available else "Reserved"
        print(f"Seat {seat_number} on flight {self.flight_number} is {status}.")

    def reserve_seat(self, seat_number: str):
        if self.seating_map.get(seat_number):
            self.seating_map[seat_number] = False
            print(f"Successfully reserved seat {seat_number}.")
        else:
            print(f"Seat {seat_number} is already taken!")

if __name__ == '__main__':
    print("--- ✈️ Abstraction ในบริบทที่ต่างกัน ---")

    print("\n[ บริบท: Flight Simulator ]")
    sim_plane = AirbusA320Simulator("A320", 850, 35000)
    sim_plane.fly()
    sim_plane.change_altitude(38000)

    print("\n[ บริบท: Flight Booking ]")
    booking_plane = AirbusA320Booking("FD123", {"1A": True, "1B": False, "1C": True})
    booking_plane.check_availability("1A")
    booking_plane.check_availability("1B")
    booking_plane.reserve_seat("1A")

    print("\n✅ สรุป: Abstraction ช่วยให้เรามุ่งเน้นเฉพาะ 'สิ่งที่จำเป็นต่อปัญหา' ในแอปพลิเคชันนั้นๆ")
    print("โดยไม่ต้องนำความซับซ้อนทั้งหมดของโลกความเป็นจริงมาใส่ในโค้ด")