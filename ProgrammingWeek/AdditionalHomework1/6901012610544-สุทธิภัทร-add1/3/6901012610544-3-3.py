'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 3 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

import random

def p(x, y):
    result = x ** y
    print(f"p({x}, {y}) = {result}")

i = 0
while i < 10:
    x = random.randint(1, 100)
    y = random.randint(0, 5)
    p(x, y)
    i += 1