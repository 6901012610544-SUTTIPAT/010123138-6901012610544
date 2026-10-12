'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 6 ใช้ฟังก์ชันแบบไม่มีพารามิเตอร์ ไม่มีการคืนค่า
'''

import random

def generate_and_check():
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

generate_and_check()