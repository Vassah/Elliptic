def Legendre(top, bottom):  #This is defined field independently since the Legendre symbol is a morphism really.
    top = top%bottom
    if top==1 or top ==0:
        return 1
    if top%2==0 and top!=2:
        return Legendre(2, bottom)*Legendre(top/2, bottom)
    if top == bottom-1:
        if bottom%4 == 1:
            return 1
        if bottom%4 == 3:
            return -1
    if top == 2:
        if bottom%8 == 1 or bottom%8 == 7:
            return 1
        if bottom%8 == 3 or bottom%8 == 5:
            return -1
    else:
        if top%4 == 1 or bottom%4 == 1:
            return Legendre(bottom, top)
        if top%4 == 3 and bottom%4 == 3:
            return -Legendre(bottom, top)
#this should hopefully calculate the legendre symbol for our two numbers
#there appears to be a case missing however. Sometimes we get a null outpout

class GeneralField():
    def __init__(self, prime, power = 1):
        if power == 1:
            self.isPrime = True
        else:
            self.isPrime = False
        self.elements = range(0, prime**power)
        self.characteristic = prime
        self.cardinality = len(self.elements)

    def of(self, number):
        return Element(self, number)

    def add(self, a, b):
        return self.of(a+b)

    def mult(self, a, b):
        return self.of(a*b)
        
    def sub(self, a, b):
        return self.of(a-b)

    def is_square(self, number, is_prime = False):
        if self.isPrime:
            return self.exponent(number, (self.cardinality - 1) // 2) == 1
        elif Legendre(number, self.cardinality) == 1:
            return True
        else:
            return False

    def exponent(self, number, exponent):
        if exponent == 0:
            return 1
        if number or exponent is float:
            try:
                number = int(number)
                exponent = int(exponent)
            except:
                print('You\'re number and exponent can\'t be true floats.')
        cut = bin(exponent).index('b') #Python nicely gives us 0xb but we don't need that information
        binexp = bin(exponent)[cut+1:][::-1] #Take the binary powers and reverse them
        exponents = [i for i in range(0, len(binexp)) if int(binexp[i])==1] #make an array of when the power is 1
        powers = [number] #Here we make the powers for the square and multiply algorithm
        for i in range(1, max(exponents)+1):
            powers.append((powers[i-1]**2)%self.cardinality)
        r = 1
        for j,val in enumerate(powers): #Here we just multiply through the values
            if j in exponents:
                r = (r*val)%self.cardinality
        return self.of(r%self.cardinality) #one last call to modulus to guarantee, then return

    def shanks(self,number):
        d= 2
        while self.is_square(d, self.cardinality):
            d += 1
        t = self.cardinality - 1
        s = 0
        while t % 2 == 0:
            t //= 2
            s += 1
        at = pow(number, t, self.cardinality)
        dt = pow(d, t, self.cardinality)
        m = 0
        for i in range(0, s):
            if pow(at * pow(dt, m), pow(2, s-1-i), self.cardinality) == (self.cardinality - 1):
                m = m + pow(2, i)
        r = (pow(number, (t + 1) // 2) * pow(dt, m // 2) % self.cardinality)
        return r

    def square_root(self, number):
        number = number % self.cardinality
        if not self.is_square(number):
            return None
        if self.cardinality == 2:
            return number,number,number
        elif self.cardinality % 4 == 3:
            r = self.exponent(2 * number, (self.cardinality - 5)//4)
            return self.of(number),self.of(r),self.of(field_size-r)
        elif self.cardinality % 8 == 5:
            v = self.exponent(2 * number, (self.cardinality - 5)//8)
            i = (2 * number * v * v) % self.cardinality
            r = (number*v*(i - 1)) % self.cardinality
            return self.of(number),self.of(r),self.of(self.cardinality-r)
        elif self.cardinality % 8 == 1:
            r = self.shanks(number) #this needs replacing since having a separate shanks method sucks
            return self.of(number),self.of(r),self.of(self.cardinality-r)

class Element():
    def __init__(self, field, data):
        self.data = data%field.cardinality
        self.field = field

    def __add__(self, other):
        if self.field == other.field:
            return self.field.add(self.data, other.data)
        return None

    def __sub__(self, other):
        if self.field == other.field:
            return self.field.sub(self.data, other.data)
        return None

    def __mult__(self, other):
        if self.field == other.field:
            return self.field.mult(self.data, other.data)
        return None
        
    __rmult__ = __mult__
    
    __radd__ = __add__

    def __pow__(self, other):
        if other is Integer:
            return self.field.exponent(self.data, other)
        elif other.data == self.field.characteristic:
            return Element(self.field, 1)
        else:
            return self.field.exponent(self.data, other.data)

    def square_root(self):
        return self.field.square_root(self.data)
        
    def __str__(self):
        return str(self.data) + " mod " + str(self.field.cardinality)
#Implement also a __lt__, __gt__, and etc

'''
#The following method can be severely generalized by passing it a method as its final argument, this being the polynomial relation to be raised to the higher power of the prime. As written, we require that there be implemented an element class which the arithmetic is operating on
The idea is to take things that are defined mod p**n and raise them mod p**n+1
This shouldn't be hard using Hensel's Lemma
'''


#Tests:
field_2 = GeneralField(2, 1)
print(field_2.cardinality)
print([i for i in field_2.elements])
print(field_2.characteristic)
print(field_2.add(3, 7))
print(field_2.add(3, 7).data)
print(field_2.sub(3, 7))
print(field_2.sub(3, 7).data)
print(field_2.of(77))
a, b = field_2.of(77), field_2.of(89)
print(a + b)
print((a + b).data)

field_3 = GeneralField(3, 1)
print(field_3.cardinality)
print([i for i in field_3.elements])
print(field_3.characteristic)
print(field_3.add(3, 7))
print(field_3.add(3, 7).data)
print(field_3.sub(3, 7))
print(field_3.sub(3, 7).data)
print(field_3.of(77))
a, b = field_3.of(77), field_3.of(89)
print(a + b)
print((a + b).data)

field_5 = GeneralField(5, 1)
print(field_5.cardinality)
print([i for i in field_5.elements])
print(field_5.characteristic)
print(field_5.add(3, 7))
print(field_5.add(3, 7).data)
print(field_5.sub(3, 7))
print(field_5.sub(3, 7).data)
print(field_5.of(77))
a, b = field_5.of(77), field_5.of(89)
print(a + b)
print((a + b).data)

field_7 = GeneralField(7, 1)
print(field_7.cardinality)
print([i for i in field_7.elements])
print(field_7.characteristic)
print(field_7.add(3, 9))
print(field_7.add(3, 9).data)
print(field_7.sub(3, 9))
print(field_7.sub(3, 9).data)
print(field_7.of(77))
a, b = field_7.of(77), field_7.of(89)
print(a + b)
print((a + b).data)

field_17 = GeneralField(17, 1)
print(field_17.cardinality)
print([i for i in field_17.elements])
print(field_17.characteristic)
print(field_17.add(15, 7))
print(field_17.add(15, 7).data)
print(field_17.sub(3, 7))
print(field_17.sub(3, 7).data)
print(field_17.of(77))
a, b = field_17.of(77), field_17.of(89)
print(a + b)
print((a + b).data)

print("\n\nis_square Test")
for i in range(0, 17):
    print(field_17.is_square(i))

print("\n\nShanks Test")
for i in range(0, 17):
    print(field_17.shanks(i))

print("\n\nSquare Root Test")
for i in range(0, 17):
    print(Element(field_17, i).square_root())
