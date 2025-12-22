def partTwo(filename):
    result = 0
    ranges = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            s, e = int(line[:line.index('-')]), int(line[line.index('-')+1:])
            ranges.append([s,e])
    # sort all ranges by start
    ranges = sorted(ranges, key=lambda item: item[0])
    for i in range(len(ranges)-1):
        if ranges[i][1] > ranges[i+1][0]:
            ranges[i+1][0] = ranges[i][1] + 1
        result += ranges[i][1] - ranges[i][0] + 1
    return result

print(partTwo('exp2.txt'))

