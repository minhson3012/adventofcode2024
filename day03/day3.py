import re

def main():
    input = readFile("input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    total = 0

    list = re.findall(r"(mul\(\d{1,},\d{1,}\))", input)

    for mul in list:
        num_list = re.sub(r"[^\d,]", "", mul).split(",")
        total += int(num_list[0]) * int(num_list[1])
    return total

def challenge2(input):
    total = 0

    list = []

    match_list = re.findall(r"(don't\(\))|(do\(\))|(mul\(\d{1,3},\d{1,3}\))", input)
    new_line = ''.join([match[0] or match[1] or match[2] for match in match_list])
    new_line = re.sub(r"(don't\(\)(.*?do\(\)))", "do()", new_line)
    new_line = re.sub(r"(don't\(\)(.*))", "do()", new_line)
    list += re.findall(r"(mul\(\d{1,3},\d{1,3}\))", new_line)

    for mul in list:
        num_list = re.sub(r"[^\d,]", "", mul).split(",")
        total += int(num_list[0]) * int(num_list[1])

    return total

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read() # no split lines this time
    file.close()
    return input_lines

if __name__ == "__main__":
    main()
