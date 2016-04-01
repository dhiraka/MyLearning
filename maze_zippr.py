def get_edge_door_indices(input_arr):
    edge_doors_indices = []
    top_edge = input_arr[0]
    for i in range(0, len(top_edge)):
        if top_edge[i] == 1:
            edge_doors_indices.append((0, i))
    input_arr_len = len(input_arr)
    bottom_edge = input_arr[input_arr_len - 1]
    for i in range(0, len(bottom_edge)):
        if bottom_edge[i] == 1:
            edge_doors_indices.append((input_arr_len - 1, i))
    for i in range(1, len(input_arr) - 1):
        if input_arr[i][0] == 1:
            edge_doors_indices.append((i, 0))
        if input_arr[i][:-1] == 1:
            edge_doors_indices.append((i, len(input_arr[i]) - 1))

    return edge_doors_indices


def get_possible_pairs(edge_doors_indices):
    start_end_pairs = []
    num_edge_door_indices = len(edge_doors_indices)
    for i in range(0, num_edge_door_indices - 1):
        j = i + 1
        while j < num_edge_door_indices:
            start_end_pairs.append(
                [edge_doors_indices[i], edge_doors_indices[j]])
            j += 1
    return start_end_pairs


def get_possible_path_between_indices(start_ind, end_ind, input_arr, path=[]):
    shortest_dist_from_start_dict = {}
    for i in range(len(input_arr)):
        for j in range(len(input_arr[i])):
            shortest_dist_from_start_dict[(i, j)] = None
    right_el = input_arr[i][j + 1]
    left_el = input_arr[i][j - 1]
    upper_el = input_arr[i - 1][j]
    lower_el = input_arr[i + 1][j]
    right_upper_el = input_arr[i - 1][j + 1]
    left_upper_el = input_arr[i - 1][j - 1]
    right_upper_el = input_arr[i + 1][j + 1]
    left_upper_el = input_arr[i + 1][j - 1]

    list_of_possible_paths = []
    return list_of_possible_paths


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

input_arr = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]


print get_possible_pairs(get_edge_door_indices(input_arr))


# Get all the edges.
# For every pair of edges, get all possible paths
