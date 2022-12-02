import re

passports = [x.rstrip() for x in open("input-04.txt").read().split('\n\n')]

required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
complete_passports = 0

complete_passport_list = []

for passport in passports:
    valid = True
    for field in required_fields:
        if not field in passport:
            valid = False
    if valid:
        complete_passports += 1
        complete_passport_list.append(passport)


def check_passport(passport):
    passport = (passport.replace('\n\n', '\n')).replace('\n', " ")
    fields = [x.split(':') for x in passport.split(' ')]
    passport = {x[0]: x[1] for x in fields}
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False
    if not re.search('^#[a-f0-9]{6}$', passport['hcl']):
        return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not len(passport['pid']) == 9 or not passport['pid'].isnumeric():
        return False
    return True


valid_passports = 0
for passport in complete_passport_list:
    if check_passport(passport):
        valid_passports += 1


print(f"Part 1: {complete_passports}")
print(f"Part 2: {valid_passports}")
