
automat = {
	"Pizza" : "8",
	"Twix" : "1",
	"Malteser" : "1",
	"Gummibaerchen" : "2",
	"Popcorn" : "3", 
	"Cola" : "1", 
	"Apfel" : "1", 
	"Salat" : "2"
}

inp = raw_input("Was wollen sie? ")


for essen in automat:
	if inp == essen:
		print "das macht", automat[essen], "EUR."

		anzahl_muenzen = 1 * automat[essen]
		print "Werfen Sie", anzahl_muenzen, "1 Euro Muenze(n) ein"


	anf = 0
	einwerf = raw_input("Bitte Muenzen einwerfen: ")


	if anf < int(automat[essen]):
		print anf
	
	if einwerf == 1:
		anf= anf + 1
		print "Noch", automat[essen] - anf, "Muenze(n) einwerfen!"
	elif anf == automat[essen]:
		print "Danke fuer ihren Einkauf!"


# anf = 0
# einwerf = ' '
# while anf < int(automat[essen]):
# 	einwerf = raw_input("Bitte Muenzen einwerfen:")
# 	print anf
# 	if einwerf == 1:
# 		anf= anf + 1
# 		break

# 		print "Noch", automat[essen] - anf, "Muenze(n) einwerfen!"
# 	elif anf == automat[essen]:
# 		print "Danke fuer ihren Einkauf!"
	 
