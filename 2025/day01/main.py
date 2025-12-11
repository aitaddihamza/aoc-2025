def partOne():
    c = 0
    p = 50
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "L" in line:
                d = line.replace("L", "")
                d = int(d)
                if d > 100:
                    d = d % 100
                r = (p - d) 
                if r < 0:
                    p = 100 - r
                else: 
                    p = r
            else:
                d = line.replace("R", "")
                d = int(d)
                if d > 100:
                    d = d % 100
                r = (p + d)
                if r >= 100:
                    p += d - 100
                else:
                    p+=d
            if p == 0:
                c+=1
    return c


def partTwo():
    c = 0
    p = 50
    with open("exp1", "r") as file:
        for line in file:
            line = line.strip()
            nbr_r = 0
            if "L" in line:
                d = line.replace("L", "")
                d = int(d)
                if d > 100:
                    nbr_r = d // 100
                    d = d - (nbr_r * 100) # 450 - 400 = 50
                p = (p - d) % 100
            else:
                d = line.replace("R", "")
                d = int(d)
                if d > 100:
                    nbr_r = d // 100
                    d = d - (nbr_r * 100) # 450 - 400 = 50
                p = (p + d) % 100
            if p == 0:
                c+=1
            if nbr_r > 0:
                c+=nbr_r
    return c

# print(f"part one: {partOne()}")
print(f"part two: {partTwo()}")



