Feld = [2, 17, 10, 9, 16, 3, 9, 16, 5, 1, 17, 14]

def sum_total():
	summe = sum(Feld)
	print "Die Summe ist: ",summe

def Produkt(feld):
	prod = 1.0
	for e in feld:
		prod = prod * e
	print "Das Produkt ist: ",prod

sum_total()
Produkt(Feld)


