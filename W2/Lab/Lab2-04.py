def say_hello(choice):
    l = ["Hello, ", "Sawasdee, ", "Selamat datang, ", "Error: there is no choice please try again"]
    if choice != 4:
        print(l[choice-1] + "KMUTNB")
    elif choice == 4:
        print("Error: there is no choice 4 please try again")

if __name__ == '__main__':
    choice = int(input())
    print(say_hello(choice))

'''
match choice:
        case 1:
            return "Hello, KMUTNB"
        case 2:
            return "Sawasdee, KMUTNB"
        case 3:
            return "Selamat datang, KMUTNB"
        case 4:
            return "Error: there is no choice " + str(choice) + " please try again"
'''