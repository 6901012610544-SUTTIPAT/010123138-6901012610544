'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 7 ใช้ฟังก์ชันแบบไม่มีพารามิเตอร์ ไม่มีการคืนค่า
'''

def calculate_median():
    n = int(input("กรุณาระบุจำนวนตัวเลข (n): "))
    numbers = []
    count = 0
    while count < n:
        val = float(input(f"กรอกตัวเลขที่ {count + 1}: "))
        numbers.append(val)
        count = count + 1

    numbers.sort()
    mid = n // 2
    if n % 2 == 1:
        median = numbers[mid]
    else:
        median = (numbers[mid - 1] + numbers[mid]) / 2

    print(f"ข้อมูลที่เรียงแล้ว: {numbers}")
    print(f"ค่ามัธยฐานคือ: {median}")

calculate_median()