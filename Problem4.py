# Part 1
import re
f = open('Input4.txt', 'r')
data = f.read()
singlePasswords = data.split('\n\n')
valid_passwords = 0
for i in singlePasswords:

    temp = i.count(':')
    if temp == 8:
        valid_passwords += 1
    elif temp == 7:
        if not 'cid:' in i:
            valid_passwords += 1

print(valid_passwords)

# Part 2
clearedData = []
possibleValid = []
for password in singlePasswords:
    spliterino = ' '.join(' '.join(password.split('\n')).split(':')).split(' ')
    list1 = spliterino[::2]
    list2 = spliterino[1::2]
    z = dict(zip(list1, list2))
    clearedData.append(z)


for passport in clearedData:
    if len(passport) == 8:
        possibleValid.append(passport)
    elif len(passport) == 7 and not 'cid' in passport.keys():
        possibleValid.append(passport)

finalResult = []
for passport in possibleValid:
    if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
        if int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
            if int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                if re.fullmatch("^#([0-9a-f]{6})", passport['hcl']):
                    if re.fullmatch("(amb|blu|brn|gry|grn|hzl|oth)", passport['ecl']):
                        if re.fullmatch("^([0-9]{9})", passport['pid']):
                            if 'cm' in passport['hgt']:
                                test = passport['hgt'].split('c')
                                if int(test[0]) >= 150 and int(test[0]) <= 193:
                                    finalResult.append(passport)
                            if 'in' in passport['hgt']:
                                test = passport['hgt'].split('i')
                                if int(test[0]) >= 59 and int(test[0]) <= 76:
                                    finalResult.append(passport)

print(len(finalResult))
