def partOne(file):
    i = 0
    ranges = set()
    inputs = []
    for line in file:
        line = line.strip()
        if line != '' and '-' in line:
            ranges.add((int(line[:line.index('-')]), int(line[line.index('-')+1:])))
        elif line != '':
            inputs.append(int(line))
    result = 0
    for n in inputs:
        for r in ranges:
            s, e = r
            if n >= s and n <= e:
                result += 1
                break
    return result

def partTwo(file):
    result = 0
    inputs = []
    ranges = []
    for line in file:
        line = line.strip()
        if line != '' and '-' in line:
            ranges.append((int(line[:line.index('-')]), int(line[line.index('-')+1:])))
        elif line != '':
            inputs.append(int(line))
    ranges.sort(key=lambda item: item[0])

    for i in range(len(ranges)):
        s, e = ranges[i]
        result += e - s + 1
        if i < len(ranges)-1:
            sn, en = ranges[i+1]
            if e > sn:
                result -= (e - sn + 1)
    for n in inputs:
        found = 0
        for r in ranges:
            s, e = r
            if n >= s and n <= e:
                found = 1
                break
        if found == 0:
            result += 1


    return result


with open('input.txt', 'r') as file:
    print(f"part one solution: {partOne(file)}")
print("----------------------------------")
with open('input.txt', 'r') as file:
    print(f"part two solution: {partTwo(file)}")

