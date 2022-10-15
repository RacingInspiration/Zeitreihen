'''
Dies ist das erste Python Programm 
In diesem werden die grundlegenden Python-Befehle vorgestellt
'''

# der obligatorische "Hello World" Befehl
print('Hello World')

# Variablentypen
a = 5 # das ist ein Integer
b = 4.5 # das ist ein Float
c = a*b # das ist auch eine floating point number
d = True

# Ausgaben
print('a= ',a,'; b= ',b,'; c= ',c)

# String Operationen
NameFreund1 = 'Hans-Peter'
NameFreund2 = 'Udo Jürgens'
Satz = 'Ich bin befreundet mit '+NameFreund1+' und '+NameFreund2+'.'
print(NameFreund1[0:2]) # Achtung: der Buchstabe NameFreund1[2] wird schon nicht mehr ausgegeben!
# der Doppelpunkt (:) bedeutet von ... bis vor ...

# Listen
bikes = ['citybike', 'ebike', 'trekking bike']
bikes.append('racingbike')

print(bikes)

# Mathematische Operationen
a = 4.0
print(type(a))
b = 'iuad'
print(type(b))
komplex = 2.1 + 3j
print(komplex.real)

#Wörterbuch
dict ={'Schmidt':123, 'Krug':456, 'Hubert':987}
print(dict)
print(dict.keys())
print(dict.values())

# Eingaben
# name = input('Wie heißt Du?')
# print(' Ich grüße Dich, ', name)

# Wenn Dann Abfrage (if ...)
# age = input('Gib bitte Dein Alter ein: ')
# age = int(age)
# if age>= 18:
#     print('Du bist zum Konzert zugelassen')
# else:
#     print('Leider bist Du noch zu jung')

# Zählschleifen
studenten = ['Nina', 'Julia','Patrick', 'Lars','Max']
matr_nr = -1
for student in studenten:
    matr_nr = matr_nr + 1
    print(student,' hat die Matr-Nr: ',matr_nr)

# While-Schleife
wert = 1
while wert < 10:
    wert = wert + 2
    print(wert)

# Funktionen
def BerechneZ(x,y):
    z = 3*x**2+y
    return z
print(BerechneZ(1,2))

# Diagramm erstellen
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6,7,8])
y = x*x
plt.plot(x,y)
plt.show()

# Listenoperationen
a = [i/2 for i in x]
print(a)




