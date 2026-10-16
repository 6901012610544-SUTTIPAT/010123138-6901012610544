'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 1 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

import random

def generate_and_display(total_numbers, min_val, max_val):
    arr = []
    i = 0
    while i < total_numbers:
        num = random.randint(min_val, max_val)
        arr.append(num)
        i = i + 1
    print("ข้อมูลทั้งหมด", arr)

generate_and_display(20, 10, 99)