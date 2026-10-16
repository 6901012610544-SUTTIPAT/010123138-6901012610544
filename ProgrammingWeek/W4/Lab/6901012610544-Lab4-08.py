'''
    ข้อที่ 8 แลกเหรียญ
    6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ      
'''

def calculate_coins(amount):
    coin10 = amount // 10
    remaining = amount % 10

    coin5 = remaining // 5
    remaining = remaining % 5

    coin1 = remaining

    return coin10, coin5, coin1


if __name__ == '__main__':
    while True:
        amount = int(input("ใส่จำนวนเงินที่ต้องการแลก (ใส่ 0 เพื่อหยุดทำงาน): "))

        if amount == 0:
            print("จบการทำงานของโปรแกรม")
            break

        if amount < 0:
            print("กรุณาใส่จำนวนเงินที่มากกว่าหรือเท่ากับ 0")
            continue

        c10, c5, c1 = calculate_coins(amount)

        #Shows result
        print(f"เหรียญ 10 จำนวน {c10} เหรียญ")
        print(f"เหรียญ 5 จำนวน {c5} เหรียญ")
        print(f"เหรียญ 1 จำนวน {c1} เหรียญ")
        print("-" * 30)