MIN_LENGTH = 100
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

def main():
    paths = readFile("input.txt")
    # challenge1_result = challenge1(paths)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(paths)
    print("Challenge 2: ", challenge2_result)

def challenge1(paths):
    # Answer: 1463
    shortcuts = {}
    for i in range(MIN_LENGTH, len(paths)):
        x, y = paths[i]
        for j in range(4):
            dx, dy = DIRECTIONS[j]

            new_point = (x + 2 * dx, y + 2 * dy)
            index = [point_index for point_index, value in enumerate(paths) if value == new_point and point_index < i and i - point_index > MIN_LENGTH]

            if len(index) == 1:
                new_path = paths[:index[0]] + paths[i:]
                
                if len(new_path) != len(paths):
                    saved_steps = len(paths) - len(new_path) - 1
                    if saved_steps not in shortcuts:
                        shortcuts[saved_steps] = 1
                    else:
                        shortcuts[saved_steps] += 1

    return sum([shortcuts[x] for x in shortcuts if x >= MIN_LENGTH])

def challenge2(paths):
    # Answer: 985332
    shortcuts = {}

    for i in range(MIN_LENGTH, len(paths)):
        x, y = paths[i]

        indexes = [point_index for point_index, value in enumerate(paths) if point_index < i and abs(value[0] - x) + abs(value[1] - y) <= 20
                   and i - point_index - abs(value[0] - x) - abs(value[1] - y) >= MIN_LENGTH]
        
        for index in indexes:
            cx, cy = paths[index]

            new_path = paths[:index] + paths[i:]
            if len(new_path) != len(paths):
                saved_steps = len(paths) - (len(new_path) + abs(x - cx) + abs(y - cy))
                if saved_steps < MIN_LENGTH:
                    continue

                if saved_steps not in shortcuts:
                    shortcuts[saved_steps] = 1
                else:
                    shortcuts[saved_steps] += 1
    print(shortcuts)
    return sum([shortcuts[x] for x in shortcuts if x >= MIN_LENGTH])

# Returns index, remaining length in said index
def get_index(paths, point, current_index, cur_length):
    for index, value in enumerate(paths[:current_index]):
        start = value["start"]
        direction = value["direction"]
        length = value["length"]

        if ((start[0] == point[0] and direction[1] != 0 and (point[1] - start[1]) // direction[1] < length)):
            return (index, length - 1 - (point[1] - start[1]) // direction[1], cur_length)
        
        if ((start[1] == point[1] and direction[0] != 0 and (point[0] - start[0]) // direction[0] < length)):
            return (index, length - 1 - (point[0] - start[0]) // direction[0], cur_length)

    return None

def is_valid_point(point, max_length):
    return 1 <= point[0] < max_length - 1 and 1 <= point[1] < max_length - 1

def setup_path(input, start, end):
    cur_point = start
    paths = []
    while cur_point != end:
        x, y = cur_point

        for i in range(4):
            dx, dy = DIRECTIONS[i]

            if (is_valid_point((x+dx, y+dy), len(input)) 
                and (input[x+dx][y+dy] == "." or input[x+dx][y+dy] == "E")
                and (x+dx, y+dy) not in paths):
                paths.append(cur_point)
                cur_point = (x+dx, y+dy)
                break
    
    paths.append(end)
    return paths

def is_valid_point(point, max_len):
    return 1 <= point[0] < max_len - 1 and 1 <= point[1] < max_len - 1


def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    start, end = None, None
    for i in range(0, len(input_lines)):
        for j in range(0, len(input_lines[i])):
            if input_lines[i][j] == "S":
                start = (i, j)
            elif input_lines[i][j] == "E":
                end = (i, j)

    paths = setup_path(input_lines, start, end)
    return paths

if __name__ == "__main__":
    main()