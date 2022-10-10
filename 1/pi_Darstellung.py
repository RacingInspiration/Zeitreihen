# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:41:25 2021

Darstellung der Ziffern von Pi

"""
import turtle as tu

# lese die Datei pi.txt als Feld ein
with open('pi.txt','r') as pi_datei:
    pi = pi_datei.read()

# print(len(pi)) # zeige die Länge des Feldes pi
# print(pi[0:3]) # zeige die ersten 3 Ziffern
# print(pi[-10:0]) # zeigen die letzten 10 Ziffern 

# Initialisierung in Turtle
tu.mode('logo') # setze alles auf Null
tu.tracer(False) # schalte den Zeichenstift aus
tu.screensize(1500,1500,'black')
tu.pencolor('red')
tu.colormode(255) #Definiere Farbpalette von 0 bis 254

steps = 200_000 # Anzahl der darzustellenden Ziffern von pi
step_color = 255 / steps # Farbabstand zweier Ziffern (Achtung: Farbe darf letztendlich nur ein Integer Wert sein!)

for i in range(steps):
    ziffer = int(pi[i])
    winkel = 36 * ziffer
    
    farbe = int(step_color * i) # Farbwert des i-ten Zeichenschritts
    tu.pencolor(255-farbe,255-farbe, farbe)
    tu.setheading(winkel)
    tu.forward(2)
    if i % 10_000 == 0 :
        tu.update()
    
# turtle Zeichnung abschließen
tu.done()
