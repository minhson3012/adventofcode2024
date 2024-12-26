def main():
    input = readFile("input.txt")
    # challenge1_result = challenge1(input)
    # print("Challenge 1: ", challenge1_result)
    challenge2_result = challenge2(input)
    print("Challenge 2: ", challenge2_result)

def challenge1(input):
    # Answer: 998
    computers = []
    indexes_to_check = set()
    for line in input:
        points = line.split("-")

        for point in points:

            if point not in computers:
                computers.append(point)

            if point[0] == "t":
                index = computers.index(point)
                indexes_to_check.add(index)

    connections = [[0] * len(computers) for _ in range(len(computers))]
    for line in input:
        points = line.split("-")

        x, y = computers.index(points[0]), computers.index(points[1])
        connections[x][y] = 1
        connections[y][x] = 1

    result = set()

    for i in indexes_to_check:
        points_to_check = []

        for j, x in enumerate(connections[i]):
            if x == 1:
                points_to_check.append(j)

        for j in points_to_check:
            for k, x in enumerate(connections[j]):
                if connections[j][k] and connections[i][k] and i != k and j != k:
                    connection = [i, j, k]
                    connection.sort()
                    result.add(tuple(connection))
    return len(result)

def challenge2(input):
    # Answer: cc,ff,fh,fr,ny,oa,pl,rg,uj,wd,xn,xs,zw
    graph = {}
    for line in input:
        points = line.split("-")

        if points[0] not in graph:
            graph[points[0]] = set()

        graph[points[0]].add(points[1])

        if points[1] not in graph:
            graph[points[1]] = set()
            
        graph[points[1]].add(points[0])

    cliques = []
    potential = set(graph.keys())
    magic_algo(set(), potential, set(), graph, cliques)

    largest_clique = max(cliques, key=len)
    return ",".join(sorted(largest_clique))

# Bron-Kerbosch algorithm
def magic_algo(current_clique, potential_nodes, processed_nodes, graph, cliques):
    if not processed_nodes and not potential_nodes:
        cliques.append(current_clique)
        return

    # Choose pivot
    pivot = next(iter(potential_nodes.union(processed_nodes)))

    # Check each candidate
    for v in list(potential_nodes - graph[pivot]):
        new_current_clique = current_clique.union([v])
        new_potential = potential_nodes.intersection(graph[v])
        new_processed = processed_nodes.intersection(graph[v])
        magic_algo(new_current_clique, new_potential, new_processed, graph, cliques)

        potential_nodes.remove(v)
        processed_nodes.add(v)

def readFile(filename):
    file = open(filename, "r")
    input_lines = file.read().splitlines()
    file.close()


    return input_lines

if __name__ == "__main__":
    main()