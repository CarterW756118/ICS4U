"""
Author : Carter Wells
Student Number : 756118
Course : ICS4U
Revision Date : 15 December 2025
Program : Polygon Driver
Description : Reads polygon data from a file, converts it into numeric
              coordinates, and constructs a polygon using the Polygon class.

VARIABLE DICTIONARY :
    fh : file - File handle for input file
    polydata : str - Line of text read from file
    points_str_list : list - List of coordinate strings
    Poly : Polygon - Polygon object
    x : float/int - X coordinate
    y : float/int - Y coordinate
"""

from poly import *

"""
Function to return numeric values from a coordinate string
Parameters:
    S (str): Coordinate string in the form "(x, y)"
Returns:
    tuple: (x, y) as numbers, or (None, None) if invalid
"""
def getNumeric(S: str):
    try:
        # Remove parentheses
        S = S.replace("(", "").replace(")", "").strip()

        # Split the string into x and y components
        x_str, y_str = S.split(",")

        # Attempt to convert x to an integer first
        try:
            x = int(x_str)
        except ValueError:
            # If not an integer, convert to float
            x = float(x_str)

        # Attempt to convert y to an integer first
        try:
            y = int(y_str)
        except ValueError:
            # If not an integer, convert to float
            y = float(y_str)

        # Return the numeric coordinates
        return (x, y)

    except:
        # Return invalid values if conversion fails
        return (None, None)


try:
    # Open the input file containing polygon data
    fh = open("a2.txt", "r")

    # Read the first line from the file
    polydata = fh.readline().strip()

    # Close the file after reading
    fh.close()

    # Split the line into individual coordinate strings
    points_str_list = polydata.split(", ")

    # Create a new Polygon object
    Poly = Polygon()

    # Loop through each coordinate string
    for point_str in points_str_list:
        # Convert string to numeric values
        x, y = getNumeric(point_str)

        # Add valid points to the polygon
        if x is not None and y is not None:
            Poly.add_point(x, y)

    # Print the polygon
    print(Poly)

except:
    # File reading error
    print("Error reading file or file does not exist.")
