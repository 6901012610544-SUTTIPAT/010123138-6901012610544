'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 5 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

def check_values(data_list, threshold):
    i = 0
    while i < len(data_list):
        if data_list[i] > threshold:
            print(f"แจ้งเตือน: ค่า {data_list[i]} มีค่าเกิน {threshold}")
        i = i + 1

numbers = [300, 800, 600, 400, 300, 900, 550, 650, 420, 601]
check_values(numbers, 500)