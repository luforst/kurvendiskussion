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


# Extremstellen / -punkte


# Wendestellen / -punkte
