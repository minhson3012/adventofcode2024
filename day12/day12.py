def main():
    input = readFile("d:\\adventofcode2024\\day12\\input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    # challenge2_result = challenge2(input)
    # print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 1477924
    plants = []

    for i in range(0, len(input)):
        for j in range(0, len(input[i])):

            current_index = get_index(i, j, input, plants)
            if(current_index == -1):
                plants.append({"type": input[i][j], "area": 0, "params": 0, "next": set()})
                plants[-1]["next"] = get_next_points(i,j,input)

            params = get_params(i, j, input)

            plants[current_index]["area"] += 1
            plants[current_index]["params"] += params
    
    
    total = 0

    for plant in plants:
        print(plant["type"], plant["area"], plant["params"], plant["next"])
        total += plant["area"] * plant["params"]
            
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
    while stack:
        point = stack.pop()
        if(point):
            next_points.add(point)
            if(point[0] > 0 and input[point[0]-1][point[1]] == current_type and (point[0]-1,point[1]) not in next_points):
                stack.append((point[0]-1,point[1]))
            if(point[1] > 0 and input[point[0]][point[1]-1] == current_type and (point[0],point[1]-1) not in next_points):
                stack.append((point[0],point[1]-1))
            if(point[0] < len(input) - 1 and input[point[0]+1][point[1]] == current_type and (point[0]+1,point[1]) not in next_points):
                stack.append((point[0]+1,point[1]))
            if(point[1] < len(input) - 1 and input[point[0]][point[1]+1] == current_type and (point[0],point[1]+1) not in next_points):
                stack.append((point[0],point[1]+1))

    return next_points

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