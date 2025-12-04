from poly import *

def getNumeric(S : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    x = None
    y = None
    S = S.replace("(", "").replace(")", "")
    x_str, y_str = S.split(",")
    if x_str.isdigit():
        x = int(x_str)
    else:
        x = float(x_str)
    if y_str.isdigit():
        y = int(y_str)
    else:
        y = float(y_str)
    
    return (x, y)

fh = open("a2.txt", "r")

polydata = fh.readline().strip()
points_str_list = polydata.split(", ")

Poly = Polygon()

for point in points_str_list:
    x, y = getNumeric(point)
    Poly.add_point(x, y)

print(Poly)
