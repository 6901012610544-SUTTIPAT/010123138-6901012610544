'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 7 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

def find_median(numbers_list):
    sorted_list = sorted(numbers_list)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 1:
        median = sorted_list[mid]
    else:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2

    print(f"ข้อมูลที่เรียงแล้ว: {sorted_list}")
    print(f"ค่ามัธยฐานคือ: {median}")

n = int(input("กรุณาระบุจำนวนตัวเลข (n): "))
user_numbers = []
count = 0

while count < n:
    val = float(input(f"กรอกตัวเลขที่ {count + 1}: "))
    user_numbers.append(val)
    count = count + 1


find_median(user_numbers)