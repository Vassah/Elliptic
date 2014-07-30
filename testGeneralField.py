import GeneralField as gf

field_3 = gf.GeneralField(3, 1)
print(field_3.cardinality)
print("\n\nis_square Test")
for i in range(0, 3):
    print(field_3.is_square(i))

print("\n\nSquare Root Test")
for i in range(0, 3):
    print(field_3.square_root(i))

field_5 = gf.GeneralField(5, 1)
print(field_5.cardinality)
print("\n\nis_square Test")
for i in range(0, 5):
    print(field_5.is_square(i))

print("\n\nSquare Root Test")
for i in range(0, 5):
    print(field_5.square_root(i))

field_7 = gf.GeneralField(7, 1)
print(field_7.cardinality)
print("\n\nis_square Test")
for i in range(0, 7):
    print(field_7.is_square(i))

print("\n\nSquare Root Test")
for i in range(0, 7):
    print(field_7.square_root(i))

field_17 = gf.GeneralField(17, 1)
print(field_17.cardinality)
print("\n\nis_square Test")
for i in range(0, 17):
    print(field_17.is_square(i))

print("\n\nShanks Test")
for i in range(0, 17):
    print(field_17.shanks(i))

print("\n\nSquare Root Test")
for i in range(0, 17):
    print(field_17.square_root(i))

