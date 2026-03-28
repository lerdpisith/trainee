from abc import ABC, abstractmethod

# --- Case Study: ระบบแจ้งเตือน (Notification System) ---
# โจทย์: เราต้องการสร้างระบบที่สามารถส่งการแจ้งเตือนหาผู้ใช้ได้หลายช่องทาง 
# เช่น Email, SMS และในอนาคตอาจจะมี Line หรือ Telegram
# โดยที่ตัวระบบหลัก (NotificationService) ไม่ควรต้องแก้ไขโค้ดทุกครั้งที่เพิ่มช่องทางใหม่

# 1. กำหนด Abstraction (Interface) - ตามหลัก DIP และ OCP
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str, receiver: str):
        pass

# 2. สร้างช่องทางต่างๆ (Concrete Classes) - ตามหลัก SRP
class EmailNotification(NotificationChannel):
    def send(self, message: str, receiver: str):
        print(f"📧 ส่ง Email ไปยัง {receiver}: {message}")

class SMSNotification(NotificationChannel):
    def send(self, message: str, receiver: str):
        print(f"💬 ส่ง SMS ไปยัง {receiver}: {message}")

# หากต้องการเพิ่มช่องทางใหม่ แค่สร้างคลาสใหม่ (Open for Extension) - ตามหลัก OCP
class LineNotification(NotificationChannel):
    def send(self, message: str, receiver: str):
        print(f"🟢 ส่ง Line Message ไปยัง {receiver}: {message}")

# 3. ระบบหลักที่ใช้งาน (High-level Module) - ตามหลัก DIP และ Composition
class NotificationService:
    def __init__(self, channel: NotificationChannel):
        # รับ Interface (Abstraction) เข้ามาประกอบ (Composition)
        # ไม่ยึดติดกับ Class ใดคลาสหนึ่งโดยเฉพาะ (Dependency Inversion)
        self.channel = channel

    def set_channel(self, channel: NotificationChannel):
        # สามารถเปลี่ยนช่องทางได้ขณะรันไทม์ (Runtime Flexibility)
        self.channel = channel

    def notify(self, message: str, receiver: str):
        self.channel.send(message, receiver)

if __name__ == '__main__':
    print("--- 🔔 Notification System (SOLID Case Study) ---")

    # 1. เริ่มต้นด้วยการส่งทาง Email
    email_service = NotificationService(EmailNotification())
    email_service.notify("ยินดีต้อนรับสู่บทเรียน OOP!", "user@example.com")

    # 2. เปลี่ยนช่องทางเป็น SMS (Runtime Flexibility)
    email_service.set_channel(SMSNotification())
    email_service.notify("รหัส OTP ของคุณคือ 123456", "081-234-5678")

    # 3. เพิ่มช่องทางใหม่ (Line) โดยไม่ต้องแก้คลาส NotificationService เลย
    line_notifier = NotificationService(LineNotification())
    line_notifier.notify("ประกาศวันหยุดสงกรานต์", "@line_user")

    print("\n✅ สรุปหลักการที่ใช้:")
    print("- SRP: แต่ละคลาส (Email, SMS) ทำหน้าที่ส่งข้อความในรูปแบบของตัวเองเท่านั้น")
    print("- OCP: เพิ่ม LineNotification ได้โดยไม่ต้องแก้ไข NotificationService")
    print("- LSP: ทุกช่องทางส่งข้อความผ่านเมธอด send() ได้เหมือนกัน")
    print("- DIP: NotificationService ยึดติดกับ NotificationChannel (Interface) แทนที่จะเป็นคลาสส่งเมล์โดยตรง")
