<<<<<<< HEAD
=======
#Begin here
>>>>>>> Simpler-Fix
import psycopg2
import EllipticCurve as ec

database_info = "" #Eventually this string will hold the login info like "dbname=xyz user=abc"
with psycopg2.connect(database_info) as connecticus:
  with connecticus.cursor() as curtesy:
    with open("./Primes.txt") as primes:
      for i in primes:
        GFi = ec.GeneralField(i, 1)
        curtesy.execute("CREATE TABLE field" + i + " id curve PRIMARY KEY") #STUFF HERE TO MAKE FIELD TABLE
        for j in range(0,i):
          for k in range(0,i):
            curvacious = ec.EllipticCurve(GFi, [j, k])
            pointses = curvacious.pointset
<<<<<<< HEAD
=======

          
>>>>>>> Simpler-Fix
