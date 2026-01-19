"""
Author : Carter Wells
Student Number : 756118
Course : ICS4U
Revision Date : 16 January 2026
Program : Area under a Polynomial Curve
Description : Promts the user for a polynomial and interval and
              calculates the area under it between the two x-values.
VARIABLE DICTIONARY :
    user_input_poly : str - polynomial input string from user
    user_input_interval : str - interval input string from user
    poly : Polynomial - constructed polynomial object
    input_x1 : float - left interval parsed from user input
    input_x2 : float - right interval parsed from user input
    valid_input : bool - boolean for valid user input
"""

from poly import *

"""
Parses numeric interval input
Parameters :
    interval_str (str) - input string from user
Variables :
    x1 (str) - first split interval
    x2 (str) - second split interval
Returns :
    tuple(float, float) - parsed interval values
"""
def get_numeric_interval(interval_str):
    # Try splitting into x1 and x2
    try:
        x1, x2 = interval_str.split()
        # Return converted floats
        return (float(x1), float(x2))
    # If fails return None, None
    except ValueError:
        return (None, None)


# Initialize variables
poly = None
input_x1 = None
input_x2 = None
valid_input = False

# Loop until valid_input is True
while not valid_input:
    # Ask user for polynomial string
    user_input_poly = input("Enter a Polynomial (coefficients separated by a space): ")
    # Ask user for interval string
    user_input_interval = input("Enter an Interval (x1 and x2 separated by a space): ")
    
    # Create Polynomial from user input
    poly = Polynomial(user_input_poly)
    # Parse x1 and x2
    input_x1, input_x2 = get_numeric_interval(user_input_interval)
    
    # If polynomial valid and interval parsed correctly
    if poly.is_valid() and input_x1 is not None and input_x2 is not None:
        valid_input = True
    # Else tell user input was bad
    else:
        print("Bad input, please try again.\n")

# Print formatted polynomial
print(f"\n--------------------------")
print(f"Polynomial: {poly}")
print(f"--------------------------")

# Compute area
area = poly.calculate_area(input_x1, input_x2)
# Print interval and result
print(f"Area under the interval [{input_x1}, {input_x2}]: {area:.4f}")
