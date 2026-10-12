'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 3 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

import random

def p(x, y):
    return x ** y

i = 0
while i < 10:
    x = random.randint(1, 100)
    y = random.randint(0, 5)
    result = p(x, y)
    print(f"p({x}, {y}) = {result}")
    i = i + 1