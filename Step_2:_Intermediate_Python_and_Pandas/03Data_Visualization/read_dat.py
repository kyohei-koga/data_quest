for line in open('2002FemPreg.dat'):
    itemList = line.split('\t')
    numbers = [ item for item in itemList ]
print numbers[0]
