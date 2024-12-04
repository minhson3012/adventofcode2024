def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    total = 0

    for i in range(0, len(input)):
        current_line = input[i]

        for j in range(0, len(current_line)):
            if(current_line[j] != "X"):
                continue

            words = []
            can_check_up = i - 3 >= 0
            can_check_down = i + 3 <= len(input) - 1
            can_check_left = j - 3 >= 0
            can_check_right = j + 3 <= len(current_line) - 1


            if(can_check_up):
                words.append([input[i-1][j], input[i-2][j], input[i-3][j]])

                if(can_check_left):
                    words.append([input[i-1][j-1], input[i-2][j-2], input[i-3][j-3]])
                
                if(can_check_right):
                    words.append([input[i-1][j+1], input[i-2][j+2], input[i-3][j+3]])

            if(can_check_down):
                words.append([input[i+1][j], input[i+2][j], input[i+3][j]])

                if(can_check_left):
                    words.append([input[i+1][j-1], input[i+2][j-2], input[i+3][j-3]])
                
                if(can_check_right):
                    words.append([input[i+1][j+1], input[i+2][j+2], input[i+3][j+3]])

            if(can_check_left):
                words.append([input[i][j-1],input[i][j-2],input[i][j-3]])

            if(can_check_right):
                words.append([input[i][j+1],input[i][j+2],input[i][j+3]])

            total += sum(word == ["M", "A", "S"] for word in words)
    return total

def challenge2(input):
    total = 0

    for i in range(0, len(input)):
        current_line = input[i]

        for j in range(0, len(current_line)):
            can_check = i >= 1 and i <= len(input) - 2 and j >= 1 and j <= len(current_line) - 2

            if(current_line[j] != "A" or can_check == False):
                continue

            word_1 = [input[i - 1][j - 1], input[i + 1][j + 1]]
            word_2 = [input[i - 1][j + 1], input[i + 1][j - 1]]

            word_1.sort()
            word_2.sort()

            if(word_1 == word_2 == ["M", "S"]):
                total += 1

    return total

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()