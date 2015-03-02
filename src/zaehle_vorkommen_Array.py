Feld = [2, 17, 10, 9, 16, 3, 9, 16, 30, 1, 12, 14]

zaehler = 0
for i in Feld:
	if i % 3 == 0:
		zaehler+=1

print zaehler, " Zahlen sind durch 3 teilbar."
print "Diese Zahlen lauten: ", 