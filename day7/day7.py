def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)

def challenge1(input):
    # Answer: 20281182715321
    total = 0
    for line in input:
        total += calculate(line)
    return total

def calculate(line):
    elems = line[1]
    elems.reverse()

    current_values = [int(line[0])]
    for index, val in enumerate(elems):
        value = int(val)
        if(index == len(elems) - 1):
            break

        new_values = []

        for index, total_value in enumerate(current_values):
            if(value != 0 and total_value % value != 0):
                current_values[index] = total_value - value

            if((value != 0 and total_value % value == 0) or value == 1):
                current_values[index] = total_value // value
                new_values.append(total_value - value)

        current_values += new_values

    # print(line[0], current_values)
    for value in current_values:
        if(value == int(elems[-1])):
            return int(line[0])
    
    return 0

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    input = []
    for line in input_lines:
        line_split = line.split(":")
        input.append([line_split[0], line_split[1].strip().split(" ")])

    return input

if __name__ == "__main__":
    main()