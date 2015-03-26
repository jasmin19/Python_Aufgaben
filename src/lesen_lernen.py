inp = raw_input('(t)age oder (w)orte? ')
if inp == 'w':
	suche = raw_input('Wie viele Worte? ')
	tage = 0
	for i in range(1,int(suche)):
		tage = tage + i
	tage = tage + 1
	print 'Ab dem ' + str(tage) + '. Tag liest Anna ' + suche + ' Worte.'

elif inp == 't':
	suche = raw_input('Welcher Tag? ')
	tage,i = 0,0
	while tage < int(suche):
		i += 1
		tage = tage + i
 
	if tage == suche:
		print 'Am ' + suche + '. Tag liest Anna ' + str(i) + ' Worte.'
	else:
		print 'Am ' + suche + '. Tag liest Anna ' + str(i) + ' Worte.'
 
else:
	print 'Bitte "t" oder "w" eingeben!'
	

