def main():
    file = open("input.txt", "r")
    input_lines = file.read().splitlines()
    file.close()

    turn_list = []
    start = []

    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            if(input_lines[i][j] == "#"):
                turn_list.append([i, j])
            
            if(input_lines[i][j] == "^"):
                start = [i, j]

    challenge1_result, used_turns = challenge1(turn_list, start, len(input_lines), len(input_lines[i]))
    print("Challenge 1: ", challenge1_result)

    used_turns.insert(0 ,start)
    challenge2_result = challenge2(used_turns, turn_list)
    print("Challenge 2: ", challenge2_result)

def add_to_list(original_list, new_list):
    for item in new_list:
        if(item not in original_list):
            original_list.append(item)
    return original_list

def challenge1(turn_list, start, num_of_rows, num_of_cols):
    current_pos = start
    end = False

    direction = ["up", "right", "down", "left"]
    current_dir = 0

    move_list = [start]
    turns = []

    while(end == False):
        next_turn = -1
        new_move_list = []

        # 4 steps:
        # 1. Find the obstacle
        # 2. From the obstacle, find the turning point
        # 3. From the turning point, get list of moves
        # 4. Add list of moves to the moves list

        if(direction[current_dir % 4] == "up"):
            next_turn = [i[0] for i in turn_list if (i[1] == current_pos[1] and i[0] < current_pos[0])]
            next_turn.sort(reverse=True)

            if(len(next_turn) > 0):
                next_pos = [next_turn[0] + 1, current_pos[1]]
                if(next_pos not in turns):
                    turns.append(next_pos)

                new_move_list = list(map(lambda x: [x, current_pos[1]], range(next_pos[0], current_pos[0] + 1)))
                current_pos = next_pos
            else:
                new_move_list = list(map(lambda x: [x, current_pos[1]], range(0, current_pos[0] + 1)))
        
        if(direction[current_dir % 4] == "right"):
            next_turn = [i[1] for i in turn_list if (i[0] == current_pos[0] and i[1] > current_pos[1])]
            next_turn.sort()

            if(len(next_turn) > 0):
                next_pos = [current_pos[0], next_turn[0] - 1]
                if(next_pos not in turns):
                    turns.append(next_pos)

                new_move_list = list(map(lambda x: [current_pos[0], x], range(current_pos[1], next_pos[1] + 1)))
                current_pos = next_pos
            else:
                new_move_list = list(map(lambda x: [current_pos[0], x], range(current_pos[1], num_of_cols)))

        if(direction[current_dir % 4] == "down"):
            next_turn = [i[0] for i in turn_list if (i[1] == current_pos[1] and i[0] > current_pos[0])]
            next_turn.sort()
            
            if(len(next_turn) > 0):
                next_pos = [next_turn[0] - 1, current_pos[1]]
                if(next_pos not in turns):
                    turns.append(next_pos)
                    
                new_move_list = list(map(lambda x: [x, current_pos[1]], range(current_pos[0], next_pos[0] + 1)))
                current_pos = next_pos
            else:
                new_move_list = list(map(lambda x: [x, current_pos[1]], range(current_pos[0], num_of_rows)))

        if(direction[current_dir % 4] == "left"):
            next_turn = [i[1] for i in turn_list if (i[0] == current_pos[0] and i[1] < current_pos[1])]
            next_turn.sort(reverse=True)
            
            if(len(next_turn) > 0):
                next_pos = [current_pos[0], next_turn[0] + 1]
                if(next_pos not in turns):
                    turns.append(next_pos)
                    
                new_move_list = list(map(lambda x: [current_pos[0], x], range(next_pos[1], current_pos[1] + 1)))
                current_pos = next_pos
            else:
                new_move_list = list(map(lambda x: [current_pos[0], x], range(0, current_pos[1] + 1)))

        move_list = add_to_list(move_list, new_move_list)

        if(len(next_turn) == 0):
            end = True
        else:
            current_dir += 1

    return len(move_list), turns
        
def custom_sort(x):
    return x

