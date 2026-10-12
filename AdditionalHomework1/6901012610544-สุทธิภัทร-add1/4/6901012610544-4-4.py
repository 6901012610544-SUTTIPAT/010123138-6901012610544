'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 4 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

import getpass

def verify_pin(correct_pin, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        pin = getpass.getpass("Enter 4-digit PIN: ")
        if pin == correct_pin:
            return True
        else:
            print(f"Incorrect PIN {attempts+1}/3")
        attempts = attempts + 1
    return False


if verify_pin("1234", 3):
    print("Authentication Successful")
else:
    print("Authentication Failed: Maximum attempts reached.(3/3)")