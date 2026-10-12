'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
Sum elements of array
'''


if __name__ == "__main__":
    a = [int(e) for e in input().split()]
    sum = 0
    i = 0
    while i < len(a):
        sum = sum + a[i]
        i = i + 1

    print(sum)