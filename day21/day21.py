import re

NUM_PAD = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
ARROW_PAD = [["", "^", "A"], ["<", "v", ">"]]

ARROW_MOVE = {"A": {"^": "<A", ">": "vA", "v": "v<A", "<": "v<<A"},
              "^": {"A": ">A", ">": "v>A", "<": "v<A", "v": "vA"},
              ">": {"A": "^A", "^": "^<A", "v": "<A", "<": "<<A"},
              "v": {"A": ">^A", "^": "^A", ">": ">A", "<": "<A"},
              "<": {"A": ">>^A", "v": ">A", "^": ">^A", ">": ">>A"}}

NUM_START = (3, 2)
ARROW_START = (0, 2)

def main():
    input = readFile("input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 203814
    commands = []
    cur_1 = NUM_START
    for code in input:
        possible_moves = set()
        for i in code:
            moves = []
            point = [(x, y) for x in range(4) for y in range(3) if NUM_PAD[x][y] == i][0]

            dx, dy = point[0] - cur_1[0], point[1] - cur_1[1]
            horizontal = ""
            vertical = ""

            if dy < 0:
                horizontal += "<" * -dy
            elif dy > 0:
                horizontal += ">" * dy

            if dx < 0:
                vertical += "^" * -dx
            elif dx > 0:
                vertical += "v" * dx

            moves.append(vertical + horizontal + "A")
            moves.append(horizontal + vertical + "A")

            if cur_1[0] == 3 and cur_1[1] + dy <= 0:
                moves = moves[:1]
            if cur_1[1] == 0 and cur_1[0] + dx >= 3:
                moves = moves[1:]

            if len(possible_moves) == 0:
                possible_moves = moves
            else:
                new_possible_moves = set()
                for move in possible_moves:
                    for x in moves:
                        new_possible_moves.add(move + x)

                possible_moves = new_possible_moves
            
            cur_1 = point

        smallest_length = 0

        for possible_move in possible_moves:
            moves = possible_move
            curr_layer = 1
            while curr_layer <= 2:
                new_move = ""
                curr_point = ARROW_START

                for move in moves:
                    if move == curr_point:
                        new_move += "A"
                    else:
                        new_move += ARROW_MOVE[curr_point][move]

                    curr_point = move

                curr_layer += 1
                moves = new_move

            if smallest_length == 0 or len(moves) < smallest_length:
                smallest_length = len(moves)

        commands.append(smallest_length)

    total = 0
    for index, command in enumerate(commands):
        numeric = int(input[index][:3])
        print(command, numeric)
        total += command * numeric
    return total

def challenge2(input):
    # Answer: 248566068436630
    total = 0
    cur_1 = NUM_START
    for code in input:
        possible_moves = set()
        for i in code:
            moves = []
            point = [(x, y) for x in range(4) for y in range(3) if NUM_PAD[x][y] == i][0]

            dx, dy = point[0] - cur_1[0], point[1] - cur_1[1]
            horizontal = ""
            vertical = ""

            if dy < 0:
                horizontal += "<" * -dy
            elif dy > 0:
                horizontal += ">" * dy

            if dx < 0:
                vertical += "^" * -dx
            elif dx > 0:
                vertical += "v" * dx

            moves.append(vertical + horizontal + "A")
            moves.append(horizontal + vertical + "A")

            if cur_1[0] == 3 and cur_1[1] + dy <= 0:
                moves = moves[:1]
            if cur_1[1] == 0 and cur_1[0] + dx >= 3:
                moves = moves[1:]

            if len(possible_moves) == 0:
                possible_moves = moves
            else:
                new_possible_moves = set()
                for move in possible_moves:
                    for x in moves:
                        new_possible_moves.add(move + x)

                possible_moves = new_possible_moves
            
            cur_1 = point

        min_length = 0
        for seq in possible_moves:
            new_min = get_shortest_seq(seq, 25, {})

            if min_length == 0 or new_min < min_length:
                min_length = new_min

        total += min_length * int(code[:3])
    return total

def get_shortest_seq(keys, depth, cache):
    if depth == 0:
        return len(keys)
    
    if (keys, depth) in cache:
        return cache[(keys, depth)]
    
    subKeys = re.split('(?<=A)', keys)

    subKeys = [subKey for subKey in subKeys if subKey]

    total = 0

    cur_1 = ARROW_START
    for code in subKeys:
        possible_moves = set()
        for i in code:
            moves = []
            point = [(x, y) for x in range(2) for y in range(3) if ARROW_PAD[x][y] == i][0]
            dx, dy = point[0] - cur_1[0], point[1] - cur_1[1]
            horizontal = ""
            vertical = ""

            if dy < 0:
                horizontal += "<" * -dy
            elif dy > 0:
                horizontal += ">" * dy

            if dx < 0:
                vertical += "^" * -dx
            elif dx > 0:
                vertical += "v" * dx

            moves.append(vertical + horizontal + "A")
            moves.append(horizontal + vertical + "A")
            if cur_1[0] == 0 and cur_1[1] + dy <= 0:
                moves = moves[:1]
            if cur_1[1] == 0 and cur_1[0] + dx >= 0:
                moves = moves[1:]
            if len(possible_moves) == 0:
                possible_moves = moves
            else:
                new_possible_moves = set()
                for move in possible_moves:
                    for x in moves:
                        new_possible_moves.add(move + x)
                possible_moves = new_possible_moves

            cur_1 = point

        min_length = 0
        for seq in possible_moves:
            new_min = get_shortest_seq(seq, depth - 1, cache)
            if min_length == 0 or new_min < min_length:
                min_length = new_min
        total += min_length


    cache[(keys, depth)] = total
    return total

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()
    return input_lines

if __name__ == "__main__":
    main()