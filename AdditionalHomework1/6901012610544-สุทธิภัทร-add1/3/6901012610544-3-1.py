'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 3 แบบไม่ใช้ฟังก์ชัน
'''

import random

count = 0
while count < 10:
    x = random.randint(1, 100)
    y = random.randint(0, 5)
    result = x ** y
    print(f"p({x}, {y}) = {result}")
    count += 1