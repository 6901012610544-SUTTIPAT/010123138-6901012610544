'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
หัวข้อ Loop until
'''

import random

sum = 0
state = True

while state:
    n = random.randint(-10, 10)
    if n == -1:
        print(f"n = {n}")
        print("-1 has entered, end of summation")
        state = False
    else:
        print(f"n = {n}")
        sum = sum + n
        print(f"sum = {sum}")
        
print(f"Therefore, the summation of random sequences is {sum}")