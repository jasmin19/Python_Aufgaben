#A, B, C, D und E sind Orte. Jeder Ort soll einmal besucht werden. 
AB = 70
BC = 80
CD = 1020
DE = 190
EA = 180

#Der kuerzeste Weg ist, wenn man die Strecke CD weg laesst. Dafuer faerht man die Strecken 
#AB, BC, DE und EA doppelt und hat trotzdem jeden Ort mindestens einmal besucht.  

Strecke = {"A":[("B", 70) , ("E", 190)],
			"B":[("C", 80) , ("A", 70)],
			"C":[("D", 1020) , ("B", 80)],
			"D":[("E", 180) , ("C", 1020)],
			"E":[]}

start = raw_input("Start: ")
ziel = raw_input("Ziel: ")
nicht_besucht = Strecke.keys()
entfernung = {k:1000000 for k in Strecke.keys()}
entfernung[start] = 0
vorgaenger = dict()

while nicht_besucht:
	weglaenge, knoten = min([(entfernung[k], k)
							for k in nicht_besucht])
	nicht_besucht -= {knoten}
	for nachbar, distanz in Strecke[knoten]:
		if(nachbar in nicht_besucht) and \
			(weglaenge + distanz < entfernung[nachbar]):
				vorgaenger[nachbar] = knoten
				entfernung[nachbar] = weglaenge + distanz


knoten = ziel
weg = []
while knoten in vorgaenger.keys():
	weg = [knoten] + weg
	knoten = vorgaenger[knoten]

print(start, end)
for k in weg:
	print ("--->", k, end)
