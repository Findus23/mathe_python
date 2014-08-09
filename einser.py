# 17. Consider a function which, for a given whole number n, returns the number of ones required when writing out all numbers between 0 and n.
# For example, f(13)=6.  Notice that f(1)=1.  What is the next largest n such that f(n)=n?


import csv, os  # für CSV-Export und Aufruf von Gnuplot

def einser(zahl):  # Anzahl der "1" in einer Zahl
	return list(str(zahl)).count("1")

# Berechnung beginnt immer mit 0
# def f(n):  # Berechnung von f(n)
# 	a = 0
# 	for x in range(0, n + 1):
# 		a += einser(x)
# 	return a
# x = 0
# while True:
# 	b = f(x)
# 	if(b == x):
# 		print(b)
# 	x += 1
# 	print(x, b)
# print(f(200000))

n = 0
sum = 0
liste = []  # Liste der f(n) Werte
try:
	while True:
		b = einser(n)
		sum += b
		liste.append(sum)  # Wert zur Liste hinzufügen
		if(n == sum):  # falls f(n)=n ...
			print(n)  # ... die Zahl ausgeben
		n += 1
except:  # Wenn das Programm abgebrochen wurde ...
	print("Das Programm wurde beendet, die Daten werden gespeichert und dargestellt.")
	out = csv.writer(open("daten.csv", "w"), delimiter = '\n')
	out.writerow(liste)
	os.system("gnuplot gnuplot.plt")
	print("Fertig")