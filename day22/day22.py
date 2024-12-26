NUM_OF_MIXES = 2000

def main():
    input = readFile("d:\\adventofcode2024\\day22\\input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)

def challenge1(input):
    # Part 1 answer: 13004408787
    total = 0

    sequences = {}
    for num in input:
        run = 0
        last_digits = [num % 10]
        local_sequences = []
        while run < NUM_OF_MIXES:
            first_num = num << 6
            num = (num ^ first_num) % 16777216

            second_num = num >> 5
            num = (num ^ second_num) % 16777216

            third_num = num << 11
            num = (num ^ third_num) % 16777216

            run += 1

            last_digit = num % 10
            last_digits.append(last_digit)
            if len(last_digits) > 4:
                sequence = ("{:+}".format(last_digits[-4] - last_digits[-5]) + "{:+}".format(last_digits[-3] - last_digits[-4]) 
                            + "{:+}".format(last_digits[-2] - last_digits[-3]) + "{:+}".format(last_digits[-1] - last_digits[-2]))
                
                if sequence not in local_sequences:
                    local_sequences.append(sequence)
                else:
                    continue
                
                if sequence not in sequences:
                    sequences[sequence] = last_digit
                else:
                    sequences[sequence] += last_digit

    max_bananas = 0
    for sequence in sequences:
        if sequences[sequence] > max_bananas:
            max_bananas = sequences[sequence]
            
    return max_bananas

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return [int(num) for num in input_lines]

if __name__ == "__main__":
    main()