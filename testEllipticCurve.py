from EllipticCurve import *

GF = GeneralField

#This test is an elliptic curve over a general field of cardinality 7                                                                    
e = EllipticCurve(GF(7, 1), [1, 1])
print(e)
print(e.field.elements)
rhss = [e.RHS(i) for i in e.field.elements]
rootset = [e.field.square_root(j) for j in rhss]
points = [e.pointmaker(k) for k in rootset if k!=None]
print(points)
print(e.points())
print(e.pointset)

#This test is an elliptic curve over a general field of cardinality 5                                                                    
print(5)
e = EllipticCurve(GF(5, 1), [2, 2])
print(e)
print(e.field.elements)
rhss = [e.RHS(i) for i in e.field.elements]
rootset = [e.field.square_root(j) for j in rhss]
points = [e.pointmaker(k) for k in rootset if k!=None]
print(points)
print(e.points())
print(e.pointset)

#This test is an elliptic curve overa  general field of cardinality 11 i.e. 3 mod 8                                                      
print(11)
e = EllipticCurve(GF(11, 1), [2, 2])
print(e)
print(e.field.elements)
rhss = [e.RHS(i) for i in e.field.elements]
rootset = [e.field.square_root(j) for j in rhss]
points = [e.pointmaker(k) for k in rootset if k!=None]
print(points)
print(e.points())
print(e.pointset)

#This test is an elliptic curve over a general field of cardinality 17 i.e. 1 mod 8                                                      
print(17)
e = EllipticCurve(GF(17, 1), [3, 2])
print(e)
print(e.field.elements)
rhss = [e.RHS(i) for i in e.field.elements]
print(rhss)
rootset = [e.field.square_root(j) for j in rhss]
print(rootset)
points = [e.pointmaker(k) for k in rootset if k!=None]
print(points)
print(e.points())
print(e.pointset)
