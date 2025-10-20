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

valid_input = False
matrix_size = 0
while not valid_input:
    user_input = input("Enter a prime number between 5 and 19: ")
    if user_input.isdigit() and int(user_input) >= 5 and int(user_input) <= 19:
        user_input_int = int(user_input)
        if user_input_int % 2 != 0 and user_input_int % 3 != 0 and user_input_int % 5 != 0:
            valid_input = True
            matrix_size = user_input_int

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
    
M3 = addM(M1, M2)
for row in M3:
    for num in row:
        print(num, end=" ")
    print()
