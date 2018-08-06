#!/usr/bin/env python3
import sympy as sym

# Eingabe der Funktion
funktion_str = input("Funktion eingeben: f(x)=")
f = sym.Symbol('f')
x = sym.Symbol('x')
f = eval(funktion_str)

# Bestimmung der Ableitungen
f1 = sym.diff(f, x, 1)
f2 = sym.diff(f, x, 2)
f3 = sym.diff(f, x, 3)

# Nullstellen
nullstellen = sym.solveset(f, x)


# Extremstellen / -punkte
extremstellen_mögl = list(sym.solveset(f1, x)) # Bestimme mögliche Extremstellen anhand notwendiger Bedingung f'(x)=0
extremstellen = {x0 for x0 in extremstellen_mögl if x0 not in sym.solveset(f2, x)}


# Wendestellen / -punkte
wendestellen_mögl = list(sym.solveset(f2, x)) # mögl. Wendest. anhand notwendiger Bedingung f''(x)=0
wendestellen = {x0 for x0 in wendestellen_mögl if x0 not in sym.solveset(f3, x)}
