'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
'''


def my_endswith(string, target_char):
    if string[-1] == target_char:
        return True
    return False

def my_isalpha(string):
    i = 0
    state = True
    while i < len(string):
        check_char = ord(string[i].lower())
        if check_char < 97 or check_char > 122:
            state = False
            break
        i = i + 1
    return state

if __name__ == "__main__":
    txt = str(input("Enter any message>> "))
    target = str(input("Enter an alphabet>> "))
    print("Built-in endswith(): ", txt.endswith(target))
    print("User-defined endswith(): ", my_endswith(txt, target))
    print("-" * 45)
    print("Built-in isalpha(): ", txt.isalpha())
    print("User-defined isalpha(): ", my_isalpha(txt))