'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 4 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบไม่มีการคืนค่า
'''

import getpass

def check_password(correct_pin, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        pin = getpass.getpass("Enter 4-digit PIN: ")
        if pin == correct_pin:
            print("Authentication Successful")
            return
        else:
            print(f"Incorrect PIN {attempts+1}/3")
        attempts = attempts + 1
    print("Authentication Failed: Maximum attempts reached.(3/3)")

check_password("1234", 3)