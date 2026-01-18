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

# Class representing a polynomial term
class Term:
    """
    Constructor for the Term class
    Parameters :
        coeff (int/float) - coefficient of the term
        expo (int) - exponent of the term
    Variables :
        __coeff (int/float) - stores the coefficient
        __expo (int) - stores the exponent
    """
    def __init__(self, coeff, expo):
        self.__coeff = coeff
        self.__expo = expo

    """
    Checks if the coefficient and exponent are valid types
    Variables :
        __coeff (int/float) - must be a number type
        __expo (int) - must be a non-negative integer
    Returns :
        bool - True if valid, otherwise False
    """
    def is_valid(self):
        # Return True only if coeff is a number and expo is a non negative int
        return isinstance(self.__coeff, (int, float)) and isinstance(self.__expo, int) and self.__expo >= 0
    
    """
    Computes the value of this term at a given x
    Parameters :
        x (float) - number to substitute into the term
    Variables :
        __coeff (int/float) - coefficient of the term
        __expo (int) - power that x is raised to
    Returns :
        float - evaluated term value
    """
    def calculate(self, x):
        return self.__coeff * (x ** self.__expo)
    
    """
    Creates a string form of the term for printing
    Parameters :
    Variables :
        __coeff (int/float) - determines numeric part of output
        __expo (int) - determines power formatting
    Returns :
        str - formatted term
    """
    def __str__(self):
        # If coeff is 0 return empty string
        if self.__coeff == 0:
            return ""
        # If expo is 0 return coeff as string
        if self.__expo == 0:
            return str(self.__coeff)
        # If expo is 1 return coefficient followed by x
        elif self.__expo == 1:
            return f"{self.__coeff}x"
        # Otherwise return coeffx^expo
        else:
            return f"{self.__coeff}x^{self.__expo}"

# Class representing a polynomial
class Polynomial:
    """
    Constructor for Polynomial class
        poly_str (str) - space separated coefficients
    Variables :
        __terms (list[Term]) - list storing Term objects
        __order (int) - highest power of the polynomial
    """
    def __init__(self, poly_str):
        # Convert poly_str into list of Term objects
        self.__terms = self.str_to_list(poly_str)
        # Store number of terms - 1 as order
        self.__order = len(self.__terms) - 1
    
    """
    Validates every Term in the polynomial
    Variables :
        __terms (list[Term]) - contains all polynomial terms
    Returns :
        bool - True if every term is valid
    """
    def is_valid(self):
        # Check every term with is_valid()
        for term in self.__terms:
            # If any term is invalid return False
            if not term.is_valid():
                return False
        # All terms are valid and return True
        return True
    
    """
    Converts input string into a list of Term objects
    Parameters :
        poly_str (str) - coefficient string input
    Variables :
        coefficients (list[str]) - split string of coefficients
        terms_list (list[Term]) - list to hold Term objects
        coeff (int/float/None) - parsed numeric coefficient
        exponent (int) - exponent per position
    Returns :
        list[Term] - polynomial terms
    """
    def str_to_list(self, poly_str):
        # Split poly_str by spaces into coefficients
        coefficients = poly_str.split()
        # Create empty list terms_list
        terms_list = []
        
        for i in range(len(coefficients)):
            # Attempt to convert to int
            try:
                coeff = int(coefficients[i])
            # If it fails try float
            except ValueError:
                try:
                    coeff = float(coefficients[i])
                # If both fail set to None
                except ValueError:
                    coeff = None
            
            exponent = len(coefficients) - i - 1
            # Create term object and add to terms_list
            terms_list.append(Term(coeff, exponent))
        
        return terms_list
    
    """
    Evaluate the polynomial at given x
    Parameters :
        x (float) - value to evaluate the polynomial at
    Variables :
        result (float) - sum of term values
        term (Term) - current Term being evaluated
    Returns :
        float - result of evaluation
    """
    def calculate_y(self, x):
        result = 0
        # For each term in terms add term.calculate(x)
        for term in self.__terms:
            result += term.calculate(x)
        return result
    
    """
    Compute area under a given interval
    Parameters :
        x1 (float) - left boundary
        x2 (float) - right boundary
    Variables :
        num_rectangles (int) - number of rectangles
        width (float) - width of each rectangle
        area (float) - area total
        x_position (float) - left edge of current rectangle
        height (float) - current rectangle height
    Returns :
        float - area under polynomial
    """
    def calculate_area(self, x1, x2):
        # num_rectangles = 1,000,000
        num_rectangles = 10**6
        # Calculate the width of each small rectangle
        width = (x2 - x1) / num_rectangles
        # Initialize variable for the total computed area
        area = 0
        
        # Loop through each rectangle
        for i in range(num_rectangles):
            # Determine the x-position at the left edge of the current rectangle
            x_position = x1 + (i * width)
            # Evaluate the polynomial at this x-position to get the height of the rectangle
            height = self.calculate_y(x_position)
            # Add the area of the current rectangle to total area
            area += height * width
        # Return the approximation of the area
        return area

    """
    Creates a string form of the polynomial for printing
    Variables :
        result (str) - built string of terms
        term_str (str)  - formatted string for a single term
    Returns :
        str - formatted polynomial
    """
    def __str__(self):
        # Start with empty result string
        result = ""
        # Loop through each term
        for i in range(len(self.__terms)):
            # Convert term to string
            term_str = str(self.__terms[i])
            # If result is not empty, add plus sign
            if result != "":
                result += " + "
            result += term_str
        # Return formatted string
        return result


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
