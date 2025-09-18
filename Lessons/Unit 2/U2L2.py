inches = 10 ** 12
(feet, _inches) = divmod(inches, 12)
(yards, _feet) = divmod(feet, 3)
(miles, _yards) = divmod(yards, 1760)
(earth_to_moon, _miles) = divmod(miles, 238855)

print("One trillion inches is the same as going the moon and back %d times, plus an extra %d miles, %d yards, %d feet, and %d inches." % (earth_to_moon, _miles, _yards, _feet, _inches ))
