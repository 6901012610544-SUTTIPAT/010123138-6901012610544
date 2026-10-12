'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 4
'''

def show_info():
    print("This program will calculate area of a land")
    print("given width and length")
    print()
    print("created by Suttipat Euaphattanakit")

def show_area(area):
    print("The result is", area, "(in square meter)")

def show_area_in_SqWa(area):
    print("The result is", area, "(in square wa)")

def get_width():
    width = float(input("Enter width of your land: "))
    return width

def get_length():
    length = float(input("Enter length of your land: "))
    return length

def cal_area(width, length):
    return width*length

if __name__ == '__main__':
    show_info()
    width = get_width()
    length = get_length()

    area = cal_area(width, length)

    show_area(area)
    show_area_in_SqWa(area/4)

    