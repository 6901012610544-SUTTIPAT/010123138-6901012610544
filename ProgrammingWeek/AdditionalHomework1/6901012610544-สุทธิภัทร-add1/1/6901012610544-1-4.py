'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 1 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

import random

def generate_random_numbers(total_numbers, min_val, max_val):
    arr = []
    i = 0
    while i < total_numbers:
        num = random.randint(min_val, max_val)
        arr.append(num)
        i = i + 1
    return arr

result = generate_random_numbers(20, 10, 99)
print("ข้อมูลทั้งหมด ", result)