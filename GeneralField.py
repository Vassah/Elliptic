class GeneralField():
    def __init__(self, prime, power):
        self.elements = range(0, prime**power)
        self.characteristic = prime
        self.cardinality = len(self.elements)

    def add(self, a, b):
        return (a+b)%self.cardinality

    def mult(self, a, b):
        return (a*b)%self.cardinality

    def is_square(self, a):
        return is_Square(a, self.cardinality)

    def exponent(self, power):
        return

    def square_root(self, number):
        if not self.is_square(number):
            return None
        if self.cardinality == 2:
            return number,number,number
        elif self.cardinality%4 == 3:
            r = self.exponent(2 * number, (self.cardinality - 5)//4)
            return number,r,field_size-r
        elif self.cardinality % 8 == 5:
            v = self.exponent(2 * number, (self.cardinality - 5)//8)
            i = (2 * number * v * v) % self.cardinality
            r = (number*v*(i - 1)) % self.cardinality
            return number,r,self.cardinality-r
        elif self.cardinality % 8 == 1:
            r = self.shanks(number)
            return number,r,self.cardinality-r
        return None

class Element():
    def __init__(self, field, data):
        self.data = data
        self.field = field

    def __add__(self, other):
        if self.field == other.field:
            return Element(self.field, (self.data + other.data) % self.field.cardinality)
        return None

    def __sub__(self, other):
        if self.field == other.field:
            return Element(self.field, (self.data - other.data) % self.field.cardinality)
        return None

    def __mult__(self, other):
        if self.field == other.field:
            return Element(self.field, (self.data * other.data) % self.field.cardinality)
        return None

    def exp(self, other):
        if other == self.field.characteristic:
            return Element(self.field, 1)
        else:
            return Element(self.field, self.field.exponent( self.data, other.data))

    def square_root(self):
        return self.field.square_root(self))



'''
#The following method can be severely generalized by passing it a method as its final argument, this being the polynomial relation to be raised to the higher power of the prime. As written, we require that there be implemented an element class which the arithmetic is operating on
The idea is to take things that are defined mod p**n and raise them mod p**n+1
This shouldn't be hard using Hensel's Lemma
