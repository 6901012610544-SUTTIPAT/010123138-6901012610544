'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 6 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

import random

def get_numbers_above_threshold(total_count, min_val, max_val, threshold):
    all_numbers = []
    over_threshold = []
    count = 0
    
    while count < total_count:
        val = random.randint(min_val, max_val)
        all_numbers.append(val)
        if val > threshold:
            over_threshold.append(val)
        count = count + 1
        
    return all_numbers, over_threshold

all_data, alerts = get_numbers_above_threshold(10, 100, 1000, 800)

print(f"ข้อมูลทั้งหมด: {all_data}")

i = 0
while i < len(alerts):
    print(f"แจ้งเตือน: ค่า {alerts[i]} มีค่าเกิน 800")
    i = i + 1