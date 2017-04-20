
w = int(input('Give a width of your box: '))
h = int(input('Give a heigh of your box: '))

print ('*' * w)

for i in range (1, h-1):
	print('*' + (w - 2) * " " + '*')

	
print ('*' * w)

