
automat = {
	"pizza" : "8",
	"twix" : "1",
	"malteser" : "1",
	"gummibaerchen" : "2",
	"popcorn" : "3", 
	"cola" : "1", 
	"apfel" : "1", 
	"salat" : "2"
}

inp = raw_input("Was wollen sie? ")

for essen in automat:
	if inp == essen.lower() or inp == essen.upper() or inp == essen.title():
		print "das macht", automat[essen], "EUR."

		anzahl_muenzen = 1 * int(automat[essen])
		print "Werfen Sie", anzahl_muenzen, "1 Euro Muenze(n) ein."
		break
else: 
	print "ERROR! Dieses Produkt gibt es nicht."

anf = 0
while anf <= automat[essen]:
	einwerf = input("Bitte Muenzen einwerfen: ")
	if einwerf == 1:
		anf+=1
		print "Noch", anzahl_muenzen - anf, "Muenze(n) einwerfen!"
		if anf == anzahl_muenzen:
			print "Danke fuer ihren Einkauf!"
			break

	 
