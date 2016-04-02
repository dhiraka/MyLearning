input_arr = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]
function get_edge_door_indices(input_arr){
    edge_doors_indices = [];
    top_edge = input_arr[0];
    for (i = 0; i < top_edge.length; i++) {
        if (top_edge[i] == 1) {
            edge_doors_indices.push([0, i]);
        }
    }
    input_arr_len = input_arr.length
    bottom_edge = input_arr[input_arr_len - 1]
    for (i = 0; i < bottom_edge.length; i++) {
        if (bottom_edge[i] == 1){
            edge_doors_indices.push([input_arr_len - 1, i]);
        }
    }
    for (i = 0; i < input_arr.length - 1; i++) {
        if (input_arr[i][0] == 1){
            edge_doors_indices.push([i, 0]);
        }
        if (input_arr[i][(input_arr[i]).length-1] == 1){
            edge_doors_indices.push([i, input_arr[i].length - 1]);
        }
    }

    return edge_doors_indices
}

function get_possible_pairs(edge_doors_indices){
    start_end_pairs = [];
    num_edge_door_indices = edge_doors_indices.length;
    for (i = 0; i < num_edge_door_indices - 1; i++) {
        j = i + 1;
        while (j < num_edge_door_indices){
            start_end_pairs.push(
                [edge_doors_indices[i], edge_doors_indices[j]]);
            j += 1;
        }
    }
    return start_end_pairs;
}

function make_graph_of_maze(input_arr){
    var connected_indices_dict = {};
    for (i = 0; i < input_arr.length; i++) {
        for (j = 0; j < (input_arr[i]).length; j++) {
            connected_index_list = []
            try{
                if (input_arr[i][j + 1] == 1){
                    connected_index_list.push([i, j + 1]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i][j - 1] == 1){
                    connected_index_list.push([i, j - 1]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i - 1][j] == 1){
                    connected_index_list.push([i - 1, j]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i + 1][j] == 1){
                    connected_index_list.push([i + 1, j]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i - 1][j + 1] == 1){
                    connected_index_list.push([i - 1, j + 1]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i - 1][j - 1] == 1){
                    connected_index_list.push([i - 1, j - 1]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i + 1][j + 1] == 1){
                    connected_index_list.push([i + 1, j + 1]);
                }
            }
            catch (e) {
            }
            try{
                if (input_arr[i + 1][j - 1] == 1){
                    connected_index_list.push([i + 1, j - 1]);
                }
            }
            catch (e) {
            }
            connected_indices_dict[[i, j]] = connected_index_list;
        }
    }
    return connected_indices_dict
}

function arraysEqual(arr1, arr2) {
    if(arr1.length !== arr2.length)
        return false;
    for(var i = arr1.length; i--;) {
        if(arr1[i] !== arr2[i])
            return false;
    }

    return true;
}

function needleInHaystack(haystack, needle){
  for(i = 0; i < haystack.length; i++){
    if(arraysEqual(haystack[i], needle)){
      return true;
    }
  }
  return false;
}


function get_possible_paths(maze_graph, first, last, path){
    if (!(first in maze_graph)){
        return [];
    }
    path.push(first)
    if (arraysEqual(first, last)){
        return [path];
    }
    var paths = [];
    cncted_pts_arr = maze_graph[first]
    for (i = 0; i < cncted_pts_arr.length; i++){
        point = cncted_pts_arr[i]
        if (!(needleInHaystack(path, point))){
            newpaths = get_possible_paths(maze_graph, point, last, path);
            for (i = 0; i < newpaths.length; i++){
                newpath = newpaths[i]
                // console.log(newpath)
                paths.push(newpath);
                // console.log(paths)
            }
        }
    }
    return paths;
}


var maze_graph = make_graph_of_maze(input_arr);
// console.log(maze_graph);
// console.log(maze_graph[[0,1]]);
var number_of_paths = 0
var all_possible_paths = [];

// console.log(get_possible_pairs(get_edge_door_indices(input_arr)));
possible_pairs = get_possible_pairs(get_edge_door_indices(input_arr));

for (k = 0; k < possible_pairs.length; k++) {
    // console.log("Entering with "+k.toString())
    pair = possible_pairs[i]
    // console.log(pair[0]);
    // console.log(pair[1]);
    all_paths_list = get_possible_paths(maze_graph, pair[0], pair[1], []);
    all_possible_paths = all_possible_paths.concat(all_paths_list);
    number_of_paths += all_paths_list.length;
    // console.log(all_paths_list)
    // console.log(number_of_paths)
}

console.log(all_possible_paths);
console.log(number_of_paths);

// console.log(arraysEqual([3,3], [3,3]));
// console.log(needleInHaystack([[3,3]], [3,3]));

// console.log(get_possible_pairs(get_edge_door_indices(input_arr)));
// console.log(make_graph_of_maze(input_arr));
