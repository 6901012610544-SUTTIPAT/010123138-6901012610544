'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
'''


def countChar(string, target_char):
    i = 0
    count = 0
    while i < len(string):
        if string[i].lower() == target_char:
            count = count + 1
        i = i + 1

    return count

def countVowels(string):
    return countChar(string, "a") + countChar(string, "e") + countChar(string, "i") + countChar(string, "o") + countChar(string, "u")


def countWords(string):
    return len(string.split())

if __name__ == "__main__":
    txt = str(input())
    target = str(input())
    print("This message has "+ str(countChar(txt, target))+ " " + target)
    print(str(countVowels(txt)))
    print(str(countWords(txt)))