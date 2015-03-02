import math

Anzahl_Noten = input("Wie viele Noten: ")

Noten = [float(input('Note: ')) for i in range(Anzahl_Noten)]
print Noten

durchschnitt = sum(Noten) / len(Noten)
print durchschnitt


aufrunden_1 = math.ceil(durchschnitt/0.1) * 0.1
print aufrunden_1
abrunden_1 = math.floor(durchschnitt /0.1) * 0.1
print abrunden_1


aufrunden_5 = math.ceil(durchschnitt/0.5) * 0.5
print aufrunden_5
abrunden_5 = math.floor(durchschnitt /0.5) * 0.5
print abrunden_5