'''
======================================================
|                                                    |
|          6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |    
|                                                     |
======================================================
'''

import random as rd


temperature = []

def week_average(w, temperatures):
    i = 0
    sum = 0
    while i < 7:
        sum = sum + temperatures[i]
        i = i + 1
    return sum/len(temperature[w])

def week_max(w, temperatures):
    max_temp = temperatures[0]
    i = 1
    while i < 7:
        if max_temp < temperatures[i]:
            max_temp = temperatures[i]
        i = i + 1
    return max_temp

def week_min(w, temperatures):
    min_temp = temperatures[0]
    i = 1
    while i < 7:
        if min_temp > temperatures[i]:
            min_temp = temperatures[i]
        i = i + 1
    return min_temp

def overall_max(temperatures):
    i = 0
    arr = []
    while i < 4:
        arr.append(week_max(i, temperatures[i]))
        i = i + 1
    max_tmp = arr.index(max(arr)) + 1
    return [max_tmp, max(arr)]
    


def overall_min(temperatures):
    i = 0
    arr = []
    while i < 4:
        arr.append(week_min(i, temperatures[i]))
        i = i + 1
    min_tmp = arr.index(min(arr)) + 1
    return [min_tmp, min(arr)]

if __name__ == "__main__":
    i = 0
    j = 0
    while i < 4:
        week_temperature = []
        while j < 7:
            #day_temperature = float(input(f"Please enter week {i+1} day {j+1} temperature in Celsius>> "))
            day_temperature = round(rd.uniform(20, 40), 2)
            week_temperature.append(day_temperature)
            j = j + 1
        temperature.append(week_temperature)
        i = i + 1
        j = 0
    print("-"*60)

    i = 0
    while i < 4:
        print(f"Week {i+1} temerature(ํC): ", end="")
        print(*(temperature[i]), sep=", ")
        i = i + 1

    print("-"*60)
    i = 0
    while i < 4:
        print(f"Week {i+1} average temerature: {week_average(i, temperature[i]):.2f}")
        i = i + 1

    print("-"*60)
    i = 0
    while i < 4:
        print(f"Week {i+1} peak temerature: {week_max(i, temperature[i]):.2f}")
        i = i + 1

    print("-"*60)
    i = 0
    while i < 4:
        print(f"Week {i+1} min temerature: {week_min(i, temperature[i]):.2f}")
        i = i + 1

    print("-"*60)
    print(f"Overall max temerature on week {overall_max(temperature)[0]} is {overall_max(temperature)[1]}")

    print("-"*60)
    print(f"Overall min temerature on week {overall_min(temperature)[0]} {overall_min(temperature)[1]}")