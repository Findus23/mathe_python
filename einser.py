import csv, os
def einser(zahl):
# 	print(list(str(zahl)))
	return list(str(zahl)).count("1")
def f(bis):
	a = 0
	for x in range(0, bis + 1):
		a += einser(x)
	return a


# Berechnung beginnt immer mit 0
# x = 0
# while True:
# 	b = f(x)
# 	if(b == x):
# 		print(b)
# 	x += 1
# 	print(x, b)
# print(f(200000))

x = 0
sum = 0
liste = []
try:
	while True:
		b = einser(x)
		sum += b
		liste.append(sum)
		if(x == sum):
			print(x)
		x += 1
except:
	print("Das Programm wurde beendet, die Daten werden gespeichert und dargestellt.")
	out = csv.writer(open("daten.csv", "w"), delimiter = '\n')
	out.writerow(liste)
	os.system("gnuplot gnuplot.plt")
	print("Fertig")