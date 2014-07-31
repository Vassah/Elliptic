import psycopg2
import EllipticCurve as ec

database_info = "dbname=slazaron_curves user=slazaron password=" #Eventually this string will hold the login info like "dbname=xyz user=abc"
with psycopg2.connect(database_info) as connecticus:
  with connecticus.cursor() as curtesy:
    with open("./home4/Elliptic/Primes.txt") as primes:
      for i in primes:
        GFi = ec.GeneralField(i, 1)
        curtesy.execute("CREATE TABLE field" + i + "(id int NOT NULL, coeff char(255), A int NOT NULL, B int NOT NULL, disc int, j int) PRIMARY KEY(id)") #STUFF HERE TO MAKE FIELD TABLE
        for j in range(0,i):
          for k in range(0,i):
            curvacious = ec.EllipticCurve(GFi, [j, k])
            pointses = curvacious.pointset
            curtesy.execute("INSERT INTO field" + i + " (A, B, id) VALUES (" + str(j) + ", " + str(k) +", " + str(j + k)+")"
            curtesy.execute("CREATE TABLE curve" + str(j + k) + " (x_val int, y_val int, z_val int)")
            for point in curvacious.pointset:
              curtesy.execute("INSERT INTO curve"  + str(j + k) + " (x_val, y_val, z_val) VALUES " + "("+point[0]+" "+point[1]+" "+point[2]+")"
#WE NEED TO THINK ABOUT DATABASE DESIGN
#Table for each field
#Columns for each coefficient, a column for curve id a column for coefficient string, a column for discriminant, a colum for j
#Then a table for each curve with three columns, one for x, y and z values of our points
