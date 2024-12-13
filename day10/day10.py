def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 644
    total = 0
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            trail_heads = set()
            if(input[i][j] == "0"):
                trail_heads.update(is_legit(i,j,input))
            total += len(trail_heads)
    return total

def challenge2(input):
    # Answer: 1366
    total = 0
    trail_heads = []
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            if(input[i][j] == "0"):
                trail_heads.append(is_legit(i,j,input))

    for i in range(0, len(trail_heads)):
        checked_points = {}
        for j in range(0, len(trail_heads[i])):
            if(trail_heads[i][j] not in checked_points):
                checked_points[trail_heads[i][j]] = 1
            else:
                checked_points[trail_heads[i][j]] += 1
        total += sum(checked_points.values())

    return total

def is_legit(v, h, point_list):
    if(int(point_list[v][h]) == 9):
        return (v,h)
    
    next_points = []
    if(v > 0 and int(point_list[v-1][h]) == int(point_list[v][h]) + 1):
        next_points.append((v-1, h))
    if(v < len(point_list) - 1 and int(point_list[v+1][h]) == int(point_list[v][h]) + 1):
        next_points.append((v+1, h))
    if(h > 0 and int(point_list[v][h-1]) == int(point_list[v][h]) + 1):
        next_points.append((v, h-1))
    if(h < len(point_list) - 1 and int(point_list[v][h+1]) == int(point_list[v][h]) + 1):
        next_points.append((v, h+1))
    
    if(len(next_points) == 0):
        return None

    current_list = []
    for point in next_points:
        end_point = is_legit(point[0], point[1], point_list)
        if(isinstance(end_point, tuple) and end_point != None):
            current_list.append(end_point)
        if(isinstance(end_point, list)):
            current_list += end_point
    return current_list

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()