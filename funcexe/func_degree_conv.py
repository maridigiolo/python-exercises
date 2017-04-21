#!/usr/bin/env python3

import matplotlib.pyplot as plot

def f(x):
	return x * 1.8 + 32

C = list(range(-10, 45, 2))
F =  []

for x in C:
	F.append(f(x))

plot.plot(C, F)
plot.show()