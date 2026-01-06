class Fraction:
    def __init__(self, num, den):
        self.__n = num
        self.__d = den
    
    def getNum(self):
        return self.__n

    def getDen(self):
        return self.__d
    
    def setNum(self, num):
        self.__n = num
    
    def setDen(self, den):
        self.__d = den
    
    def __str__(self):
        return "{0}/{1}".format(self.__n, self.__d)

class Fraction2(Fraction):
    def check(self):
        if self.getDen() == 0:
            print("Fraction has a denominator of zero!")
        else:
            print("Fraction is good!")
    
    def unreduce(self, value):
        self.setNum(self.getNum() * value)
        self.setDen(self.getDen() * value)

# driver code
f = Fraction2(3, 4)
print(f)
f.check()
f.unreduce(5)
print(f)

f2 = Fraction2(3, 0)
print(f2)
f2.check()
