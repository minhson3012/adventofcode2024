import heapq

def challenge1(input):
    # Answer: 90440
    row = len(input)
    col = len(input[0])

    start = (row - 2, 1)
    end = (1, col - 2)

    directions = [((-1, 0)), (1, 0), (0, -1), (0, 1)] # up, down, left, right
    distance = [[[float('inf')] * 4 for _ in range(col)] for _ in range(row)]
    priority_queue = []

    for i in range(4):
        if(i == 3):
            distance[start[0]][start[1]][i] = 0
            heapq.heappush(priority_queue, (0, start[0], start[1], i))  # cost, x, y, direction
        else:
            distance[start[0]][start[1]][i] = float('inf')
            heapq.heappush(priority_queue, (float('inf'), start[0], start[1], i))  # cost, x, y, direction

    while priority_queue:
        curr_distance, x, y, curr_direction = heapq.heappop(priority_queue)

        if (x, y) == end:
            return curr_distance
        
        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            new_distance = curr_distance

            if(curr_direction != i):
                new_distance += 1001
            else:
                new_distance += 1

            if (0 <= new_x < row  and 0 <= new_y < col and input[new_x][new_y] != "#"):
                if(new_distance < distance[new_x][new_y][i]):
                    distance[new_x][new_y][i] = new_distance
                    heapq.heappush(priority_queue, (new_distance, new_x, new_y, i))

    return -1

def challenge2(input):
    # Answer: 479
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    rows, cols = len(input), len(input[0])
    start = (rows - 2, 1)
    end = (1, cols - 2)

    priority_queue = []
    dist = {}  # dist[(x, y, direction)] = cost

    heapq.heappush(priority_queue, (0, start[0], start[1], 0)) # (cost, x, y, direction)
    dist[(start[0], start[1], 0)] = 0

    paths = { (start[0], start[1], 0): [[start]] }
    while priority_queue:
        cost, x, y, direction = heapq.heappop(priority_queue)

        if (x, y) == end:
            break

        for new_direction, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy

            if not is_valid(new_x, new_y, input):
                continue

            new_cost = cost + 1
            if(direction != new_direction):
                new_cost += 1000

            if (new_x, new_y, new_direction) not in dist or dist[(new_x, new_y, new_direction)] > new_cost:
                dist[(new_x, new_y, new_direction)] = new_cost
                heapq.heappush(priority_queue, (new_cost, new_x, new_y, new_direction))

                paths[(new_x, new_y, new_direction)] = [path + [(new_x, new_y)] for path in paths[(x, y, direction)]]
            elif dist[((new_x, new_y, new_direction))] == new_cost:
                paths[(new_x, new_y, new_direction)].extend([path + [(new_x, new_y)] for path in paths[(x, y, direction)]])

    shortest_distance = float('inf')
    unique_paths = []

    for direction in range(4):
        if (end[0], end[1], direction) in dist:
            if dist[(end[0], end[1], direction)] < shortest_distance:
                shortest_distance = dist[(end[0], end[1], direction)]
                unique_paths = paths[(end[0], end[1], direction)]
            elif dist[(end[0], end[1], direction)] == shortest_distance:
                unique_paths.extend(paths[(end[0], end[1], direction)])

    points = set()
    for path in unique_paths:
        points.update(path)
    return len(points)

def is_valid(x, y, input):
    return 1 <= x < len(input) - 1 and 1 <= y < len(input[0]) - 1 and input[x][y] != "#"

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    return input_lines

def main():
    input = readFile("d:\\adventofcode2024\\day16\\input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

if __name__ == "__main__":
    main()