word = "Women"

long = " "
for i in word:
	if i not in 'aeiou':
		long = long + i
	if i in 'aeiou':
		long = long + (5*i)
	
print (long)
	
		
		