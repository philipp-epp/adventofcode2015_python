with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    #split each line by delimiter "x" and save first element of line in l, second in w, third in h
    split_list = line.split("x")
    l = int(split_list[0])
    w = int(split_list[1])
    h = int(split_list[2])
    #two smallest dimensions to wrap the present
    first_dim = min(l, w, h)
    if first_dim == l:
        second_dim = min(w, h)
    elif first_dim == w:
        second_dim = min(l, h)
    else:
        second_dim = min(w, l)
    #calculating sum by utilizing given calculation including ribbon for the bow
    sum += 2 * first_dim + 2 * second_dim + l * w * h
print(sum)
