def partOne():
    result = 0
    with open("input.txt", "r") as file:
        for line in file:
            mx = int(line[:2])
            for i in range(len(line)):
                for j in range(i+1, len(line) - 1):
                    if mx < int(line[i] + line[j]):
                        mx = int(line[i] + line[j])
            result += mx
    return result


def find_max_index(nums: str, s: int, e: int):
    mx_idx = s
    for i in range(s, e):
        if int(nums[i]) > int(nums[mx_idx]):
            mx_idx = i
    return mx_idx



def partTwo():
    result = 0
    with open("exp.txt", "r") as file:
        for line in file:
            fs = find_max_index(line, 0, len(line) - 12)
            # '911112111'
            # line[fs = 6] = 9
            mx = line[fs] # mx = '9'
            for i in range(11):
                t = find_max_index(line, fs+i,len(line)-11+i)
                mx += line[t]
                print(t)

    return result


print(partOne())
# print(partTwo())
