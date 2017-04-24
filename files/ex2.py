fileex2 = open('ex2.txt', 'w')

contents = input('Type a input to your file: ')

fileex2.write(contents)
fileex2.close()

#to add the information instead of replace them, use the option 'a', instead of
#'w' or 'r' in name = open('name of the file', 'a')
