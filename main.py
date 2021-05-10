x = input('type something you want written to the file:')
with open('myFile.txt', 'w') as myFile:
    myFile.write(x)
y = open('myFile.txt', 'r')
print(y.read())
