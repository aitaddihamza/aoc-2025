def partOne():
    password = 0
    position = 50
    with open("exp1.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction = line[0] # right or left
            distance = int(line[1:])

            if direction == "L":
                position = (position - distance) % 100
            else:
                position = (position + distance) % 100
            if position == 0:
                password+=1
    return password

def partTwo():
    password = 0
    position = 50  # position de départ

    with open("exp1.txt", "r") as file:
        for line in file:
            line = line.strip()
            direction = line[0]  # 'L' ou 'R'
            distance = int(line[1:])

            # Simuler chaque clic
            for _ in range(distance):
                if direction == "L":
                    position = (position - 1) % 100
                else:  # 'R'
                    position = (position + 1) % 100

                if position == 0:
                    password += 1

    return password

print(partTwo())

print(f"parte one: {partOne()}")
print(f"parte two: {partTwo()}")
