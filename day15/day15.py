def main():
    input, moves, max_length, max_height = readFile("input.txt")
    # challenge1_result = challenge1(input, moves, max_length)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input, moves, max_length, max_height)
    print("Challenge 2: ", challenge2_result)

def challenge1(points, moves, max_length):
    # Answer: 1421727

    current_point = points["current"]
    for move in moves:

        dx = 1 if move == ">" else -1 if move == "<" else 0
        dy = 1 if move == "v" else -1 if move == "^" else 0
        
        # Check if there's a wall
        walls = [x for x in points["walls"] if current_point[0] + dy == x[0] and current_point[1] + dx == x[1]]
        if(len(walls) == 1):
            continue

        # Check if there's any box
        next_box = [x for x in points["boxes"] if current_point[0] + dy == x[0] and current_point[1] + dx == x[1]]
        if(len(next_box) == 0):
            current_point = calc_next_point(current_point[1] + dx, current_point[0] + dy, max_length - 2)
            continue

        # boxes = [(index1, (x1, y1)), (index2, (x2, y2)), ...]
        boxes = [{"index": index, "value":x} for index, x in enumerate(points["boxes"]) if ((dy == 0 and x[0] == current_point[0]) or (dy != 0 and (x[0] - current_point[0]) / dy >= 0)) 
                    and ((dx == 0 and x[1] == current_point[1]) or (dx != 0 and (x[1] - current_point[1]) / dx >= 0))]
        
        boxes = sort_boxes(boxes, dx, dy)

        for box in boxes:
            index = box["index"]
            current_box = points["boxes"][index]
            box_next_point = calc_next_point(current_box[1] + dx, current_box[0] + dy, max_length - 2)
            if(box_next_point != current_box and box_next_point not in points["boxes"] and box_next_point not in points["walls"]):
                points["boxes"][index] = box_next_point

        # next_point = (current_point[0] + dy, current_point[1] + dx)
        # if(next_point not in points["boxes"] and next_point not in points["walls"]):
        current_point = calc_next_point(current_point[1] + dx, current_point[0] + dy, max_length - 2)
    
    gps = 0
    for box in points["boxes"]:
        gps += 100 * box[0] + box[1]
    return gps

def challenge2(points, moves, max_length, max_height):
    # Answer: 1463160

    current_point = points["current"]
    current_move = 0
    # print_current(points, current_point, max_length, max_height, moves[0], current_move)
    for move in moves:
        current_move += 1

        dx = 1 if move == ">" else -1 if move == "<" else 0
        dy = 1 if move == "v" else -1 if move == "^" else 0
        
        # Check if there's a wall
        walls = [x for x in points["walls"] if current_point[0] + dy == x[0] and current_point[1] + dx == x[1]]
        if(len(walls) == 1):
            # print_current(points, current_point, max_length, max_height, move, current_move)
            continue

        # Check if there's any box
        next_box = [x for x in points["boxes"] if current_point[0] + dy == x[0] 
                    and (((dx < 0 or dy != 0) and current_point[1] + 2*dx == x[1] )
                        or ((dx > 0 or dy != 0) and current_point[1] + 2*dx - 1 == x[1]))]
        if(len(next_box) == 0):
            current_point = calc_next_point(current_point[1] + dx, current_point[0] + dy, max_length - 2, max_height - 1)
            # print_current(points, current_point, max_length,max_height, move, current_move)
            continue
        else:
            # Check case box is already in border
            box = next_box[0]
            if((dy == -1 and box[0] == 1) or (dy == 1 and box[0] == max_height - 1)
               or (dx == -1 and box[1] == 2) or (dx == 1 and box[1] == max_length - 2)):
                # print_current(points, current_point, max_length, max_height, move, current_move)
                continue

        # boxes = [(index1, (x1, y1)), (index2, (x2, y2)), ...]
        boxes = get_list_of_boxes(dx, dy, current_point, points)
        
        boxes = sort_boxes(boxes, dx, dy, box_size=2)

        new_boxes = points["boxes"].copy()
        can_move = True
        for box in list(boxes):
            index = box["index"]
            current_box = box["value"]
            box_next_point = calc_next_point(current_box[1] + dx, current_box[0] + dy, max_length - 2, max_height - 1)
            if(can_move_box(points["walls"], new_boxes, box_next_point, index)):
                new_boxes[index] = box_next_point
            else:
                can_move = False
                break
        if(can_move):
            points["boxes"] = new_boxes
            current_point = calc_next_point(current_point[1] + dx, current_point[0] + dy, max_length - 2, max_height - 1)

        # print_current(points, current_point, max_length, max_height, move, current_move)
    
    gps = 0
    for box in points["boxes"]:
        gps += 100 * box[0] + box[1]
    return gps

