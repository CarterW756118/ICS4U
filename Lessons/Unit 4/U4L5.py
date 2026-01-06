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
    def mult(self, g):
        num = self.getNum() * g.getNum()
        den = self.getDen() * g.getDen()
        result = Fraction2(num, den)
        return result
    
    def unreduce(self, value):
        self.setNum(self.getNum() * value)
        self.setDen(self.getDen() * value)
    
    def add(self, g):
        num = self.getNum() + g.getNum()
        den = g.getDen()
        result = Fraction2(num, den)
        return result

# driver code
f = Fraction2(5, 6)
f2 = Fraction2(3, 4)
f3 = f2.mult(f)
print(f3)

f2Den = f2.getDen()
fDen = f.getDen()

f.unreduce(f2Den)
f2.unreduce(fDen)
f4 = f.add(f2)
print(f4)
