def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)


def challenge1(input):
    total = 0
    first_list = []
    second_list = []
    for line in input:
        current_nums = line.split()
        first_list.append(current_nums[0])
        second_list.append(current_nums[1])

    first_list.sort()
    second_list.sort()

    for index, item in enumerate(first_list):
        total += abs(int(first_list[index]) - int(second_list[index]))
    return total

def challenge2(input):
    total = 0
    first_list = []
    second_list = []
    for line in input:
        current_nums = line.split()
        first_list.append(current_nums[0])
        second_list.append(current_nums[1])

    first_set = set(first_list)

    for item in first_set:
        total += int(item) * second_list.count(item)

    return total

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()