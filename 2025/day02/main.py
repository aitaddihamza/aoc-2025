def partOne():
    with open("input.txt", "r") as file:
        content = file.read().strip() # supprimer \n
        # print(content.split(",")) # retourne un array of ranges
        ranges = content.split(",")
        outpout = 0
        for r in ranges:
            start, end = r.split("-")
            for i in range(int(start), int(end) + 1):
                j = str(i)
                if len(j) % 2 == 0:
                    if j[:(len(j) // 2)] == j[len(j) // 2:]:
                        outpout += i
        return outpout


def partTwo():
    with open("input.txt", "r") as file:
        content = file.read().strip() # supprimer \n
        ranges = content.split(",")
        outpout = 0
        for r in ranges:
            start, end = r.split("-")
            for i in range(int(start), int(end) + 1):
                j = str(i)
                for w in range(1, (len(j) // 2) + 1):
                    if len(j) % w == 0:
                        if j.count(j[:w]) == len(j) // w:
                            outpout += i
                            break
        return outpout


print(partOne())
# print(partTwo())
