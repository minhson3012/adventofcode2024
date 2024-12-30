def main():
    locks, keys = readFile("input.txt")
    challenge1_result = challenge1(locks, keys)
    print("Challenge 1: ", challenge1_result)

def challenge1(locks, keys):
    # Answer: 3356
    count = 0
    for lock in locks:
        for key in keys:
            if all(key[x] + lock[x] < 6 for x in range(5)):
                count += 1

    return count

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    keys = []
    locks = []

    current_item = [-1] * 5
    current_index = 0
    is_lock = False
    for line in input_lines:
        if not line:
            current_index = 0
            continue

        if current_index == 0 and line == "#" * 5:
            is_lock = True
        elif current_index == 0 and line == "." * 5:
            is_lock = False
        
        for index, symbol in enumerate(line):
            if symbol == "#":
                current_item[index] += 1

        if current_index == 6:
            if is_lock:
                locks.append(current_item)
            else:
                keys.append(current_item)

            current_item = [-1] * 5
        else:
            current_index += 1
    return locks, keys

if __name__ == "__main__":
    main()