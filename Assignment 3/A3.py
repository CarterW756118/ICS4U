class Term:
    def __init__(self, coeff, expo):
        self.__coeff = coeff
        self.__expo = expo
    
    def is_valid(self):
        if self.__expo >= 0:
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
    
    def str_to_list(self, poly_str):
        poly_list = poly_str.split(" ")
        terms_list = []
        for i in range(len(poly_list)):
            term_int = int(poly_list[i])
            new_term = Term(term_int, len(poly_list) - i - 1)
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
            
            
poly = Polynomial("-1 2 8 0 2")
print(poly)
print(poly.calculate_area(-2, 4))
