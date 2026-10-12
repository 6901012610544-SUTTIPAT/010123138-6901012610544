'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
Text mode ข้อที่ 1
'''


#a. Max, min, and average value of an array
def get_max_value(arr):
    if len(arr) == 0:
        return None
    max_val = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] > max_val:
            max_val = arr[i]
        i += 1
    return max_val


def get_min_value(arr):
    if len(arr) == 0:
        return None
    min_val = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] < min_val:
            min_val = arr[i]
        i += 1
    return min_val


def get_average(arr):
    if len(arr) == 0:
        return 0.0
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total / len(arr)


#b. Index of max and min value of an array
def get_max_index(arr):
    if len(arr) == 0:
        return "Empty array."
    max_idx = 0
    i = 1
    while i < len(arr):
        if arr[i] > arr[max_idx]:
            max_idx = i
        i += 1
    return max_idx


def get_min_index(arr):
    if len(arr) == 0:
        return "Empty array"
    min_idx = 0
    i = 1
    while i < len(arr):
        if arr[i] < arr[min_idx]:
            min_idx = i
        i += 1
    return min_idx


#c. Search for a value in an array (returns first matching index or -1)
def search_value(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return "No target value in this array"


#d. Count number of elements with value higher than the average
def count_higher_than_average(arr):
    if len(arr) == 0:
        return 0
    avg = get_average(arr)
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] > avg:
            count += 1
        i += 1
    return count


#e. Check whether values of an array are increasing (sorted)
def is_increasing(arr):
    if len(arr) <= 1:
        return True
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            return False
        i += 1
    return True


#Example
sample_array = [3, 8, 1, 14, 9, 22, 6]
target_to_find = 14

print("Array:", sample_array)

#a
print("Max Value:", get_max_value(sample_array))
print("Min Value:", get_min_value(sample_array))
print("Average Value:", get_average(sample_array))

#b
print("Index of Max:", get_max_index(sample_array))
print("Index of Min:", get_min_index(sample_array))

#c
print(f"Index of {target_to_find}:", search_value(sample_array, target_to_find))

#d
print("Count of elements > average:", count_higher_than_average(sample_array))

#e
print("Is increasing:", is_increasing(sample_array))
print("Is [2, 5, 7, 10] increasing:", is_increasing([2, 5, 7, 10]))