def get_list_of_boxes(dx, dy, current_point, points):
    boxes = []
    points_copy = points["boxes"].copy()
    points_to_check = []

    for index, x in enumerate(points["boxes"]):
        if(((dy == 0 and x[0] == current_point[0]) 
            or (dy != 0 and (x[0] - current_point[0]) / dy >= 0)) 
                and ((dx == 0 and x[1] == current_point[1] and current_point[0] + dy == x[0]) 
                    or (dx != 0 and (x[1] - current_point[1]) / (2*dx) >= 0))):
            # Check boxes directly on the same y and x axis
            if({"index": index, "value":x} not in boxes):
                boxes.append({"index": index, "value":x})
            points_to_check.append(x)
        elif(dx == 0 and x[1] + 1 == current_point[1] and current_point[0] + dy == x[0]):
            # Check boxes slightly to the left on y axis
            if({"index": index, "value":x} not in boxes):
                boxes.append({"index": index, "value":x})
            points_to_check.append(x)

    points_to_check = list(set(points_to_check))
    while(points_to_check and dx == 0):
        point = points_to_check.pop()
        if(point):
            for index, x in enumerate(points_copy):
                if(point[0] + dy == x[0] and (abs(point[1] - x[1]) <= 1) and {"index": index, "value":x} not in boxes):
                    points_to_check.append(x)
                    boxes.append({"index": index, "value":x})
    return list(boxes)

def can_move_box(walls, boxes, next_point, current_index):
    # Check if wall is next
    if(next_point in walls or (next_point[0], next_point[1] + 1) in walls):
        return False

    # Check if box can be moved

    for index, box in enumerate(boxes):  
        boxes_to_check = [box, (box[0], box[1] + 1)]
        if((next_point in boxes_to_check or (next_point[0], next_point[1] + 1) == box) and current_index != index):
            return False
    return True

def print_current(points, current_point, max_length, max_height, move, current_move):
    print("-----------", "Move", current_move, move, "----------")
    for i in range(0, max_height):
        current_line = ""
        is_box = False
        for j in range(0, max_length):
            if(current_point == (i, j)):
                current_line += "@"
                is_box = False
            elif((i,j) in points["walls"]):
                current_line += "#"
                is_box = False
            elif((i,j) in points["boxes"]):
                current_line += "["
                is_box = True
            elif(not is_box):
                current_line += "."
                is_box = False
            elif(is_box):
                current_line += "]"
                is_box = False
        print(current_line)
    return

def calc_next_point(x, y, length_limit, height_limit):
    new_x = 2 if x < 2 else length_limit if x > length_limit else x
    new_y = 1 if y < 1 else height_limit if y > height_limit else y
    return (new_y, new_x)

def sort_boxes(boxes, dx, dy, box_size=1):
    if(len(boxes) == 0):
        return boxes
    if(dx != 0):
        # After sorting, make sure that boxes are right next to each other
        sorted_boxes = sorted(boxes, key=lambda x: x["value"][1], reverse=True if dx < 0 else False)
        for index, box in enumerate(sorted_boxes):
            value = box["value"]

            if(index < len(sorted_boxes) - 1):
                next_box = sorted_boxes[index + 1]

                if(next_box["value"][1] - value[1] != box_size * dx):
                    return reversed(sorted_boxes[:index+1])
                    # return sorted(boxes[:index + 1], key=lambda x: x["value"][1], reverse=False if dx < 0 else True)
        # return sorted(boxes, key=lambda x: x["value"][1], reverse=False if dx < 0 else True)
        return reversed(sorted_boxes)            
    if(dy != 0):
        sorted_boxes = sorted(boxes, key=lambda x: x["value"][0], reverse=True if dy < 0 else False)
        y_axis = set()
        for index, box in enumerate(sorted_boxes):
            value = box["value"]
            y_axis.add(value[0])
            if(index < len(sorted_boxes) - 1):
                next_box = sorted_boxes[index + 1]

                if(next_box["value"][0] not in y_axis and next_box["value"][0] - value[0] != dy):
                    return reversed(sorted_boxes[:index+1])
                    # return sorted(boxes[:index + 1], key=lambda x: x["value"][0], reverse=False if dy < 0 else True)
        # return sorted(boxes, key=lambda x: x["value"][0], reverse=False if dy < 0 else True)
        return reversed(sorted_boxes)
    return boxes

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()

    input = {"walls": set(), "boxes": [], "current": None}
    moves = ""
    set_move = False
    max_height = 0
    for i in range(0, len(input_lines)):
        if(len(input_lines[i].strip()) == 0):
            max_height = i
            set_move = True
            continue
        for j in range(0, len(input_lines[i])):
            if(set_move):
                moves += input_lines[i][j].strip()
                continue

            if(input_lines[i][j] == "#"):
                input["walls"].add((i,j))
            if(input_lines[i][j] == "["):
                input["boxes"].append((i,j))
            if(input_lines[i][j] == "@"):
                input["current"] = (i, j)
    return input, moves, len(input_lines[0]), max_height

if __name__ == "__main__":
    main()