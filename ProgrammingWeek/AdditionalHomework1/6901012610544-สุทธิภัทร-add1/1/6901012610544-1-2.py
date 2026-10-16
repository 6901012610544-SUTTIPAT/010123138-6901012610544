'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 1 ใช้ฟังก์ชันแบบไม่มีพารามิเตอร์ ไม่มีการคืนค่า
'''

import random

def generate_and_display():
    arr = []
    i = 0
    while i < 20:
        num = random.randint(10, 99)
        arr.append(num)
        i = i + 1
    print("ข้อมูลทั้งหมด", arr)

generate_and_display()