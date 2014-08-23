#!/usr/bin/python
import cgi
import cgitb
import psycopg2
import json
import EllipticCurve as ec
cgitb.enable()

#Send the header of the response
print("Content-Type: text/json")
print()

#Now we have to check the database to see if the desired curve is there.
requested = cgi.FieldStorage()
for j,i in enum(requested):
	requested[j] = i.lower()
with psycopg2.connect() as connecticus:
	with curse as psycopg2.cursor():
		curse.execute("SELECT " + requested["curve"] + " FROM " + requested["field"] + ";")
		first = cur.fetchone()
		if first == ():
			result = []
			break
		else:
			curse.execute("SElECT * FROM " + first[2])
			result = curse.fetchall()

#Now we send the requisite response
if result != []:
	print json.dumps(result)
else:
	prime = int(float(requested["field"]))
	curve = #Some stuff here
	gf = ec.GeneralField(prime)
