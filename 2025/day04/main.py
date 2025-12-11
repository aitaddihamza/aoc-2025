def create_2d_array(filename):
    content = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            content.append(line)
    return content


def partOne(filename):
    content = create_2d_array(filename)
    s = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == '@':
                total_neighbors = 0
                if i - 1 >= 0 and j - 1 >= 0 and content[i-1][j-1] == '@':
                    total_neighbors += 1
                if i - 1 >= 0 and content[i-1][j] == '@':
                    total_neighbors += 1
                if i - 1 >= 0 and j+1 <= len(content[i]) - 1 and content[i-1][j+1] == '@':
                    total_neighbors += 1

                if j - 1 >= 0 and content[i][j-1] == '@':
                    total_neighbors += 1
                if j + 1 <= len(content[i]) - 1 and content[i][j+1] == '@':
                    total_neighbors += 1

                if i + 1 <= len(content) - 1 and j - 1 >= 0 and content[i+1][j-1] == '@':
                    total_neighbors += 1
                if i + 1 <= len(content) - 1 and content[i+1][j] == '@':
                    total_neighbors += 1
                if i + 1 <= len(content) - 1 and j+1 <= len(content[i]) - 1 and content[i+1][j+1] == '@':
                    total_neighbors += 1

                if total_neighbors < 4 and total_neighbors > 0: 
                    s += 1

    return s


def partOne_v2(filename):
    content = create_2d_array(filename)
    s = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == '@':
                total_neighbors = 0
                for k in range(-1, 2):
                    for z in range(-1, 2):
                        if i + k < 0 or i +k >= len(content): 
                            break
                        if i + k >= 0 and i + k < len(content) \
                                and j + z >= 0 and j + z < len(content[i]):
                            if content[i+k][j+z] == '@':
                                total_neighbors += 1
                if total_neighbors <= 4 and total_neighbors > 0: 
                    s += 1
    return s


def updateGrid(content, positions):
    new_content = []
    for i in range(len(content)):
        line = ''
        for j in range(len(content[i])):
            if (i,j) in positions:
                line+='.'
            else:
                line+=content[i][j]
        new_content.append(line)
    return new_content


def get_positions_and_sum(content):
    positions = set()
    s = 0
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] == '@':
                total_neighbors = 0
                for k in range(-1, 2):
                    for z in range(-1, 2):
                        if i + k < 0 or i +k >= len(content): 
                            break
                        if i + k >= 0 and i + k < len(content) \
                                and j + z >= 0 and j + z < len(content[i]):
                            if content[i+k][j+z] == '@':
                                total_neighbors += 1
                if total_neighbors <= 4 and total_neighbors > 0: 
                    s += 1
                    positions.add((i, j))
    return (positions, s)
def partTwo(filename):
    content = create_2d_array(filename)
    positions = set()
    r = 0
    s = 1
    while s > 0:
        positions, s = get_positions_and_sum(content)
        content = updateGrid(content, positions)
        r += s
    return r

# print(partOne('exp.txt'))
positions = {}
# print(partOne('input.txt'))
print(partTwo('input.txt'))
