'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 2 ใช้ฟังก์ชันแบบมีพารามิเตอร์ แบบมีการคืนค่า
'''

def get_primes(start, end):
    primes = []
    num = start
    while num <= end:
        if num > 1:
            is_prime = True
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    is_prime = False
                    break
                divisor = divisor + 1
            if is_prime:
                primes.append(num)
        num = num + 1
    return primes

result = get_primes(1, 100)
print(result)