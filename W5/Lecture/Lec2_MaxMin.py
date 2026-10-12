arr = [int(e) for e in input().split()]

max_arr = arr[0]
min_arr = arr[0]

for i in arr:
    if max_arr < i:
        max_arr = i

    if min_arr > i:
        min_arr = i

print(f"max = {max_arr}\nmin = {min_arr}")