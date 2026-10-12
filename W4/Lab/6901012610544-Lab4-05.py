'''
    ข้อที่ 5 Perfect Number
    6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ      
'''



def is_perfect_number(num):
    if num <= 0:
        return False
        
    divisor_sum = 0
    i = 1
    
    while i < num:
        if num % i == 0:
            divisor_sum += i
        i += 1
    return divisor_sum == num


if __name__ == '__main__':
    #number = int(input())
    i = 1
    while i <= 50:
        perfect_num = is_perfect_number(i)
        if perfect_num:
                print(f"{i} is perfect number.")    
        i = i + 1