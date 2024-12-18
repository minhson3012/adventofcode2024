def main():
    input, limit = readFile("input.txt")
    challenge1_result = challenge1(input, limit)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input, limit)
    print("Challenge 2: ", challenge2_result)

def challenge1(input, limit):
    # Answer: 361
    point_list = set()
    for freq in input:
        antennas = input[freq]

        for i in range(0, len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                dy = antennas[j][0] - antennas[i][0]
                dx = antennas[j][1] - antennas[i][1]

                if(0 <= antennas[i][0] - dy <= limit and 0 <= antennas[i][1] - dx <= limit):
                    point_list.add((antennas[i][0] - dy, antennas[i][1] - dx))

                if(0 <= antennas[j][0] + dy <= limit and 0 <= antennas[j][1] + dx <= limit):
                    point_list.add((antennas[j][0] + dy, antennas[j][1] + dx))

    return len(point_list)

def challenge2(input, limit):
    # Answer: 1249
    point_list = set()
    for freq in input:
        antennas = input[freq]

        for i in range(0, len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                dy = antennas[j][0] - antennas[i][0]
                dx = antennas[j][1] - antennas[i][1]
                point_list.add(antennas[i])
                point_list.add(antennas[j])

                stop_1 = False
                multiplier_1 = 1
                while(stop_1 == False):
                    if(0 <= (antennas[i][0] - multiplier_1 * dy) <= limit and 0 <= (antennas[i][1] - multiplier_1 * dx) <= limit):
                        point_list.add((antennas[i][0] - multiplier_1 * dy, antennas[i][1] - multiplier_1 * dx))
                    else:
                        stop_1 = True
                    multiplier_1 += 1

                stop_2 = False
                multiplier_2 = 1
                while(stop_2 == False):
                    if(0 <= (antennas[j][0] + multiplier_2 * dy) <= limit and 0 <= (antennas[j][1] + multiplier_2 * dx) <= limit):
                        point_list.add((antennas[j][0] + multiplier_2 * dy, antennas[j][1] + multiplier_2 * dx))
                    else:
                        stop_2 = True
                    multiplier_2 += 1

    return len(point_list)

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    input = {}
    for i in range(0, len(input_lines)):
        for j in range(0, len(input_lines[i])):
            if(input_lines[i][j] != "."):
                elem = input_lines[i][j]

                if(elem not in input):
                    input[elem] = [(i, j)]
                else:
                    input[elem].append((i, j))

    return input, len(input_lines) - 1

if __name__ == "__main__":
    main()