'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 7 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

def find_median(numbers_list):
    sorted_list = sorted(numbers_list)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 1:
        return sorted_list[mid]
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

n = int(input("กรุณาระบุจำนวนตัวเลข (n): "))
data = []
count = 0
while count < n:
    data.append(float(input(f"กรอกตัวเลขที่ {count + 1}: ")))
    count = count + 1

result = find_median(data)
print(f"ข้อมูลทั้งหมดคือ: {sorted(data)}")
print(f"ค่ามัธยฐานคือ: {result}")