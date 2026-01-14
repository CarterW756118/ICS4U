class Term:
    def __init__(self, coeff, expo):
        self.__coeff = coeff
        self.__expo = expo
        
    def is_valid(self):
        if isinstance(self.__coeff, (int, float)) and isinstance(self.__expo, int) and self.__expo >= 0:
            return True
        return False
    
    def calculate(self, x):
        return self.__coeff * (x ** self.__expo)
    
    def __str__(self):
        if self.__coeff == 0:
            return ""
        if self.__expo == 0:
            return "{0}".format(self.__coeff)
        elif self.__expo == 1:
            return "{0}x".format(self.__coeff)
        else:
            return "{0}x^{1}".format(self.__coeff, self.__expo)
        

class Polynomial:
    def __init__(self, poly_str):
        self.__terms = self.str_to_list(poly_str)
        self.__order = len(self.__terms) - 1
    
    def is_valid(self):
        for term in self.__terms:
            if not term.is_valid():
                return False
        return True
        
    def str_to_list(self, poly_str):
        poly_list = poly_str.split(" ")
        terms_list = []
        for i in range(len(poly_list)):
            term_num = 0
            try:
                try:
                    term_num = int(poly_list[i])
                except ValueError:
                    term_num = float(poly_list[i])
            except ValueError:
                term_num = None
            new_term = Term(term_num, len(poly_list) - i - 1)
            terms_list.append(new_term)
        return terms_list
            
    def calculate_y(self, x):
        result = 0
        for term in self.__terms:
            result += term.calculate(x)
        return result
    
    def calculate_area(self, x1, x2):
        area = 0
        width = (x2 - x1) / 10**6
        for i in range(10**6):
            area += self.calculate_y(x1 + (i*width)) * width
        return area
    
    def __str__(self):
        result = ""
        for i in range(len(self.__terms)):
            if str(self.__terms[i]) != "":
                result += str(self.__terms[i])
                if i < len(self.__terms) - 1:
                    result += " + "
        return result

def get_numeric_interval(interval_str):
    try:
        x1, x2 = interval_str.split(" ")
        return (float(x1), float(x2))
    except:
        return (None, None)

poly = None
user_input_poly = None
input_x1 = None
input_x2 = None

valid_input = False
while not valid_input:
    user_input_poly = input("Enter a Polynomial (coefficients separated by a space): ").strip()
    user_input_interval = input("Enter a Interval (x1 and x2 separated by a space): ").strip()
    poly = Polynomial(user_input_poly)
    input_x1, input_x2 = get_numeric_interval(user_input_interval)
    if poly.is_valid() and input_x1 != None and input_x2 != None:
        valid_input = True
    else:
        print("Bad input please try again.")
    
print("--------------------------\n" + str(poly) + "\n--------------------------")
print("Area under the interval {0}, {1}: \n{2}".format(input_x1, input_x2, poly.calculate_area(input_x1, input_x2)))
    
