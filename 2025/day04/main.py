def partOne(filename):
    s = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            for _, v in enumerate(line):
                if v == 'x':
                    s += 1
    return s


# print(partOne("exp.txt"))
print(partOne("input.txt"))
