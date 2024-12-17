def main():
    input = readFile("input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 1477924
    plants = []

    for i in range(0, len(input)):
        for j in range(0, len(input[i])):

            current_index = get_index(i, j, input, plants)
            if(current_index == -1):
                plants.append({"type": input[i][j], "area": 0, "params": 0, "next": set()})
                plants[-1]["next"], _ = get_next_points(i,j,input)

            params = get_params(i, j, input)

            plants[current_index]["area"] += 1
            plants[current_index]["params"] += params
    
    
    total = 0

    for plant in plants:
        print(plant["type"], plant["area"], plant["params"], plant["next"])
        total += plant["area"] * plant["params"]
            
    return total

def challenge2(input):
    # Answer: 841934
    plants = []

    for i in range(0, len(input)):
        for j in range(0, len(input[i])):

            current_index = get_index(i, j, input, plants)
            if(current_index == -1):
                plants.append({"type": input[i][j], "area": 0, "next": set(), "sides": 0})
                plants[-1]["next"], plants[-1]["sides"] = get_next_points(i,j,input)

            plants[current_index]["area"] += 1
    
    total = 0

    for plant in plants:
        print(plant["type"], plant["area"], plant["sides"])
        total += plant["area"] * plant["sides"]
            
    return total

def get_index(h, v, input, plants):
    current_type = input[h][v]

    for index, plant in enumerate(plants):
        has_up_point = h > 0 and (h-1,v) in plant["next"]
        has_left_point = v > 0 and (h, v-1) in plant["next"]
        has_down_point = h < len(input) - 1 and (h+1,v) in plant["next"]
        has_right_point = v < len(input) - 1 and (h,v+1) in plant["next"]

        if(plant["type"] == current_type and ((h,v) in plant["next"] or has_up_point
            or has_down_point or has_left_point or has_right_point)):
            plant["next"].add((h,v))
            return index
    
    return -1

def get_next_points(h, v, input):
    current_type = input[h][v]

    stack = [(h,v)]
    next_points = set()
    neighbors = set()
    total_sides = 0
    while stack:
        point = stack.pop()
        if(point and point not in next_points):
            next_points.add(point)
            neighbors_direction = [0] * 4 # up, left, down, right

            # Check next type
            if(point[0] > 0 and input[point[0]-1][point[1]] == current_type and (point[0]-1,point[1]) not in next_points):
                stack.append((point[0]-1,point[1]))
            if(point[1] > 0 and input[point[0]][point[1]-1] == current_type and (point[0],point[1]-1) not in next_points):
                stack.append((point[0],point[1]-1))
            if(point[0] < len(input) - 1 and input[point[0]+1][point[1]] == current_type and (point[0]+1,point[1]) not in next_points):
                stack.append((point[0]+1,point[1]))
            if(point[1] < len(input) - 1 and input[point[0]][point[1]+1] == current_type and (point[0],point[1]+1) not in next_points):
                stack.append((point[0],point[1]+1))

            # Check corners
            if(point[0] == 0):
                neighbors_direction[0] = 1
            else:
                next_point = input[point[0]-1][point[1]]
                left = None if point[1] == 0 else input[point[0]-1][point[1]-1]
                right = None if point[1] == len(input) - 1 else input[point[0]-1][point[1]+1]

                is_corner = next_point != current_type and (left == current_type or right == current_type)
                if(next_point != current_type and (point[0]-1,point[1]) not in neighbors):
                    neighbors.add((point[0]-1,point[1]))
                    neighbors_direction[0] = 1
                elif(next_point != current_type):
                    neighbors_direction[0] = 2
                    if(is_corner):
                        total_sides += 1

            if(point[1] == 0):
                neighbors_direction[1] = 1
            else:
                next_point = input[point[0]][point[1]-1]
                up = None if point[0] == 0 else input[point[0]-1][point[1]-1]
                down = None if point[0] == len(input) - 1 else input[point[0]+1][point[1]-1]

                is_corner = next_point != current_type and (up == current_type or down == current_type)
                if(next_point != current_type and (point[0],point[1]-1) not in neighbors):
                    neighbors.add((point[0],point[1]-1))
                    neighbors_direction[1] = 1
                elif(next_point != current_type):
                    neighbors_direction[1] = 2
                    if(is_corner):
                        total_sides += 1

            if(point[0] == len(input) - 1):
                neighbors_direction[2] = 1
            else:
                next_point = input[point[0]+1][point[1]]
                left = None if point[1] == 0 else input[point[0]+1][point[1]-1]
                right = None if point[1] == len(input) - 1 else input[point[0]+1][point[1]+1]

                is_corner = next_point != current_type and (left == current_type or right == current_type)
                if(next_point != current_type and (point[0]+1,point[1]) not in neighbors):
                    neighbors.add((point[0]+1,point[1]))
                    neighbors_direction[2] = 1
                elif(next_point != current_type):
                    neighbors_direction[2] = 2
                    if(is_corner):
                        total_sides += 1

            if(point[1] == len(input) - 1):
                neighbors_direction[3] = 1
            else:
                next_point = input[point[0]][point[1]+1]
                up = None if point[0] == 0 else input[point[0]-1][point[1]+1]
                down = None if point[0] == len(input) - 1 else input[point[0]+1][point[1]+1]

                is_corner = next_point != current_type and (up == current_type or down == current_type)
                if(next_point != current_type and (point[0],point[1]+1) not in neighbors):
                    neighbors.add((point[0],point[1]+1))
                    neighbors_direction[3] = 1
                elif(next_point != current_type):
                    neighbors_direction[3] = 2
                    if(is_corner):
                        total_sides += 1

            true_index = [index for index, value in enumerate(neighbors_direction) if value > 0]
            if(len(true_index) == 4):
                total_sides += 4
            elif(len(true_index) == 3):
                total_sides += 2
            elif(len(true_index) == 2 and true_index[1] - true_index[0] != 2):
                total_sides += 1

            doubled_index = [index for index, value in enumerate(neighbors_direction) if value > 1]
            if(len(doubled_index) > 1):
                for i in range(0, len(doubled_index) - 1):
                    if(doubled_index[i+1] - doubled_index[i] != 2):
                        point = get_last_point(point, doubled_index[i], doubled_index[i+1])
                        if(point in next_points):
                            total_sides -= 2

    return next_points, total_sides

def get_last_point(base_point, direction_1, direction_2):
    point_1, point_2 = None, None
    if(direction_1 == 0):
        point_1 = (base_point[0] - 1, base_point[1])
    elif(direction_1 == 1):
        point_1 = (base_point[0], base_point[1] - 1)
    elif(direction_1 == 2):
        point_1 = (base_point[0] + 1, base_point[1])
    elif(direction_1 == 3):
        point_1 = (base_point[0], base_point[1] + 1)

    if(direction_2 == 0):
        point_2 = (base_point[0] - 1, base_point[1])
    elif(direction_2 == 1):
        point_2 = (base_point[0], base_point[1] - 1)
    elif(direction_2 == 2):
        point_2 = (base_point[0] + 1, base_point[1])
    elif(direction_2 == 3):
        point_2 = (base_point[0], base_point[1] + 1)

    y1, x1 = point_1
    y2, x2 = base_point
    y3, x3 = point_2

    # Calculate the midpoint of diagonal AC
    midpoint_AC = ((y1 + y3) / 2, (x1 + x3) / 2)

    # Calculate the fourth point D using vector addition (adjusting for (y, x) coordinates)
    y4 = 2 * midpoint_AC[0] - y2
    x4 = 2 * midpoint_AC[1] - x2

    return (int(y4), int(x4))

def get_params(h, v, input):
    current_type = input[h][v]
    params = 0

    if(h == 0 or input[h-1][v] != current_type):
        params += 1

    if(h == len(input) - 1 or input[h+1][v] != current_type):
        params += 1

    if(v == 0 or input[h][v-1] != current_type):
        params += 1

    if(v == len(input) - 1 or input[h][v+1] != current_type):
        params += 1
    return params

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()