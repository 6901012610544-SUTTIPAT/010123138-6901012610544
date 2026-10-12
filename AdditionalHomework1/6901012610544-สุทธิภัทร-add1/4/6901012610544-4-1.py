'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 4 แบบไม่ใช้ฟังก์ชัน
'''

import getpass

CORRECT_PIN = "1234"
attempts = 0

while attempts < 3:
    pin = getpass.getpass("Enter 4-digit PIN: ")
    if pin == CORRECT_PIN:
        print("Authentication Successful")
        break
    else:
        print(f"Incorrect PIN {attempts+1}/3")
    attempts = attempts + 1

if attempts == 3 and pin != CORRECT_PIN:
    print("Authentication Failed: Maximum attempts reached.(3/3)")