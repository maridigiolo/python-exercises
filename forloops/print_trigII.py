size = int(input('Type a number as the height of the triangle: '))
max = size

for i in range(0, max):
	print (" " * size, "*" * (i * 2 +1))
	size = size - 1
	
	