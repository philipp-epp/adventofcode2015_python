with open("input.txt") as file:
    lines = file.readlines()

floor = 0
for line in lines[0]:
    if line == "(":
        floor += 1
    else:
        floor -= 1
print(floor)
