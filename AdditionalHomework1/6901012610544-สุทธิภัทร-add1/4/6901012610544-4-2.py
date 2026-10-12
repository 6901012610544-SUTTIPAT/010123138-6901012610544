'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 4 ใช้ฟังก์ชันแบบไม่มีพารามิเตอร์ ไม่มีการคืนค่า
'''

import getpass

def check_password():
    correct_pin = "1234"
    attempts = 0
    while attempts < 3:
        pin = getpass.getpass("Enter 4-digit PIN: ")
        if pin == correct_pin:
            print("Authentication Successful")
            return
        else:
            print(f"Incorrect PIN {attempts+1}/3")
        attempts = attempts + 1
    print("Authentication Failed: Maximum attempts reached.(3/3)")

check_password()