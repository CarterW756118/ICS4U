"""
Author : Carter Wells
Student Number : 756118
Revison date : 22 October 2025
Program : Random Magic Squares
Description : Generates magic squares based on the size input
VARIABLE DICTIONARY :
    valid_input: bool - Boolean of if the user has input a valid number
    matrix_size: int - Size of the matrix
    user_input: str - User input
    user_input_int: int - User input converted into int
    row: list - The first row of the generated matrix
    M1: list - The first matrix generated
    M2: list - The second matrix generated
    M3: list - The resulting matrix of M1 and M2 added together
    magic_sum: int - The magic sum of the magic square
    
"""

import random

"""
Function to shift a given array by an amount
Parameters:
    array (list): Array to be shifted
    amount (int): The amount that the array will be shifted by
Variables:
    new_array (list): The new array that will be shifted and returned
"""
def shift(array, amount):
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[(i + amount) % len(array)] = array[i]
    return new_array

"""
Function to add two matrices together
Parameters:
    M1 (list): Matrix to be added
    M2 (list): Second matrix to be added
Variables:
    result (list): The resulting matrix that will be returned
    row (list): Each row of the matrix
"""
def add_matrix(M1, M2):
    result = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(M1[i][j] + M2[i][j])
        result.append(row)
    return result

"""
Function to check if a number between 5 and 19 is prime
Parameters:
    num (int): The number to be checked
"""
def is_prime(num):
    return (num == 5) or (num % 2 != 0 and num % 3 != 0 and num % 5 != 0)

"""
Function to print a given matrix
Parameters:
    M (list): Matrix to be printed
Variables:
    largest (int): The largest number in the matrix
    width (int): The number of digits of the largest number
"""
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

"""
Function to compute the magic sum
Parameters:
    N (int): The size of the matrix
Variables:
    total (int): The sum of the numerator in the equation
"""
def magic_sum_formula(N):
    total = 0
    for i in range(1, N * N + 1):
        total = total + i
    return total // N

"""
Function to check if the magic square is magic
Parameters:
    M (list): The matrix to be checked
Variables:
    size (int): The size of the matrix
    magic_sum (int): The expected magic sum of the matrix
    row_sum (int): Sum of each row in the magic square
    col_sum (int): Sum of each collum in the magic square
    diag1 (int): Sum of one diagnal in the magic square
    diag2 (int): Sum of the second diagnal in the magic square
"""
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
M3 = add_matrix(M1, M2)

print("\nMagic Square of dimension %dx%d\n-----------------------" % (matrix_size, matrix_size))
print_matrix(M3)

magic_sum = magic_sum_formula(matrix_size)
print("\nMagic Sum: %d" % magic_sum)

if is_magic_square(M3):
    print("The square is magic!")
else:
    print("The square is not magic!")
