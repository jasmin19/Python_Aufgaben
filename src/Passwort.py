pw = "098765"
versuche = 3


while versuche != 0:
	inp = raw_input("Passwort: ")

	if inp == pw:
		print "BERECHTIGT"
		break
	else:
		versuche = versuche - 1
		print "Passwort ist Falsch! Du hast noch", versuche, "Versuch(e)."


		if versuche < 1: 				
			print "KONTO GESPERRT: ANZAHL PASSWORTVERSUCHE UEBERSCHRITTEN!"

