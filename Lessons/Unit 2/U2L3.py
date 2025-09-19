A = ["zebra", "kangaroo", "cat", "human", "aardvark"]

n = len(A)
for i in range(n-1):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            
print(A)
