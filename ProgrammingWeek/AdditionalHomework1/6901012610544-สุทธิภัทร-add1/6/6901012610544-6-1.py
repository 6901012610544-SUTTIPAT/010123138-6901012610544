'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 6 แบบไม่ใช้ฟังก์ชัน
'''

import random

numbers = []
count = 0
while count < 10:
    numbers.append(random.randint(100, 1000))
    count = count + 1

print(f"ข้อมูลทั้งหมด: {numbers}")

i = 0
while i < len(numbers):
    if numbers[i] > 800:
        print(f"แจ้งเตือน: ค่า {numbers[i]} มีค่าเกิน 800")
    i = i + 1