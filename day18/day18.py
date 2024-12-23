import heapq

SIZE = 71
BYTE = 1024

def main():
    input, input_lines = readFile("d:\\adventofcode2024\\day18\\input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input_lines)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 264
    start = (0,0)
    end = (SIZE - 1, SIZE - 1)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = [(0, start[0], start[1])] # cost, y, x

    distances = [[float('inf')] * SIZE for _ in range(SIZE)]
    distances[start[0]][start[1]] = 0

    prev = [[None] * SIZE for _ in range(SIZE)]
    while priority_queue:
        cost, y, x = heapq.heappop(priority_queue)
        
        if (y, x) == end:
            path = []
            while (y, x) != start:
                path.append((y, x))
                y, x = prev[y][x]
            path.append(start)
            path.reverse()
            # print(path)
            return cost
        
        for (dy, dx) in directions:
            new_x = x + dx
            new_y = y + dy
            
            new_distance = cost + 1
            if(0 <= new_y < SIZE and 0 <= new_x < SIZE and input[y][x] != "#"):
                if(new_distance < distances[new_y][new_x]):
                    distances[new_y][new_x] = new_distance
                    prev[new_y][new_x] = (y, x)
                    heapq.heappush(priority_queue, (new_distance, new_y, new_x))
    
    return -1

def challenge2(lines):
    # Answer: 41,26
    possible_lines = []
    for i in range(0, len(lines)):
        current_point = (lines[i][1], lines[i][0])

        index = [i for i, item in enumerate(possible_lines) if current_point in item["points"]]
        if ((len(possible_lines) == 0 or len(index) == 0)):
            start_point = []

            if (current_point[0] == 0 or current_point[1] == 0 or
                current_point[0] == SIZE - 1 or current_point[1] == SIZE - 1):
                start_point.append(current_point)

            possible_lines.append({"start": start_point, "points": add_points(current_point)})
        elif len(index) == 1:
            curr_start = possible_lines[index[0]]["start"]
            if len(curr_start) > 0 and has_blocked(possible_lines[index[0]]["start"], current_point):
                return current_point
            
            possible_lines[index[0]]["points"] += add_points(current_point)
            if ((current_point[0] == 0 or current_point[1] == 0 or
                current_point[0] == SIZE - 1 or current_point[1] == SIZE - 1)):
                possible_lines[index[0]]["start"].append(current_point)
        elif len(index) > 1:
            new_lines = {"start": [], "points": [item for i in index for item in possible_lines[i]["points"]]}

            for i in index:
                if len(possible_lines[i]["start"]) > 0:
                    new_lines["start"] += possible_lines[i]["start"]
            
            if len(new_lines["start"]) > 0 and has_blocked(new_lines["start"], current_point):
                return current_point

            possible_lines = [item for i, item in enumerate(possible_lines) if i not in index]
            possible_lines.append(new_lines)

    return None

def has_blocked(start_points, current_point):
    for start_point in start_points:
        if(start_point == current_point):
            continue

        if (is_blocked(start_point, current_point)):
                return True
        
        if(len(start_points) > 0 and any(is_blocked(start_point, x) for x in start_points if x != start_point)):
            return True
    return False

def is_blocked(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    return ((y1 == 0 and (x2 == 0 or y2 == SIZE - 1)) or
            (y1 == SIZE - 1 and (y2 == 0 or x2 == SIZE - 1)) or
            (x1 == 0 and (x2 == SIZE - 1 or y2 == 0)) or
            (x1 == SIZE - 1 and (x2 == 0 or y2 == SIZE - 1)))

def add_points(curr_point):
    y, x = curr_point
    points = [
        (y - 1, x - 1),
        (y - 1, x),
        (y - 1, x + 1),
        (y, x - 1),
        (y, x + 1),
        (y + 1, x - 1),
        (y + 1, x),
        (y + 1, x + 1),
        (y, x)
    ]

    return [item for item in points if 0 <= item[0] < SIZE and 0 <= item[1] < SIZE]
    
def readFile(filename):
    file = open(filename, "r")

    input_lines = []
    for line in file.read().splitlines():
        line_split = line.split(",")
        input_lines.append((int(line_split[0]), int(line_split[1])))
    file.close()

    input = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(BYTE):
        current_item = input_lines[i]
        input[current_item[1]][current_item[0]] = "#"

    return input, input_lines

if __name__ == "__main__":
    main()