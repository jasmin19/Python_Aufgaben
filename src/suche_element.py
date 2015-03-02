zahlen = [2, 17, 10, 9, 16, 3, 9, 16, 5, 1, 17, 14]

print zahlen
Zahl = input("Welche Zahl?")

for i in zahlen:
	if Zahl == i:
		print "Die ausgewaehlte Zahl lautet: ", Zahl
	else:
		print "Diese Zahl ist nicht in der Liste vorhanden"