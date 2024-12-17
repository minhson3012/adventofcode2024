def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 225552000
    quadrants_width = 50
    quadrants_height = 51

    list_of_points = {}
    for i in range(0, len(input)):
        points = input[i].split()
        x1, y1 = [int(x) for x in points[0].split(",")]
        x2, y2 = [int(x) for x in points[1].split(",")]

        final_point = ((x1 + 100 * x2) % (quadrants_width * 2 + 1), (y1 + 100 * y2) % (quadrants_height * 2 + 1))
        if(final_point not in list_of_points):
            list_of_points[final_point] = 1
        else:
            list_of_points[final_point] += 1

    quad_1_points = sum([list_of_points[x] for x in list_of_points if x[0] <= (quadrants_width - 1) and x[1] <= (quadrants_height - 1)])
    quad_2_points = sum([list_of_points[x] for x in list_of_points if x[0] >= (quadrants_width + 1) and x[1] <= (quadrants_height - 1)])
    quad_3_points = sum([list_of_points[x] for x in list_of_points if x[0] <= (quadrants_width - 1) and x[1] >= (quadrants_height + 1)])
    quad_4_points = sum([list_of_points[x] for x in list_of_points if x[0] >= (quadrants_width + 1) and x[1] >= (quadrants_height + 1)])

    quads = [quad_1_points, quad_2_points, quad_3_points, quad_4_points]
    safety_factor = 1
    for i in range(0, len(quads)):
        if(quads[i] != 0):
            safety_factor *= quads[i]
    return safety_factor

def challenge2(input):
    # Answer: 7371
    quadrants_width = 50
    quadrants_height = 51

    should_continue = True
    current_iter = 1
    while(should_continue):
        list_of_points = {}
        for i in range(0, len(input)):
            points = input[i].split()
            x1, y1 = [int(x) for x in points[0].split(",")]
            x2, y2 = [int(x) for x in points[1].split(",")]

            final_point = ((x1 + current_iter * x2) % (quadrants_width * 2 + 1), (y1 + current_iter * y2) % (quadrants_height * 2 + 1))
            if(final_point not in list_of_points):
                list_of_points[final_point] = 1
            else:
                list_of_points[final_point] += 1

        if(all([list_of_points[x] == 1 for x in list_of_points])):
            should_continue = False
            break
        current_iter += 1
    return current_iter

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()