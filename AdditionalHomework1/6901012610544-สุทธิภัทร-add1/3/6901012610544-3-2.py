'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 3 ใช้ฟังก์ชันแบบไม่มีพารามิเตอร์ ไม่มีการคืนค่า
'''

import random

def p():
    count = 0
    while count < 10:
        x = random.randint(1, 100)
        y = random.randint(0, 5)
        result = x ** y
        print(f"p({x}, {y}) = {result}")
        count += 1

p()