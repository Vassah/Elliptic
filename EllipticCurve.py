import sys
sys.path.append('~/')
from GeneralField import *

class BadField(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class EllipticCurve():
    def __init__(self, field, coefficients): #we will require a tuple of coefficients
        self.coefficients = []
        try:
            if field.cardinality%2==0:
                if len(coefficients)<5:
                    raise BadField(field.cardinality)
                for i,val in enumerate(coefficients):
                    self.coefficients[i] = val
                    self.field = field
            if field.cardinality%3==0:
                if len(coefficients)!=3:
                    raise BadField(field.cardinality)
                for i,val in enumerate(coefficients):
                    self.coefficients[i] = val
                    self.weierstrass = 'y**2 = 4x**3 + '+str(self.coefficients[0])+' x**2 + '+str(self.coefficients[1])+'x + '+str(self.coefficients[2])
                    self.field = field
            else:
                self.coefficients = [i%field.cardinality for i in coefficients]
                self.weierstrass = 'y**2 = x**3 + '+str(self.coefficients[0])+'x + '+str(self.coefficients[1])
                self.discriminant = -16*(4*self.coefficients[0]**3 + 27*self.coefficients[1]**2)
                if self.discriminant != 0:
                    self.j = -1728*((4*(self.coefficients[0]**3))//self.discriminant)
                    self.singular = False
                else:
                    self.j = None
                    self.singular = True
                self.field = field
                self.pointset = self.points()

        except BadField as err:
            print("Sorry I don't support that yet.")
            return None

    def __str__(self):
        return 'Elliptic Curve given by '+self.weierstrass+' over '+str(self.field)
    
    def pointmaker(self, l):
        return [l[0], l[1], 1], [l[0], l[2], 1]

    def RHS(self, number):
        return (number**3 + self.coefficients[0]*number + self.coefficients[1])%self.field.cardinality

    def points(self):
        rhss = [[i, self.RHS(i)] for i in self.field.elements]
        roots = [[j[0], self.field.square_root(j[1])] for j in rhss]
        points = [[point for point in self.pointmaker([j[0], j[1][1], j[1][2]])] for j in roots if j[1]!=None]
        #The pervious line is two list comprehensions, makes points for each squareroot, the second flattens the returned tuple
        points.append([0,0,0])
        return points

    def inverse(self, a):
        if a in self.pointset:
            if self.field.characteristic == 2:
                return [a[0], a[1] - self.coefficients[0]*a[0] - self.coefficients[2], 1]
            return [a[0], a[1], 1]
        return None

    def add(self, a, b):
        if a in self.pointset and b in self.pointset:
            if self.field.characteristic == 2:
                return #something here
            elif self.field.characteristic == 3:
                return #something here
            else:
                if a == self.inverse(b):
                    return [0,0,0]
                elif (a != b):
                    delabscissa = b[0] - a[0]
                    lam = (b[1] - a[1]) // (delabscissa)
                    nu = (a[1] * b[0] - a[0] * b[1]) // (delabscissa)
                else:
                    delabscissa = 2*a[1]
                    lam = (3*a[0]**2 + 2*self.coefficients[0] + self.coefficients[1]) // delabscissa
                    nu =  -a[0]**3 + self.coefficients[1] * a[0] + 2* a[1] // delabscissa  #this line is wrong
        return None

GF = GeneralField
