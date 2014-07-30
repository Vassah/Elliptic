import psycopg2
import EllipticCurve as ec

database_info = "dbname=slazaron_curves user=slazaron password=" #Eventually this string will hold the login info like "dbname=xyz user=abc"
with psycopg2.connect(database_info) as connecticus:
  with connecticus.cursor() as curtesy:
    with open("./home4/Elliptic/Primes.txt") as primes:
      for i in primes:
        GFi = ec.GeneralField(i, 1)
        curtesy.execute("CREATE TABLE field" + i + " id curve PRIMARY KEY") #STUFF HERE TO MAKE FIELD TABLE
        for j in range(0,i):
          for k in range(0,i):
            curvacious = ec.EllipticCurve(GFi, [j, k])
            pointses = curvacious.pointset
            curtesy.execute("ALTER TABLE field" + i + " ADD " + ec.coefficients + " string")
            curtesy.execute("CREATE TABLE " + ec.coefficients + "coefficients PRIMARY KEY")
            for point in curvacious.pointset:
              curtesy.execute("INSERT INTO (x, y, z)" + ec.coefficients + " VALUES " + "("+point[0]+" "+point[1]+" "+point[2]+")"
#WE NEED TO THINK ABOUT DATABASE DESIGN
