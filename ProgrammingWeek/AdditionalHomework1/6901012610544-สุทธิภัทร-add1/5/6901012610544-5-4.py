'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 5 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

def get_values_above_threshold(data_list, threshold):
    result = []
    i = 0
    while i < len(data_list):
        if data_list[i] > threshold:
            result.append(data_list[i])
        i = i + 1
    return result

# รับค่า list ที่กรองแล้ว แล้วนำมาแจ้งเตือน
numbers = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]
over_500 = get_values_above_threshold(numbers, 500)

i = 0
while i < len(over_500):
    print(f"แจ้งเตือน: ค่า {over_500[i]} มีค่าเกิน 500")
    i = i + 1