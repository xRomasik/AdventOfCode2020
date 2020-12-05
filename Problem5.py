f = open('Input5.txt', 'r')
data = f.read()
list_of_data = data.split('\n')

minRow = 0
maxRow = 127
minCol = 0
maxCol = 7

correctRow = 0
results = []
results2 = []
for i in list_of_data:
    index = 0
    for o in i:
        index += 1
        if o == 'F':
            maxRow = maxRow - round((maxRow-minRow)/2)
            if index == 7:
                results.append(minRow)
        elif o == 'B':
            minRow = minRow + round((maxRow-minRow)/2)
            if index == 7:
                results.append(maxRow)
        elif o == 'R':
            minCol = minCol + round((maxCol-minCol)/2)
            if index == 10:
                # results.append(maxCol)
                hoho = results[-1] * 8 + maxCol
                results2.append(hoho)
        elif o == 'L':
            maxCol = maxCol - round((maxCol-minCol)/2)
            if index == 10:
                # results.append(minCol)
                hoho = results[-1] * 8 + minCol
                results2.append(hoho)
    minCol = 0
    maxCol = 7
    minRow = 0
    maxRow = 127
# print(results)
print('Highest ID')
print(max(results2))
hola = sorted(results2)
# print(hola)


def sereMeTo():
    indux = 1
    for i in hola:
        if int(i) + 1 != hola[indux]:
            return i+1
        indux += 1

    print(hola)


print('My Id')
print(sereMeTo())
