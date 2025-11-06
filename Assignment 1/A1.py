"""
Author : Carter Wells
Student Number : 756118
Revison date : 7 November 2025
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
    # Create a new list of the same length
    new_array = [0] * len(array)
    # Loop over each index in the array
    for i in range(len(array)):
        # Calculate the new position for each element and place it in new_array
        new_array[(i + amount) % len(array)] = array[i]
    # Return the shifted list
    return new_array

"""
Function to add two matrices together (must be same size)
Parameters:
    M1 (list): Matrix to be added
    M2 (list): Second matrix to be added
Variables:
    result (list): The resulting matrix that will be returned
    row (list): Each row of the matrix
"""
def add_matrix(M1, M2):
    # Return -1 if the sizes are not the same
    if len(M1) != len(M2):
        return -1
    # Stores the final summed matrix
    result = []
    # Loop through each row index
    for i in range(matrix_size):
        # Temporary list for the current row
        row = []
        # Loop through each column index
        for j in range(matrix_size):
            # Add corresponding elements from both matrices
            row.append(M1[i][j] + M2[i][j])
        # Add completed row to the result
        result.append(row)
    # Return the new matrix
    return result

"""
Function to check if a number between 5 and 19 is prime
Parameters:
    num (int): The number to be checked
"""
def is_prime(num):
    # Returns True if number is 5 or not divisible by 2, 3, or 5
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
    # Find the largest number to determine spacing width for alignment
    largest = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > largest:
                largest = M[i][j]
    # Width based on number of digits in largest number
    width = len(str(largest))
    
    # Loop over each row in the matrix
    for i in range(len(M)):
        # Loop through each value in the row
        for j in range(len(M)):
            # Print with width formatting
            print("%*d " % (width, M[i][j]), end="")
        # Move to next line after each row
        print()

"""
Function to compute the magic sum
Parameters:
    N (int): The size of the matrix
Variables:
    total (int): The sum of the numerator in the equation
"""
def magic_sum_formula(N):
    # Calculate total of all numbers from 1 to N^2
    total = 0
    for i in range(1, N * N + 1):
        total = total + i
    # Divide by N to get the magic sum
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
    # Size of the matrix (number of rows)
    size = len(M)
    
    # Expected magic sum for that size
    magic_sum = magic_sum_formula(size)
    
    # Check all rows
    for i in range(size):
        row_sum = 0
        for j in range(size):
            row_sum += M[i][j]
        # If any row sum does not match, it is not magic
        if row_sum != magic_sum:
            return False
    
    # Check all columns
    for i in range(size):
        col_sum = 0
        for j in range(size):
            col_sum += M[j][i]
        # If any column sum does not match, it is not magic
        if col_sum != magic_sum:
            return False
    
    # Check both diagonals
    diag1 = 0
    diag2 = 0
    for i in range(size):
        # Top-left to bottom-right
        diag1 += M[i][i]
        # Top-right to bottom-left
        diag2 += M[i][size - 1 - i]
    
    # If either diagonal sum does not match, it is not magic
    if diag1 != magic_sum or diag2 != magic_sum:
        return False
    
    # All tests passed, so it is magic
    return True

# Will remain false until user provides valid input
valid_input = False
# Hold the user selected matrix size
matrix_size = 0
while not valid_input:
    # Ask user for input
    user_input = input("Enter a prime number between 5 and 19: ")
    # Check if input is numeric
    if user_input.isdigit():
        # Convert to integer
        user_input_int = int(user_input)
        # Check range and if it is prime
        if user_input_int >= 5 and user_input_int <= 19 and is_prime(user_input_int):
            # Input is valid
            valid_input = True
            # Save as matrix size
            matrix_size = user_input_int
        else:
            print("Input must be an odd prime number between 5 and 19.")
    else:
        print("Please enter a number.")

# Initialize first matrix
M1 = []
# Create a list of numbers 1..N
row = []
for i in range(1,matrix_size+1):
    row.append(i)
# Shuffle the row randomly
random.shuffle(row)
# Append shifted versions of row to M1 (using increments of 2)
for i in range(0, matrix_size * 2 + 1, 2):
    # Add shifted row to matrix
    M1.append(shift(row,i))

# Initialize second matrix
M2 = []
# Create a list of numbers (0, N, 2N, ...)
row = []
for i in range(0, matrix_size):
    row.append(matrix_size * i)
# Shuffle the row randomly
random.shuffle(row)
# Append shifted versions of row to M2 (using increments of 3)
for i in range(0, matrix_size * 3 + 1, 3):
    # Add shifted row to matrix
    M2.append(shift(row,i))

# Add M1 and M2 together
M3 = add_matrix(M1, M2)

# Print the resulting magic square matrix
print("\nMagic Square of dimension %dx%d\n-----------------------" % (matrix_size, matrix_size))
print_matrix(M3)

# Compute and print expected magic sum
magic_sum = magic_sum_formula(matrix_size)
print("\nMagic Sum: %d" % magic_sum)

# Check if M3 is a valid magic square and print the result
if is_magic_square(M3):
    print("The square is magic!")
else:
    print("The square is not magic!")
