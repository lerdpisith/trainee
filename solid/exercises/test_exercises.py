import pytest
import inspect
from abc import ABC

# Test SRP
def test_srp_exercise():
    from solid.exercises import exercise_srp
    # ตรวจสอบว่ามีคลาส ReceiptPrinter แยกออกมาจริงหรือไม่
    assert hasattr(exercise_srp, 'ReceiptPrinter'), "ควรสร้างคลาส ReceiptPrinter แยกออกมา"
    
    # ตรวจสอบว่า Order ยังมี calculate_total อยู่
    order = exercise_srp.Order([('Test', 10)])
    assert order.calculate_total() == 10
    
    # ตรวจสอบว่า Order ไม่ควรมี logic การพิมพ์ Receipt อยู่ในตัว (หรือควรจะ delegate ไปที่อื่น)
    # ในแบบฝึกหัดพื้นฐาน เราจะตรวจว่า print_receipt ถูกย้ายออกไป
    source = inspect.getsource(exercise_srp.Order)
    assert "print(\"--- Receipt ---\")" not in source, "Order ไม่ควรมี logic การพิมพ์ใบเสร็จอยู่ภายในคลาส"

# Test OCP
def test_ocp_exercise():
    from solid.exercises import exercise_ocp
    source = inspect.getsource(exercise_ocp.DiscountCalculator)
    # ตรวจสอบว่าไม่มีการใช้ if-else สำหรับตรวจสอบประเภทลูกค้าใน Calculator
    assert "if customer_type == \"VIP\"" not in source, "DiscountCalculator ไม่ควรใช้ if-else ตรวจสอบประเภทลูกค้า"
    assert "elif customer_type == \"Standard\"" not in source, "DiscountCalculator ไม่ควรใช้ if-else ตรวจสอบประเภทลูกค้า"

# Test LSP
def test_lsp_exercise():
    from solid.exercises import exercise_lsp
    # ตรวจสอบว่า Ostrich ไม่ควรจะพ่น NotImplementedError เมื่อเรียกใช้เมธอดที่คลาสแม่มี
    # หรือตรวจสอบว่า Ostrich ไม่ควรสืบทอดจาก Bird ที่มี fly() โดยตรงหากบินไม่ได้
    
    # วิธีการตรวจ: ลองรันฟังก์ชันที่ใช้คลาสแม่ แล้วคลาสลูกต้องไม่พัง
    # หากผู้ใช้แยก interface บินได้/บินไม่ได้ ฟังก์ชัน make_bird_fly ควรรับเฉพาะ FlyingBird
    pass

# Test DIP
def test_dip_exercise():
    from solid.exercises import exercise_dip
    # ตรวจสอบว่า Register รับ database เข้ามาทาง constructor (Dependency Injection)
    # แทนที่จะสร้างเองข้างใน
    sig = inspect.signature(exercise_dip.Register.__init__)
    assert 'db' in sig.parameters or 'database' in sig.parameters, "Register.__init__ ควรรับ database object เข้ามา (Dependency Injection)"
