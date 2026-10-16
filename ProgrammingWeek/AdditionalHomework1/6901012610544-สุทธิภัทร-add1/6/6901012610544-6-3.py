'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 6 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

import random

def check_random_numbers(total_count, min_val, max_val, threshold):
    numbers = []
    count = 0
    while count < total_count:
        numbers.append(random.randint(min_val, max_val))
        count = count + 1
        
    print(f"ข้อมูลทั้งหมด: {numbers}")
    
    i = 0
    while i < len(numbers):
        if numbers[i] > threshold:
            print(f"แจ้งเตือน: ค่า {numbers[i]} มีค่าเกิน {threshold}")
        i = i + 1

check_random_numbers(10, 100, 1000, 800)