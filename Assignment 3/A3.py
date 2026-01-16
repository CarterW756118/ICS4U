"""
# Class representing a polynomial term
"""
class Term:
    """
    Constructor for the Term class
    Parameters:
        coeff (int/float) : coefficient of the term
        expo (int)        : exponent of the term
    """
    def __init__(self, coeff, expo):
        self.__coeff = coeff
        self.__expo = expo

    """
    Checks if the coefficient and exponent are valid types
    Returns:
        bool: True if valid, otherwise False
    """
    def is_valid(self):
        return isinstance(self.__coeff, (int, float)) and isinstance(self.__expo, int) and self.__expo >= 0
    
    """
    Computes the value of this term at a given x
    Parameters:
        x (float)
    Returns:
        float: evaluated term
    """
    def calculate(self, x):
        return self.__coeff * (x ** self.__expo)
    
    """
    Creates a string form of the term for printing
    Returns:
        str: formatted term
    """
    def __str__(self):
        if self.__coeff == 0:
            return ""
        if self.__expo == 0:
            return str(self.__coeff)
        elif self.__expo == 1:
            return f"{self.__coeff}x"
        else:
            return f"{self.__coeff}x^{self.__expo}"

"""
# Class representing a polynomial
"""
class Polynomial:
    """
    Constructor for Polynomial class
    Parameters:
        poly_str (str): space separated coefficients
    """
    def __init__(self, poly_str):
        self.__terms = self.str_to_list(poly_str)
        self.__order = len(self.__terms) - 1
    
    """
    Validates every Term in the polynomial
    Returns:
        bool: True if every term is valid
    """
    def is_valid(self):
        for term in self.__terms:
            if not term.is_valid():
                return False
        return True
    
    """
    Converts input string into a list of Term objects
    Parameters:
        poly_str (str)
    Returns:
        list[Term]: polynomial terms
    """
    def str_to_list(self, poly_str):
        coefficients = poly_str.split()
        terms_list = []
        
        for i in range(len(coefficients)):
            try:
                coeff = int(coefficients[i])
            except ValueError:
                try:
                    coeff = float(coefficients[i])
                except ValueError:
                    coeff = None
            
            exponent = len(coefficients) - i - 1
            terms_list.append(Term(coeff, exponent))
        
        return terms_list
    
    """
    Evaluate the polynomial at given x
    Parameters:
        x (float)
    Returns:
        float: result of evaluation
    """
    def calculate_y(self, x):
        result = 0
        for term in self.__terms:
            result += term.calculate(x)
        return result
    
    """
    Compute area under a given interval
    Parameters:
        x1 (float), x2 (float)
    Returns:
        float: area under polynomial
    """
    def calculate_area(self, x1, x2):
        num_rectangles = 10**6
        width = (x2 - x1) / num_rectangles
        area = 0
        
        for i in range(num_rectangles):
            x_position = x1 + (i * width)
            area += self.calculate_y(x_position) * width
        
        return area

    """
    Creates a string form of the polynomial for printing
    Returns:
        str: formatted polynomial with + signs
    """
    def __str__(self):
        result = ""
        for i in range(len(self.__terms)):
            term_str = str(self.__terms[i])
            if term_str != "":
                if result != "":
                    result += " + "
                result += term_str
        return result

def get_numeric_interval(interval_str):
    try:
        x1, x2 = interval_str.split()
        return float(x1), float(x2)
    except (ValueError, AttributeError):
        return None, None


poly = None
input_x1 = None
input_x2 = None

valid_input = False
while not valid_input:
    user_input_poly = input("Enter a Polynomial (coefficients separated by a space): ").strip()
    user_input_interval = input("Enter an Interval (x1 and x2 separated by a space): ").strip()
    
    poly = Polynomial(user_input_poly)
    input_x1, input_x2 = get_numeric_interval(user_input_interval)
    
    if poly.is_valid() and input_x1 is not None and input_x2 is not None:
        valid_input = True
    else:
        print("Bad input, please try again.\n")

print(f"\n--------------------------")
print(f"Polynomial: {poly}")
print(f"--------------------------")
area = poly.calculate_area(input_x1, input_x2)
print(f"Area under the interval [{input_x1}, {input_x2}]: {area:.4f}")
