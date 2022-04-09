with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    #split each line by delimiter "x" and save first element of line in l, second in w, third in h
    split_list = line.split("x")
    l = int(split_list[0])
    w = int(split_list[1])
    h = int(split_list[2])
    smallest_side = min(l*w, w*h, h*l)
    #calculating sum by utilizing given calculation
    sum += 2 * l * w + 2 * w * h + 2 * h * l + smallest_side
print(sum)
