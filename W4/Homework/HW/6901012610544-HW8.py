'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
หัวข้อ print_line()
'''

def print_line(n):
    while n > 0:
        print("*", end="")
        n = n - 1
    print()

if __name__ == '__main__':
    n = int(input("How long do you want for your line: "))
    print_line(n)