# linear search function
def linsearch(arr, val):
    indexes = []
    for i in range(len(arr)):
        if arr[i] == val:
        indexes.append(i)
    if indexes != []:
        print(val, "found at indexes:", indexes)
    else:
        print(val, "not found")
        


# your main code here
myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50, 60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]

values = [20, 25, 60, 74, 97]

for value in values:
    linsearch(myArr, value)
