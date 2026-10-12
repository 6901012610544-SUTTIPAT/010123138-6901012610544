'''
    ข้อที่ 7 ค่าเฉลี่ยน้ำหนักทุเรียน
    6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ      
'''


def calculate_durian_average():
    sum_of_weight = 0
    counter = 0

    while True:
        weight = int(input("Please input Durian weight: "))
        if weight != 0:
            sum_of_weight += weight
            counter += 1
        else:
            print("Exit.")
            break

    if counter > 0:
        average_weight = sum_of_weight / counter
        return counter, average_weight
    else:
        return 0, 0.0


if __name__ == '__main__':
    count, avg = calculate_durian_average()

    if count > 0:
        print(f"Average weight of {count} durians is {avg:.2f} kg.")
    else:
        print("No durian weights were entered.")