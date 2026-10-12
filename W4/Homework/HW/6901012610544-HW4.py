'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
หัวข้อ Sum
'''

i = 1
sum = 0
n = int(input())

while(i <= n):
    print(f"i = {i}")
    sum = sum + i
    print(f"sum {sum}")
    i = i + 1
    

print(f"Final summation from 1 to {n} is {sum}")