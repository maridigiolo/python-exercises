file_name = input('Enter a file name that you want to work on: ')

fileex1 = open(file_name, 'r')

filecontents = fileex1.read()
fileex1.close()

print(filecontents)
