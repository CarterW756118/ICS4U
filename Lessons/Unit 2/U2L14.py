setA = set() # how sets are declared in Python
setB = set()

for i in range(0,100,3):
    setA.add(i)
for i in range(0,100,4):
    setB.add(i)

if 72 in setA:
    print("72 is in setA.. removing")
    setA.remove(72)
    if not 72 in setA:
        print("72 is no longer in setA")
else:
    print("72 is not in setA")


if 72 in setB:
    print("72 is in setB.. removing")
    setB.remove(72)
    if not 72 in setB:
        print("72 is no longer in setB")
else:
    print("72 is not in setB")
    
if 13 in setA:
    print("13 is in setA.. removing")
    setA.remove(13)
else:
    print("13 is not in setA")

if 13 in setB:
    print("13 is in setB.. removing")
    setB.remove(13)
else:
    print("13 is not in setB")
    
setA.discard(13)
setB.discard(13)
