def main():
    input = readFile("d:\\adventofcode2024\\day9\\input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 6283170117911
    blocks = [input[i: i + 2] for i in range(0, len(input), 2)]
    
    block_str = []
    num_of_space = 0
    for i in range(0, len(blocks)):
        block_str += [str(i)] * int(blocks[i][0])
        if(i < len(blocks) - 1):
            block_str += ["."] * int(blocks[i][1])
            num_of_space += int(blocks[i][1])

    new_str = []
    j = len(block_str) - 1

    for i in range(0, len(block_str) - num_of_space):
        if(block_str[i] != "."):
            new_str.append(block_str[i])
            continue

        new_str.append(block_str[j])

        while(j >= 0):
            j -= 1
            if(block_str[j] != "."):
                break
    return sum(index * int(value) for index, value in enumerate(new_str))

def challenge2(input):
    # Answer: 6307653242596 

    blocks_str = []
    for i in range(0, len(input)):
        if(i % 2 == 0):
            blocks_str += [str(i // 2)] * int(input[i])
        else:
            blocks_str += ["."] * int(input[i])

    num_list = [int(input[i:i+1]) for i in range(0, len(input), 2)]

    for index, value in reversed(list(enumerate(num_list))):
        start_index = sum(int(input[i]) for i in range(0, index * 2))

        for i in range(0, start_index):
            if(blocks_str[i] != "."):
                continue

            current_gap = get_gap(i, blocks_str)

            if(current_gap < value):
                continue

            blocks_str[i:i+value], blocks_str[start_index: start_index + value] = blocks_str[start_index: start_index + value], blocks_str[i:i+value]

    return sum(index * int(value) for index, value in enumerate(blocks_str) if value != ".")

def get_gap(start_index, list):
    num_of_gap = 0
    for i in range(start_index, len(list)):
        if(list[i] == "."):
            num_of_gap += 1
        else: 
            break
    return num_of_gap

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines[0]

if __name__ == "__main__":
    main()