import math

A = [3, 2, 0, -1]
B = [5, 7, 8, 4]

def magnitude(arr):
    total = 0
    for num in arr:
        total += num ** 2
    return math.sqrt(total)

def vector_addition(arr, arr2):
    if len(arr) != len(arr2):
        return
    new_vector = [0] * len(arr)
    for i in range(len(arr)):
        new_vector[i] = arr[i] + arr2[i]
    return new_vector

C = vector_addition(A, B)

mag_A = magnitude(A)
mag_B = magnitude(B)
mag_C = magnitude(C)

print("|A|:", mag_A)
print("|B|:", mag_B)
print("|A+B|:", mag_C)
print("|A| + |B|:", mag_A + mag_B)

def dot_product(arr, arr2):
    if len(arr) != len(arr2):
        return
    product = 0
    for i in range(len(arr)):
        product += arr[i] * arr2[i]
    return product

def compute_angle(arr, arr2):
    if len(arr) != len(arr2):
        return
    theta = math.acos((dot_product(arr,arr2))/(magnitude(arr) * magnitude(arr2)))
    degrees = theta * 180/math.pi
    return degrees

A = [3, 2, 4]
B = [-5, 7, 2]
print(dot_product(A, B))
print(compute_angle(A, B))

print("A⋅B =", dot_product(A, A))
print("|A|^2 =", magnitude(A) ** 2)
