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
