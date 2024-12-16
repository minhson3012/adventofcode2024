def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 194557
    current_stones = input.copy()
    times_blinked = 1

    while(times_blinked <= 25):
        new_stones = []
        for stone in current_stones:
            if(stone == 0):
                new_stones.append(1)
            elif(len(str(stone)) % 2 == 0):
                stone_str = str(stone)
                half_length = len(str(stone)) // 2
                new_stones.append(int(stone_str[:half_length]))
                new_stones.append(int(stone_str[half_length:]))
            else:
                new_stones.append(stone * 2024)
        current_stones = new_stones
        times_blinked += 1
    return len(current_stones)

def challenge2(input):
    # Answer: 231532558973909
    stones = {}
    for i in range(0, len(input)):
        if(input[i] in stones):
            stones[input[i]] += 1
        else:
            stones[input[i]] = 1

    times_blinked = 1

    while(times_blinked <= 75):
        new_stones = {}
        
        for stone in list(stones.keys()):
            if(stone == 0):
                if((stone + 1) in new_stones):
                    new_stones[stone + 1] += stones[stone]
                else:
                    new_stones[stone + 1] = stones[stone]
            elif(len(str(stone)) % 2 == 0):
                stone_str = str(stone)
                half_length = len(str(stone)) // 2

                first_num = int(stone_str[:half_length])
                if(first_num in new_stones):
                    new_stones[first_num] += stones[stone]
                else:
                    new_stones[first_num] = stones[stone]

                second_num = int(stone_str[half_length:])
                if(second_num in new_stones):
                    new_stones[second_num] += stones[stone]
                else:
                    new_stones[second_num] = stones[stone]
            else:
                new_num = stone * 2024
                if(new_num in new_stones):
                    new_stones[new_num] += stones[stone]
                else:
                    new_stones[new_num] = stones[stone]

        stones = new_stones
        times_blinked += 1

    total = 0

    for stone in stones:
        total += stones[stone]
    return total


def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return [int(x) for x in input_lines[0].split()]

if __name__ == "__main__":
    main()