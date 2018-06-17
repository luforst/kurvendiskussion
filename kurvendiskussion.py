#!/usr/bin/env python3
import sympy as sym

# Eingabe der Funktion
funktion_str = input("Funktion eingeben: f(x)=")
f = sym.Symbol('(' + funktion_str + ')')

# Bestimmung der Ableitungen
x = sym.Symbol('x')
f1 = sym.diff(f, x, 1)
f2 = sym.diff(f, x, 2)
f3 = sym.diff(f, x, 3)

# Nullstellen


# Extremstellen / -punkte


# Wendestellen / -punkte
