# -*- coding: utf-8 -*-
"""
Einführung in Python
"""

# Bibliotheken importieren
# Hinweis: erstmalige Installation von Biblotheken: pip install namederbibliothek
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Das ist das erste Py-Programm und beginnt wie üblich mit "Hello World"
Nachricht="Hello World"
print(Nachricht)

# Strings verbinden
first_name = "Albert "
second_name = "Einstein"
full_name = first_name + second_name
print(full_name)

# Liste erstellen
bikes = ['citybike','mountainbike','racing bike','e-bike']
bikes.append('kids_bike')
print(bikes)

# Mathematische Operationen
a = 4
print(type(a))
b = 2.1
komplex = b+3j
print(komplex.imag)
pruefung = 4 > 3

# Wörterbuch
dict = {'Schmidt':491524364764,'Steingruber':4962544334,'Rübenau':49625242343}
print(dict.keys())
print(dict.values())

# Benutzereingaben
frage = "Wie alt bis Du?"
alter = input(frage)
print("Das Alter ist ",alter," Jahre")

# Wenn Abfragen
alter = int(alter)
if alter > 18:
    print('Du bist ein Erwachsener')
elif alter == 18:
    print('Du bist gerade so erwachsen ;-)')
else:
    print('Du bist ein Kind')

# Schleife (Zählschleife oder andere Schleife)
studenten = ['Niklas','Jana','Hannes','Sebastian','Mara']
j = 0

for student in studenten:
    print(student + ' hat die Matrikelnr. ',j)
    j = j + 5

# While Schleifen
wert = 1
while wert < 10:
    print(wert)
    wert = wert + 1
    
# Funktionen y(x)=cos(x)
a = 3
def y(x):
    return np.cos(x) 

# Diagramm erstellen
x = np.linspace(0,10,100)
plt.plot(x,y(x))

    




