import random

def shift(array, index):
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[(i + index) % len(array)] = array[i]
    return new_array

def addM(M1, M2):
    result = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(M1[i][j] + M2[i][j])
        result.append(row)
    return result

def is_prime(num):
    return (num == 5) or (num % 2 != 0 and num % 3 != 0 and num % 5 != 0)

def print_matrix(M):
    largest = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > largest:
                largest = M[i][j]
    
    width = len(str(largest))
    
    for i in range(len(M)):
        for j in range(len(M)):
            print("%*d " % (width, M[i][j]), end="")
        print()

def magic_sum_formula(N):
    total = 0
    for i in range(1, N * N + 1):
        total = total + i
    return total // N

def is_magic_square(M):
    size = len(M)
    
    magic_sum = magic_sum_formula(size)

    for i in range(size):
        row_sum = 0
        for j in range(size):
            row_sum += M[i][j]
        if row_sum != magic_sum:
            return False

    for j in range(size):
        col_sum = 0
        for i in range(size):
            col_sum += M[i][j]
        if col_sum != magic_sum:
            return False

    diag1 = 0
    diag2 = 0
    for i in range(size):
        diag1 += M[i][i]
        diag2 += M[i][size - 1 - i]

    if diag1 != magic_sum or diag2 != magic_sum:
        return False

    return True

valid_input = False
matrix_size = 0
while not valid_input:
    user_input = input("Enter a prime number between 5 and 19: ")
    if user_input.isdigit():
        user_input_int = int(user_input)
        if user_input_int >= 5 and user_input_int <= 19 and is_prime(user_input_int):
            valid_input = True
            matrix_size = user_input_int
        else:
            print("Input must be an odd prime number between 5 and 19.")
    else:
        print("Please enter a number.")

M1 = []
row = []
for i in range(1,matrix_size+1):
    row.append(i)
random.shuffle(row)
for i in range(0, matrix_size * 2 + 1, 2):
    M1.append(shift(row,i))

M2 = []
row = []
for i in range(0, matrix_size):
    row.append(matrix_size * i)
random.shuffle(row)
for i in range(0, matrix_size * 3 + 1, 3):
    M2.append(shift(row,i))
    5
M3 = addM(M1, M2)

print("\nMagic Square of size %d\n------------------------" % matrix_size)
print_matrix(M3)

magic_sum = magic_sum_formula(matrix_size)
print("\nMagic Sum: %d" % magic_sum)

if is_magic_square(M3):
    print("The square is magic!")
else:
    print("The square is not magic!")
