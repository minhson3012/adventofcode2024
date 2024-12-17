import math

def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    # challenge2_result = challenge2(input)
    # print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Challenge 1: 39290
    # Challenge 2: 73458657399094
    x1, x2, y1, y2, s1, s2 = 0, 0, 0, 0, 0, 0

    tokens = 0
    for i in range(0, len(input) + 1):
        if(i % 4 == 0):
            x1, y1 = [int(x) for x in input[i].split()]
        if(i % 4 == 1):
            x2, y2 = [int(x) for x in input[i].split()]
        if(i % 4 == 2):
            s1, s2 = [int(x) + 10000000000000 for x in input[i].split()]
            # s1, s2 = [int(x) for x in input[i].split()]
        if(i % 4 == 3):

            lcm1 = math.lcm(x1, y1)
            multiplier1 = lcm1 // x1
            multiplier2 = lcm1 // y1
            b = (s1 * multiplier1 - s2 * multiplier2) / (x2 * multiplier1 - y2 * multiplier2)
            a = (s1 - x2*b) / x1

            if(a.is_integer() and b.is_integer() and a >= 0 and b >= 0):
                tokens += a * 3 + b

    return tokens

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()