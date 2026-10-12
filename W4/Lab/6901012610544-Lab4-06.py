'''
    ข้อที่ 6 Lucky Number
    6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ      
'''


import random as rd


def check_guess(guess, target):
    if guess == target:
        return "win"
    elif guess > target:
        return "greater"
    else:
        return "lower"

if __name__ == '__main__':
    lucky_number = rd.randint(1, 100)

    while True:
        guess_number = int(input("Guess the number >> "))

        #เงื่อนไขออกจากเกม
        if guess_number == 0:
            print("Exit.")
            break

        #เรียกใช้ฟังก์ชันเพื่อตรวจสอบผลการทาย
        result = check_guess(guess_number, lucky_number)

        if result == "win":
            print("You win.")
            break
        elif result == "greater":
            print(f"{guess_number} is greater than the lucky number.")
        elif result == "lower":
            print(f"{guess_number} is lower than the lucky number.")