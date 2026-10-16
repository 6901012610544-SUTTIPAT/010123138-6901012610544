'''
======================================================
|                                                    |
|          6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |    
|                                                     |
======================================================
'''

def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"Enter the elements for Matrix {name} (space-separated per row):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i + 1}: ").split()
            if len(row_input) == cols:
                matrix.append([int(x) for x in row_input])
                break
            print(f"Error: Please enter exactly {cols} values.")
    return matrix


#Part A: Max, Min, and Average


def find_max(matrix):
    max_val = matrix[0][0]
    for row in matrix:
        for val in row:
            if val > max_val:
                max_val = val
    return max_val


def find_min(matrix):
    min_val = matrix[0][0]
    for row in matrix:
        for val in row:
            if val < min_val:
                min_val = val
    return min_val


def find_average(matrix):
    total = 0
    count = 0
    for row in matrix:
        for val in row:
            total += val
            count += 1
    return total / count if count > 0 else 0


#Value Search


def is_found(my_array, target):
    for row in my_array:
        for val in row:
            if val == target:
                return True
    return False


#Part C: Matrix Operations
def matrix_add(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def matrix_subtract(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result


def matrix_multiply(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += a[i][k] * b[k][j]
            row.append(cell_sum)
        result.append(row)
    return result


# --- Main Execution ---

# 1. Input Matrix A
matrix_a = input_matrix("A")

# Part A Checks on Matrix A
print("\n--- Matrix A Statistics ---")
print(f"Maximum: {find_max(matrix_a)}")
print(f"Minimum: {find_min(matrix_a)}")
print(f"Average: {find_average(matrix_a):.2f}")

#Part B Check on Matrix A
target = int(input("\nEnter a value to search in Matrix A: "))
print(f"Is {target} found in Matrix A?: {is_found(matrix_a, target)}")

#2.Input Matrix B
print("\n--- Enter Matrix B ---")
matrix_b = input_matrix("B")

#Part C
print("\n--- Matrix Operations ---")

#Addition & Subtraction
if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
    print("\nMatrix Addition (A + B):")
    for row in matrix_add(matrix_a, matrix_b):
        print(row)

    print("\nMatrix Subtraction (A - B):")
    for row in matrix_subtract(matrix_a, matrix_b):
        print(row)
else:
    print("\nAddition and Subtraction require Matrix A and B to have matching dimensions.")

#Multiplication
if len(matrix_a[0]) == len(matrix_b):
    print("\nMatrix Multiplication (A x B):")
    for row in matrix_multiply(matrix_a, matrix_b):
        print(row)
else:
    print(f"\nMultiplication not possible: Columns of A ({len(matrix_a[0])}) != Rows of B ({len(matrix_b)}).")