# Part 1
# Convert input into usable data
import operator
import functools

f = open('input3.txt', 'r')
data = f.read()
list_of_data = data.split('\n')
# Move 3 right, 1 down, chekc if its a # add +1 or +0
right = 3
down = 1
number_of_trees = 0
end_of_side = len(list_of_data[0])
end_of_map = len(list_of_data)
# Loop trough the map
for index in range(1, end_of_map):
    print(down, right, end_of_side)
    if list_of_data[down][right] == '#':
        number_of_trees += 1
        print('Kaboom, you got hit by a huge tree!')
    down += 1
    right += 3
# If we reach end of a row, start again
    if right >= end_of_side:
        right = right - end_of_side
print(f'{number_of_trees} Olaaa')

# Part 2
number_of_trees = 0
hit_list = []
increment_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for slope in increment_list:
    r_increment = slope[0]
    d_increment = slope[1]
    right = slope[0]
    down = slope[1]
    print('-------------------------HEY-------------------------')
    if down == 2:
        end_of_map = round(end_of_map/2)
    for index in range(1, end_of_map):
        print(down+1, right, end_of_side)
        if list_of_data[down][right] == '#':
            number_of_trees += 1
            print('Kaboom, you got hit by a huge tree!')
        down += d_increment
        right += r_increment
        if right >= end_of_side:
            right = right - end_of_side
    hit_list.append(number_of_trees)
    number_of_trees = 0

print(hit_list)
result2 = functools.reduce(operator.mul, hit_list)
print(result2)
