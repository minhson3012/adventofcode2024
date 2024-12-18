def main():
    file = open("input.txt", "r")
    input_lines = file.read().splitlines()
    file.close()

    page_list = []
    order_list = []

    end_of_page = False
    for line in input_lines:
        if(len(line) == 0):
            end_of_page = True
            continue

        if(end_of_page == False):
            page_list.append(line.split("|"))
        else:
            order_list.append(line.split(","))

    dict = get_dict(page_list)
    challenge1_result = challenge1(dict, order_list)
    print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(dict, order_list)
    print("Challenge 2: ", challenge2_result)

def get_dict(page_list):
    dict = {}

    for page in page_list:
        if(page[0] not in dict):
            dict[page[0]] = [page[1]]
        else:
            dict[page[0]].append(page[1])
    return dict

def challenge1(dict, orders):
    total = 0
    
    for order in orders:
        if(all(order[i] in dict and order[i+1] in dict[order[i]] for i in range(len(order) - 1))):
            total += int(order[len(order) // 2])
        
    return total

def challenge2(dict, orders):
    total = 0

    for order in orders:
        if(all(order[i] in dict and order[i+1] in dict[order[i]] for i in range(len(order) - 1))):
            continue

        list = [-1] * len(order)
        for i in range(len(list)):
            remaining_items = [item for item in order.copy() if item != order[i]]

            current_count = sum(order[i] in dict and remaining_items[j] in dict[order[i]] for j in range(len(remaining_items)))
            if(current_count == len(order) // 2):
                total += int(order[i])
        
    return total

if __name__ == "__main__":
    main()