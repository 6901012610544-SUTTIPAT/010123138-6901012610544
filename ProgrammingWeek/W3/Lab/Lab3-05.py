def calculate_Grade(score):
    if score >= 80:
        return "A"
    elif score >= 70 and score <= 79:
        return "B"
    elif score >= 60 and score <= 69:
        return "C"
    elif score >= 50 and score <= 59:
        return "D"
    else:
        return "F"

def get_Score():
    score = int(input("Enter your score: "))
    if score > 100 or score < 0:
        print("Error: score must be in range from 0 to 100.")
        get_Score()
    else:
        return score

if __name__ == '__main__':
    score = get_Score()
    print(calculate_Grade(score))