def challenge1(input):
    # Answer: 7,5,4,3,4,5,3,4,6
    reg_A = int(input[0])
    reg_B = int(input[1])
    reg_C = int(input[2])

    program = [int(x) for x in input[4].split(",")]

    pointer = 0
    output = []
    program_running = True
    while program_running:
        if(pointer >= len(program)):
            program_running = False
            continue
            
        opcode = program[pointer]
        operand = program[pointer + 1]
        combo_operand = get_combo_value(operand, reg_A, reg_B, reg_C)

        if opcode == 0:
            reg_A = reg_A // pow(2, combo_operand)
        elif opcode == 1:
            reg_B = reg_B ^ operand
        elif opcode == 2:
            reg_B = combo_operand % 8
        elif opcode == 3 and reg_A != 0:
            pointer = operand
            continue
        elif opcode == 4:
            reg_B = reg_B ^ reg_C
        elif opcode == 5:
            output.append(str(combo_operand % 8))
        elif opcode == 6:
            reg_B = reg_A // pow(2, combo_operand)
        elif opcode == 7:
            reg_C = reg_A // pow(2, combo_operand)
        pointer += 2

    return ",".join(output)

def challenge2(input):
    # Answer: 164278899142333
    return do_the_thing(input, 0, 1)

# Check from end of the output to start, shift reg_A by 3 bits after every loop to try and find the right value
def do_the_thing(input, reg_A, current_index, valid = set()):
    reg_B = input[1]
    reg_C = input[2]
    program = input[4]
    commands = [x for x in input[4].split(",")]

    for i in range(8):
        new_A = (reg_A << 3) | i
        output = challenge1([new_A, reg_B, reg_C, "", program])
        output_split = output.split(",")
        
        if(output_split == commands[-current_index:]):
            if(output == program):
                valid.add(new_A)
            else:
                do_the_thing(["", reg_B, reg_C, "", program], new_A, current_index + 1, valid)

    if len(valid) > 0:
        return min(valid)
    
    return 0

def get_combo_value(operand, A, B, C):
    if(operand == 4):
        return A
    if(operand == 5):
        return B
    if(operand == 6):
        return C
    return operand

# opcode 4
def bxc(B_value, C_value):
    return B_value ^ C_value

def main():
    input = readFile("d:\\adventofcode2024\\day17\\input.txt")
    challenge1_result = challenge1(input)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    
    return input_lines

if __name__ == "__main__":
    main()