def challenge2(turns, turn_list):
    # Answer: 1831
    # Example points: [6,3], [7,6], [7,7], [8,1], [8,3], [9,7]
    # total = 0

    # direction_list = ["right", "down", "left", "up"]
    direction_list = ["up", "right", "down", "left"]
    loop_points = []

    for i in range(0, len(turns)):
        # print("index", i)
        current_dir = direction_list[i % 4]
        if(current_dir == "left"):
            points_to_check = range(turns[i+1][1] + 1, turns[i][1]) if i + 1 <= len(turns) - 1 else range(1, turns[i][1])
        
            for point in points_to_check:
                # We bruteforce
                point_list = [x for x in turn_list if x[1] == point and x[0] < turns[i][0]]
                point_list = sorted(point_list, key=lambda x: x[0], reverse=True)

                if(len(point_list) > 0):
                    current_turns = turns[:i+1]
                    current_turns.append([turns[i][0], point])

                    loop_point = [turns[i][0], point - 1]
                    if(is_loop(current_turns, turn_list)):
                        # print("loop", [turns[i][0], point - 1], current_turns)
                        loop_points.append(loop_point)
                        # total += 1


        if(current_dir == "up"):
            points_to_check = range(turns[i+1][0] + 1, turns[i][0]) if i + 1 <= len(turns) - 1 else range(1, turns[i][0])

            for point in points_to_check:
                point_list = [x for x in turn_list if x[0] == point and x[1] > turns[i][1]]
                point_list = sorted(point_list, key=lambda x: x[1])

                if(len(point_list) > 0):
                    current_turns = turns[:i+1]
                    current_turns.append([point, turns[i][1]])

                    loop_point = [point - 1, turns[i][1]]
                    if(is_loop(current_turns, turn_list)):
                        # print("loop", [point - 1, turns[i][1]], current_turns)
                        loop_points.append([point - 1, turns[i][1]])
                        # total += 1

        if(current_dir == "right"):
            points_to_check = range(turns[i][1] + 1, turns[i+1][1]) if i + 1 <= len(turns) - 1 else range(turns[i][1] + 1, len(turns) - 1)

            for point in points_to_check:
                point_list = [x for x in turn_list if x[1] == point and x[0] > turns[i][0]]
                point_list = sorted(point_list, key=lambda x: x[0], reverse=True)

                if(len(point_list) > 0):
                    current_turns = turns[:i+1]
                    current_turns.append([turns[i][0], point])

                    loop_point = [turns[i][0], point + 1]
                    if(is_loop(current_turns, turn_list)):
                        loop_points.append([turns[i][0], point + 1])
                        # print("loop", [turns[i][0], point + 1], current_turns)
                        # total += 1

        if(current_dir == "down"):
            points_to_check = range(turns[i][0] + 1, turns[i+1][0]) if i + 1 <= len(turns) - 1 else range(turns[i][0] + 1, len(turns) - 1)

            for point in points_to_check:
                point_list = [x for x in turn_list if x[0] == point and x[1] < turns[i][1]]
                point_list = sorted(point_list, key=lambda x: x[1])

                if(len(point_list) > 0):
                    current_turns = turns[:i+1]
                    current_turns.append([point, turns[i][1]])

                    loop_point = [point + 1, turns[i][1]]
                    if(is_loop(current_turns, turn_list)):
                        # print("loop", [point + 1, turns[i][1]], current_turns)
                        loop_points.append(loop_point)
                        # total += 1
    
    unique_lists = [list(x) for x in set(tuple(x) for x in loop_points)]
    return len(unique_lists)

def is_loop(base_turns, all_turns):
    turn_list = base_turns
    # direction_list = ["right", "down", "left", "up"]
    direction_list = ["up", "right", "down", "left"]
    loop = False
    end = False

    while(end == False):
        current_index = len(turn_list) - 1

        start_pos = turn_list[current_index]

        next_pos = []
        if(direction_list[current_index % 4]) == "right":
            next_obstacle = [x for x in all_turns if x[0] == start_pos[0] and x[1] > start_pos[1]]
            next_obstacle = sorted(next_obstacle, key=lambda x: x[1])
            if(len(next_obstacle) > 0):
                next_pos = next_obstacle[0]
                next_pos = [next_pos[0], next_pos[1] - 1]

        if(direction_list[current_index % 4]) == "down":
            next_obstacle = [x for x in all_turns if x[1] == start_pos[1] and x[0] > start_pos[0]]
            next_obstacle = sorted(next_obstacle, key=lambda x: x[0])
            if(len(next_obstacle) > 0):
                next_pos = next_obstacle[0]
                next_pos = [next_pos[0] - 1, next_pos[1]]

        if(direction_list[current_index % 4]) == "left":
            next_obstacle = [x for x in all_turns if x[0] == start_pos[0] and x[1] < start_pos[1]]
            next_obstacle = sorted(next_obstacle, key=lambda x: x[1], reverse=True)
            if(len(next_obstacle) > 0):
                next_pos = next_obstacle[0]
                next_pos = [next_pos[0], next_pos[1] + 1]

        if(direction_list[current_index % 4]) == "up":
            next_obstacle = [x for x in all_turns if x[1] == start_pos[1] and x[0] < start_pos[0]]
            next_obstacle = sorted(next_obstacle, key=lambda x: x[0], reverse=True)
            if(len(next_obstacle) > 0):
                next_pos = next_obstacle[0]
                next_pos = [next_pos[0] + 1, next_pos[1]]

        if(next_pos != []):
            if((current_index + 1) % 4 in all_directions(turn_list, next_pos)):
                loop = True
                end = True

            turn_list.append(next_pos)
        else:
            end = True
    
    return loop

def all_directions(list, value):
    indexes = [i % 4 for i, x in enumerate(list) if x == value]
    return indexes

if __name__ == "__main__":
    main()