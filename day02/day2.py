def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def check_valid(num_list):
    diffs = []
    for i in range(0, len(num_list) - 1):
        diffs.append(int(num_list[i]) - int(num_list[i + 1]))
        
    num_negative = list(filter(lambda x: x < 0, diffs))
    num_positive = list(filter(lambda x: x > 0, diffs))
    num_invalid = list(filter(lambda x: (abs(x) < 1 or abs(x) > 3), diffs))

    if(len(num_positive) + len(num_invalid) == 0 or len(num_negative) + len(num_invalid) == 0):
        return True
    
    return False

def challenge1(input):
    total = 0
    for line in input:
        num_list = line.split()

        if(check_valid(num_list)):
            total += 1

    return total

def challenge2(input):
    total = 0
    for line in input:
        num_list = line.split()

        if(check_valid(num_list)):
            total += 1
        else:
            for i in range(0, len(num_list)):
                new_list = num_list.copy()
                new_list.pop(i)
                if(check_valid(new_list)):
                    total += 1
                    break
    return total

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()
