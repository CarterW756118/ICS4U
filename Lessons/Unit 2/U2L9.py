a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3] # an array of arrays

print(Magic3[0], "\n", Magic3[1], "\n", Magic3[2], sep="")

def print_rows_cols_diag(factor = 1, addition = 0):
    print((Magic3[0][0] * factor + addition) + (Magic3[0][1] * factor + addition) + (Magic3[0][2]) * factor + addition)
    print((Magic3[1][0] * factor + addition) + (Magic3[1][1] * factor + addition) + (Magic3[1][2]) * factor + addition)
    print((Magic3[2][0] * factor + addition) + (Magic3[2][1] * factor + addition) + (Magic3[2][2]) * factor + addition)
    # Columns
    print((Magic3[0][0] * factor + addition) + (Magic3[1][0] * factor + addition) + (Magic3[2][0]) * factor + addition)
    print((Magic3[0][1] * factor + addition) + (Magic3[1][1] * factor + addition) + (Magic3[2][1]) * factor + addition)
    print((Magic3[0][2] * factor + addition) + (Magic3[1][2] * factor + addition) + (Magic3[2][2]) * factor + addition)
    # Diagonals
    print((Magic3[0][0] * factor + addition) + (Magic3[1][1] * factor + addition) + (Magic3[2][2]) * factor + addition)
    print((Magic3[0][2] * factor + addition) + (Magic3[1][1] * factor + addition) + (Magic3[2][0]) * factor + addition)

# Problem a
print_rows_cols_diag()

# Problem b
print_rows_cols_diag(1, 3)

# Problem c
print_rows_cols_diag(1, -3)

# Problem d
print_rows_cols_diag(2, 0)
