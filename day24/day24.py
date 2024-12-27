def main():
    base_values, z_values, gates = readFile("input.txt")
    challenge1_result = challenge1(base_values, z_values, gates)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(z_values, gates)
    print("Challenge 2: ", challenge2_result)

def calculate(base_values, gates, current_item):
    gate1, gate2, logic_gate = gates[current_item]
    
    value1, value2 = None, None
    if gate1 in base_values:
        value1 = base_values[gate1]
    else:
        value1 = calculate(base_values, gates, gate1)

    if gate2 in base_values:
        value2 = base_values[gate2]
    else:
        value2 = calculate(base_values, gates, gate2)

    value = value1 & value2 if logic_gate == "AND" else value1 | value2 if logic_gate == "OR" else value1 ^ value2
    base_values[current_item] = value
    return value

def challenge1(base_values, z_values, gates):
    # Answer: 55920211035878
    new_base_values = base_values.copy()
    for z in z_values:
        z_values[z] = calculate(new_base_values, gates, z)

    # Part 1
    sorted_values = dict(sorted(z_values.items(), reverse=True))
    value_str = "".join(map(str, sorted_values.values()))
    return int(value_str, 2)

def challenge2(z_values, gates):
    # Answer: btb,cmv,mwp,rdg,rmj,z17,z23,z30
    highest_z = "z" + str(len(z_values) - 1).zfill(2)
    wrong = set()
    for gate in gates:
        gate1, gate2, logic = gates[gate]

        if gate[0] == "z" and logic != "XOR" and gate != highest_z:
            wrong.add(gate)
        elif (logic == "XOR" 
            and gate[0] not in ["x", "y", "z"]
            and gate1[0] not in ["x", "y", "z"]
            and gate2[0] not in ["x", "y", "z"]):
            wrong.add(gate)
        elif logic == "AND" and "x00" not in [gate1, gate2]:
            for subgate in gates:
                subgate1, subgate2, sublogic = gates[subgate]
                if (gate == subgate1 or gate == subgate2) and sublogic != "OR":
                    wrong.add(gate)
        elif logic == "XOR":
            for subgate in gates:
                subgate1, subgate2, sublogic = gates[subgate]
                if (gate == subgate1 or gate == subgate2) and sublogic == "OR":
                    wrong.add(gate)
    return ",".join(sorted(wrong))

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    setup_values = True
    base_values = {}
    gates = {}
    z_values = {}
    for line in input_lines:
        if not line:
            setup_values = False
            continue

        str_split = line.split(" ")

        if setup_values:
            base_values[str_split[0]] = int(str_split[1])
        else:
            gates[str_split[3]] = (str_split[0], str_split[2], str_split[1])

            if str_split[3][0] == "z":
                z_values[str_split[3]] = None

    return base_values, z_values, gates

if __name__ == "__main__":
    main()