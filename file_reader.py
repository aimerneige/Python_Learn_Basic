with open('pi_digits.txt') as file_obj:
    contens = file_obj.read()
    print(contens.rstrip())

with open('pi_digits.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())

with open('pi_digits.txt') as file_obj:
    for sss in file_obj:
        print(sss.rstrip())

with open('pi_digits.txt') as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())
