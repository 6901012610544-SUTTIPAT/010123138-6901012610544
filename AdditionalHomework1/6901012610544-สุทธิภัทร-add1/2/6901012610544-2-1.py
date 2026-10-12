'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 2 แบบไม่ใช้ฟังก์ชัน
'''


num = 1

while num <= 100:
    if num > 1:
        is_prime = True
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor = divisor + 1
        if is_prime:
            print(num, end=" ")
    num = num + 1