a = [[1, 3, 7], [2, 4, 8], [5, 6, 9]]

b = [[5, 2, 7], [1, 0, 4], [1, 2, 3]]

list = []

for i in range(0, len(a)):
	new_list = []
	for j in range(0, len(b)):
		new_list.append(a[i][j] + b[i][j])
		
	list.append(new_list)		

for line in list:
	for item in line:
		print(item, end=" ")
		
	print("")