# Part 1
f = open('Input6.txt', 'r')
data = f.read()
groups = data.split('\n\n')
result = 0
for group in groups:
    new = set(''.join(group.split('\n')))
    result += len(new)
    # print('---------') - Printing lines for better visualization of data
    # print(new)
print(f'Part 1 answer is {result}!')

# Part 2
result2 = 0
for group in groups:
    tempList = group.split('\n')
    lengthTempList = len(tempList)
    # Setting 1st set, then comparing it with another set from same group,
    # changing the set and comparing the new set again.
    # Finally measuring how lenght of that set and adding it to the results.
    comparer = set(tempList[0])
    for iteration in range(lengthTempList-1):
        comparer = comparer.intersection(set(tempList[iteration + 1]))
    result2 += len(comparer)

print(f'Part 2 answer is {result2}!')
