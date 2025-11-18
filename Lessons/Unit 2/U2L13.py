import random

setA = set() # how sets are declared in Python
setB = set()
"""
Below we are populating both sets by using a 'for' loop.
  - In the first loop we go from 0 to 99, skipping to every
    3rd number.
  - In the second loop, we go from 0 to 99, skipping to every
    4th number.
"""

def print_set(_set):
    for value in _set:
        print(value, "", end="")
    print()

def check_value(_set, value):
    if value in _set:
        print(value, "is in the set.")
    else:
        print(value, "is not in the set")

for i in range(0,100,3):
    setA.add(i)
for i in range(0,100,4):
    setB.add(i)

print("setA:")
print_set(setA)
print("setB:")
print_set(setB)

check_value(setA, 51)
check_value(setB, 72)

print("Length of setA:", len(setA))
print("Length of setB:", len(setB))

print("Smallest number in setA:", min(setA))
print("Smallest number in setB:", min(setB))

print("Largest number in setA:", max(setA))
print("Largest number in setB:", max(setB))

setC = set()
for i in range(10): 
    num = random.randint(1, 50)
    setC.add(num)
print("Length of setC:", len(setC))
