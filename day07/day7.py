def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 20281182715321
    total = 0
    for line in input:
        total += calculate(line, False)
    return total

def challenge2(input):
    # Answer: 159490400628354
    total = 0
    for line in input:
        total += calculate(line, True)
    return total

def calculate(line, do_the_thing):
    elems = line[1].copy()
    elems.reverse()

    current_values = [int(line[0])]
    for index, val in enumerate(elems):
        value = int(val)
        if(index == len(elems) - 1):
            break

        new_values = []

        for index, total_value in enumerate(current_values):
            if(value != 0 and total_value % value != 0 and total_value - value >= 0):
                current_values[index] = total_value - value

            if((value != 0 and total_value % value == 0) or value == 1):
                current_values[index] = total_value // value

                if(total_value - value >= 0):
                    new_values.append(total_value - value)

            if(do_the_thing):
                total_value_str = str(total_value)
                if(total_value_str[-len(val):] == val and total_value != value):
                    new_values.append(int(total_value_str[:-len(val)]))

        current_values += new_values

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