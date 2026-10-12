'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
'''


def search_char_from_left(string, target_char):
    i = 0
    result = []
    while i < len(string):
        if string[i].lower() == target_char:
            result.append(i)
        i = i + 1
    return result

def search_char_from_right(string, target_char):
    length = len(string)
    i = length - 1
    result = []
    while i >= 0:
        if string[i].lower() == target_char:
            result.append(i)
        i = i - 1
    return result

def check_palindrome(string):
    i = 0
    j = len(string) - 1
    state = True
    while i < j:
        if string[i].lower() == string[j].lower():
            state = True
        else:
            state = False
            break
        i = i + 1
        j = j - 1
    return state




if __name__ == "__main__":
    txt = str(input("Enter a message>> "))
    target = str(input("Enter an alphabet>> "))
    print(target + " from left [index]: " + str(search_char_from_left(txt, target)))
    print(target + " from right [index]: " + str(search_char_from_right(txt, target)))
    print("Is palindrome: " + str(check_palindrome(txt)))