#!/usr/bin/env python3

import matplotlib.pyplot as plot
import math

def f(x):
	return math.sin(x)

xs = list(range(-5, 5))
ys = []
for x in xs:
	ys.append(f(x))

print (xs)
print (ys)

plot.plot(xs, ys)
plot.show()