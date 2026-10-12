'''
6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ
Text mode ข้อที่ 2
'''



def calculate_variance(arr):
    n = len(arr)
    if n == 0:
        return 0.0

    #Calculate the mean
    total = 0
    i = 0
    while i < n:
        total += arr[i]
        i += 1
    mean = total / n

    #Calculate the sum of squared differences
    sum_squared_diff = 0.0
    i = 0
    while i < n:
        diff = arr[i] - mean
        sum_squared_diff += diff * diff
        i += 1

    #Compute population variance
    return sum_squared_diff / n


#Example
sample_data = [10, 12, 23, 23, 16, 23, 21, 16]
result = calculate_variance(sample_data)

print("Array:", sample_data)
print("Variance:", result)