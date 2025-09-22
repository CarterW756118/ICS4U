a = [7, 1, 3, 5, 2, 4, 6]
b = [0] * len(a)

shift = 2

for i in range(len(a)):
    b[(i + shift) % len(a)] = a[i]

print("Before:", a)
print("After:", b)
