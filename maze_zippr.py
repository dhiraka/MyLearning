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
        if input_arr[i][-1] == 1:
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


def make_graph_of_maze(input_arr):
    connected_indices_dict = {}
    for i in range(len(input_arr)):
        for j in range(len(input_arr[i])):
            connected_index_list = []
            try:
                if input_arr[i][j + 1] == 1:
                    connected_index_list.append((i, j + 1))
            except:
                pass
            try:
                if input_arr[i][j - 1] == 1:
                    connected_index_list.append((i, j - 1))
            except:
                pass
            try:
                if input_arr[i - 1][j] == 1:
                    connected_index_list.append((i - 1, j))
            except:
                pass
            try:
                if input_arr[i + 1][j] == 1:
                    connected_index_list.append((i + 1, j))
            except:
                pass
            try:
                if input_arr[i - 1][j + 1] == 1:
                    connected_index_list.append((i - 1, j + 1))
            except:
                pass
            try:
                if input_arr[i - 1][j - 1] == 1:
                    connected_index_list.append((i - 1, j - 1))
            except:
                pass
            try:
                if input_arr[i + 1][j + 1] == 1:
                    connected_index_list.append((i + 1, j + 1))
            except:
                pass
            try:
                if input_arr[i + 1][j - 1] == 1:
                    connected_index_list.append((i + 1, j - 1))
            except:
                pass
            connected_indices_dict[(i, j)] = connected_index_list
    return connected_indices_dict


def get_possible_paths(maze_graph, first, last, path=[]):
    if first not in maze_graph:
        return []
    path = path + [first]
    if first == last:
        return [path]
    paths = []
    for point in maze_graph[first]:
        if point not in path:
            newpaths = get_possible_paths(maze_graph, point, last, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

input_arr = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]


maze_graph = make_graph_of_maze(input_arr)
number_of_paths = 0
all_possible_paths = []
for pair in get_possible_pairs(get_edge_door_indices(input_arr)):
    all_paths_list = get_possible_paths(maze_graph, pair[0], pair[1])
    all_possible_paths += all_paths_list
    number_of_paths += len(all_paths_list)
print all_possible_paths
print number_of_paths
