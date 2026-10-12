def print_roof():
    print("  ^\n ^ ^\n^   ^")

def print_ceiling():
    print("|||||")

def print_wall():
    print("|   |\n|   |")

def print_floor():
    print("|||||")

def draw_house(h):
    print_roof()
    for i in range(0, h):
        print_ceiling()
        print_wall()
    print_floor()

if __name__ == '__main__':
    h = int(input("How many floor do you want?\n"))
    draw_house(h)