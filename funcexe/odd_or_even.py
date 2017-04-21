#!/usr/bin/env python3

import matplotlib.pyplot as plot

def f(x):
	if x % 2 != 0:
		return 1
	if x % 2 == 0:
		return -1
	
xs = list(range(-5, 5, 1))
ys = []
for x in xs:
	ys.append(f(x))
		
print(xs)
print(ys)
plot.bar(xs, ys)
plot.show()
