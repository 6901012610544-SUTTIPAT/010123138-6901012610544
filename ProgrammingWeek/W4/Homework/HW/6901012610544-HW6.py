'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
หัวข้อ Password
'''

import getpass

count = 0


while count != 5:
    user_password = getpass.getpass("Enter your password")
    if user_password == "KMUTNB":
       print("Logging in...")
       break
    else:
       count = count + 1
       print(f"Password incorrect. Please try again {count}/5")