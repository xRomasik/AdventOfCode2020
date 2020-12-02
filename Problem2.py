# import requests
# response = requests.get('https://adventofcode.com/2020/day/2/input')
# print(response.reason)
# This didnt work out, because I didnt figure out how to login to the link with Python, so it gave me 400 Bad request all the time

f = open('Input2.txt', 'r')
data = f.read()
list_of_data = data.split('\n')

# Part 1


def split_by_space(string):
    return string.split(' ')


def checkPassword(checkFor, password, min1, max1):
    temp = 0
    for letter in password:
        if letter == checkFor:
            temp += 1
    if temp >= min1 and temp <= max1:
        return True
    else:
        return False


nestedList = list(map(split_by_space, list_of_data))
iterateList = nestedList.copy()

count = 0
for lister in iterateList:
    nestedList[count][0] = list(map(int, lister[0].split('-')))
    count += 1

result = 0
for lister in nestedList:
    result += checkPassword(lister[1][0], lister[2],
                            min(lister[0]), max(lister[0]))

print(result)

# Part 2


def checkPassword2(checkFor, password, pos1, pos2):
    temp = 0
    if password[pos1-1] == checkFor:
        temp += 1
    if password[pos2-1] == checkFor:
        temp += 1
    if temp == 1:
        return True
    else:
        return False


result2 = 0
for lister in nestedList:
    result2 += checkPassword2(lister[1][0], lister[2],
                              min(lister[0]), max(lister[0]))

print(result2)
