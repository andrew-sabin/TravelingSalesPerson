import sys
infinity = sys.maxsize

def solve_tsp(G):
    visited = {}
    path = []
    start_node = 0
    curr_node = start_node
    path.append(curr_node)
    nodes_left = len(G)
# set a list of visited nodes and a starting node
    while nodes_left > 0:
        if nodes_left > 1:
            curr_min = infinity
            node = None
            for edge in range(len(G[curr_node])):
                if curr_min > G[curr_node][edge] and G[curr_node][edge] != 0 and edge not in visited:
                    curr_min = G[curr_node][edge]
                    node = edge
            if node != None:
                path.append(node)
                visited[curr_node] = node
                curr_node = node
                nodes_left -= 1
            else:
                curr_node = path[len(path)-1]
                path.pop()
                nodes_left += 1
        elif nodes_left == 1:
            if G[curr_node][start_node] != 0:
                visited[curr_node] = 0
                curr_node = 0
                path.append(curr_node)
                nodes_left -= 1
            else:
                curr_node = path[len(path)-1]
                path.pop()
                nodes_left += 1
    return path




# create a loop that goes through the array of different values in the 2D array

# make a loop that finds the smallest value in the row while checking to see if it has been visited




# Graph for testing

G = [
[0, 2, 3, 20, 1],
[2, 0, 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0],
]

print(solve_tsp(G))