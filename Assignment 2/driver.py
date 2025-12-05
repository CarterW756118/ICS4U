from poly import *

def getNumeric(S: str):
    try:
        # Remove parentheses and split by comma
        S = S.replace("(", "").replace(")", "").strip()
        x_str, y_str = S.split(",")
        
        # Convert to int if possible, otherwise float
        try:
            x = int(x_str)
        except ValueError:
            x = float(x_str)
        
        try:
            y = int(y_str)
        except ValueError:
            y = float(y_str)
        
        return (x, y)
    except:
        return (None, None)

try:
    fh = open("a2.txt", "r")
    polydata = fh.readline().strip()
    fh.close()
    
    points_str_list = polydata.split(", ")
    Poly = Polygon()
    
    for point_str in points_str_list:
        x, y = getNumeric(point_str)
        if x is not None and y is not None:
            Poly.add_point(x, y)
    
    print(Poly)
except:
    print("Error reading file")

