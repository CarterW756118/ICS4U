def addM(M1, M2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j] = M1[i][j] + M2[i][j]
    return result

def isMagic(M):
    magic_number = 0
    for num in M[0]:
        magic_number += num
    # Rows
    for i in range(len(M)):
        result = 0
        for j in range(len(M)):
            result += M[i][j]
        if result != magic_number:
            return False
    # Cols
    for i in range(len(M)):
        result = 0
        for j in range(len(M)):
            result += M[j][i]
        if result != magic_number:
            return False
        
    # Diags
    #[0,0], [1,1], [2,2]
    result = 0
    for i in range(len(M)):
        result += M[i][i]
    #[0,2], [1,1], [2,0]
    for i in range(len(M)):
        result = 0
        for j in range(len(M) - 1, -1, -1):
            result += M[i][j]
        if result != magic_number:
            return False
        
    return True

m1 = [2, 7, 6]
m2 = [9, 5, 1]
m3 = [4, 3, 8]
M = [m1, m2, m3]

print(M)
print(isMagic(M))

M2 = addM(M,M)
print(M2)
print(isMagic(M2))

M3 = addM(M, [[-2, -2, -2], [-2, -2, -2], [-2, -2, -2]])
print(M3)
print(isMagic(M3))

M4 = addM(M, [[4, 9, 2], [3, 5, 7], [8, 1, 6]])
print(M4)
print(isMagic(M4))

M5 = addM(M, [[6, 7, 2], [1, 5, 9], [8, 3, 4]])
print(M5)
print(isMagic(M5))

M6 = addM(M, [[2, 9, 4], [7, 5, 3], [6, 1, 8]])
print(M6)
print(isMagic(M6))
