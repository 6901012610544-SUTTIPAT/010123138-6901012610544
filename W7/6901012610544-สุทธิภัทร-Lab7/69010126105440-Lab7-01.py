'''
======================================================
|                                                    |
|          6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |    
|                                                     |
======================================================
'''
#Araay of array slide page 40-45


def print_2D(m):
    i = 0
    while i < len(m):
        print_all(m[i])
        i = i + 1

def print_all(m):
    i = 0
    while i < len(m):
        print(m[i], end = " ")
        i = i + 1
    print("\n")


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [3, 2, 1],
        [9, 1, 1]
    ]
    print_2D(m)