def find_index(line: str,start: int, end: int):
    mx = start
    for i in range(start, end):
        if int(line[mx]) < int(line[i]):
            mx = i
    return mx


def partTwo(filename):
    result = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            w = 12
            f = find_index(line, 0, len(line) - w + 1)
            mx = line[f]
            for i in range(1, w):
                f = find_index(line, f+1, len(line) - (w - i) + 1)
                mx += line[f]
            result += int(mx)
    return result

x = '89828283'
# print(f"index: {find_index(x, 0, len(x)} => {x[find_index(x, 0, len(x)]}")
print(f"exp: {partTwo('exp.txt')}")
print(f"input: {partTwo('input.txt')}")
