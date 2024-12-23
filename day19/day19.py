def main():
    patterns, towel = readFile("input.txt")
    # challenge1_result = challenge1(patterns, towel)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(patterns, towel)
    print("Challenge 2: ", challenge2_result)

def challenge1(patterns, towels):
    # Answer: 238
    num_of_towels = 0

    for towel in towels:
        if can_construct(patterns, towel):
            num_of_towels += 1

    return num_of_towels

def challenge2(patterns, towels):
    # Answer: 635018909726691
    num_of_towels = 0

    for towel in towels:
        num_of_towels += num_of_constructs(patterns, towel)

    return num_of_towels

def can_construct(patterns, towel):
    dp = [False] * (len(towel) + 1)
    dp[0] = True # empty string is always True

    for i in range(1, len(towel) + 1):
        for pattern in patterns:
            if i >= len(pattern) and dp[i - len(pattern)] and towel[i - len(pattern):i] == pattern:
                dp[i] = True
                break

    return dp[len(towel)]

def num_of_constructs(patterns, towel):
    dp = [0] * (len(towel) + 1)
    dp[0] = 1 # empty string is always True

    for i in range(1, len(towel) + 1):
        for pattern in patterns:
            if i >= len(pattern) and dp[i - len(pattern)] > 0 and towel[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(towel)]

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    patterns = input_lines[0].split(", ")
    return patterns, input_lines[2:]

if __name__ == "__main__":
    main()