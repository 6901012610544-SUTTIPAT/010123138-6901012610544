'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
ข้อที่ 3
'''

def BMI(weight, height):
    bmi = weight / height**2
    print(f"Your BMI is {bmi:.2f}.")

if __name__ == '__main__':
    weight = float(input("Please enter your weight in kilogram: "))
    height = float(input("Please enter your height in meter: "))
    BMI(weight, height)
