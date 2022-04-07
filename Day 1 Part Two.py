with open("input.txt") as file:
    lines = file.readlines()

floor = 0
counter = 1
for line in lines[0]:
    if line == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(counter)
        break
    counter += 1