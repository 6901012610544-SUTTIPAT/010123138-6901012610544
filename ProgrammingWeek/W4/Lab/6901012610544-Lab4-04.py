'''
    ข้อที่ 4 ตารางแม่สูตรคูณ
    6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ      
'''

def multiplication_table(n):
    i = 1
    while i <= 12:
            print(f"{number} x {i} = {number*i}")
            i = i + 1

if __name__ == '__main__':
    number = int(input("Enther number you want to be shown in Multiplication Table >>"))
    multiplication_table(number)