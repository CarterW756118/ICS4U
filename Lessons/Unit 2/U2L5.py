s1 = {2, 3, 5, 7}
s2 = {11, 13, 17, 19, 23}
s3 = {29, 31, 37}

S = s1.union(s2.union(s3))
print(S)

S = s1.intersection(s2.intersection(s3))
print(S)
print(len(S))

print("\n")



cars = {"Ford":"Escape", "Toyota":"Camry", "Chrysler":"Pacifica", "Dodge":"Challenger"}
for key in cars:
   print(cars[key])

print("\n")



little =   {"hairy":"rat", "clever":"bat", "slow":"cod", "bare":"ant", "quick":"cat"}
midsized = {"hairy":"ewe", "clever":"fox", "slow":"pig", "bare":"eel", "quick":"doe"}
large =    {"hairy":"gnu", "clever":"ape", "slow":"cow", "bare":"elephant", "quick":"nag"}

animals = {"little": little, "midsized": midsized, "large": large}

for sub_dict in animals:
    for key in animals[sub_dict]:
        print(animals[sub_dict][key], end = " ")
    print()

print("\n")



for outter_key in animals:
    for inner_key in animals[outter_key]:
        print("The %s is %s and %s" % (animals[outter_key][inner_key], outter_key, inner_key))
