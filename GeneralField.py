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
        return number % self.cardinality


    def add(self, a, b):
        return self.of(a + b)

    def mult(self, a, b):
        return self.of( a * b)
        
    def sub(self, a, b):
        return self.of(a - b)

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
                print('Your number and exponent can\'t be true floats.')
        cut = bin(exponent).index('b') #Python nicely gives us 0xb but we don't need that information
        binexp = bin(exponent)[cut+1:][::-1] #Take the binary powers and reverse them
        exponents = [i for i in range(0, len(binexp)) if int(binexp[i])==1] #make an array of when the power is 1
        powers = [number] #Here we make the powers for the square and multiply algorithm
        for i in range(1, max(exponents)+1):
            powers.append(self.of(powers[i-1]**2))
        r = 1
        for j,val in enumerate(powers): #Here we just multiply through the values
            if j in exponents:
                r = self.of(r*val)
        return self.of(r) #one last call to modulus to guarantee, then return
    
    def shanks(self, number):
        d = 2
        while self.is_square(d):
            d += 1
        t = self.cardinality - 1
        s = 0
        while t % 2 ==0:
            t //= 2
            s += t
        at = pow(number, t, self.cardinality)
        dt = pow(d, t, self.cardinality)
        m = 0
        for i in range(0, 2):
            if pow(at * pow(dt, m), pow(2, s-1-i), self.cardinality) == (self.cardinality - 1):
                m = m + pow(2, i)
        r = (pow(number, (t + 1) // 2) * pow(dt, m // 2)) % self.cardinality
        return r

    def cipolla(self, number):
        return None

    def square_root(self, number):
        number = number % self.cardinality
        if not self.is_square(number):
            return None
        if self.cardinality == 2:
            return number,number,number
        elif self.cardinality % 4 == 3:
            r = self.exponent(2 * number, (self.cardinality - 5)//4)
            return self.of(number),self.of(r),self.of(self.cardinality-r)
        elif self.cardinality % 8 == 5:
            v = self.exponent(2 * number, (self.cardinality - 5)//8)
            i = (2 * number * v * v) % self.cardinality
            r = (number*v*(i - 1)) % self.cardinality
            return self.of(number),self.of(r),self.of(self.cardinality-r)
        elif self.cardinality % 8 == 1:
            r = self.shanks(number) #this needs replacing since having a separate shanks method sucks
            return self.of(number),self.of(r),self.of(self.cardinality-r)
        return None

'''
#The following method can be severely generalized by passing it a method as its final argument, this being the polynomial relation to be raised to the higher power of the prime. As written, we require that there be implemented an element class which the arithmetic is operating on
The idea is to take things that are defined mod p**n and raise them mod p**n+1
This shouldn't be hard using Hensel's Lemma
'''


