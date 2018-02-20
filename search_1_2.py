# This is a class implemented for queue data structure

from collections import deque, defaultdict
from heapq import heappop, heappush


# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted tree

#Class to represent a Tree
class Tree:
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.tree = [] # default dictionary 
                                # to store tree
        

    # function to add an edge to tree
    def addEdge(self,u,v,w):
        self.tree.append([u,v,w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's 
        # algorithm
    def KruskalMST(self):

        result =[] #This will store the resultant MST

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

            # Step 1: Sort all the edges in non-decreasing 
                # order of their
                # weight. If we are not allowed to change the 
                # given tree, we can create a copy of tree
        self.tree = sorted(self.tree, key=lambda item: item[2])

        parent = [] ; rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
    
        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :

            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
            u,v,w = self.tree[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)         
            # Else discard the edge

        # print the contents of result[] to display the built MST
        # print "Following are the edges in the constructed MST"
        # for u,v,weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            # print ("%d -- %d == %d" % (u,v,weight))
        return result

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    # print(height, width)
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j] == '%'}
    # print(graph)
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col] == '%':
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and not maze[row][col + 1] == '%':
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph



        

def find_path_dfs(maze, start, goal):
    stack = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    expanded = 0
    while stack:
        path, current = stack.pop()
        if current == goal:
            return path, expanded
        if current in visited:
            continue
        visited.add(current)
        expanded += 1
        for direction, neighbour in graph[current]:
            stack.append((path + direction, neighbour))
    return "NO WAY!"


def find_path_bfs(maze, start, goal):
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    expanded = 0
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path, expanded
        if current in visited:
            continue
        visited.add(current)
        expanded += 1
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"


def get_manhattan(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    
def heuristic(start, cell, goal):
    manhattan = get_manhattan(cell, goal)
    dx1 = cell[0] - goal[0]
    dy1 = cell[1] - goal[1]
    dx2 = start[0] - goal[0]
    dy2 = start[1] - goal[1]
    cross = abs(dx1*dy2 - dx2*dy1)
    return manhattan + cross*0.001


def find_path_gbfs(maze, start, goal):
    pr_queue = []
    heappush(pr_queue, (heuristic(start, start, goal), "", start))
    visited = set()
    graph = maze2graph(maze)
    expanded = 0
    while pr_queue:
        _, path, current = heappop(pr_queue)
        if current == goal:
            return path, expanded
        if current in visited:
            continue
        visited.add(current)
        expanded += 1
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (heuristic(start, neighbour, goal), 
                                path + direction, neighbour))
    return "NO WAY!"


def find_path_astar(maze, start, goal):
    pr_queue = []
    heappush(pr_queue, (0 + heuristic(start, start, goal), 0, "", start))
    visited = set()
    graph = maze2graph(maze)
    expanded = 0
    while pr_queue:
        _, cost, path, current = heappop(pr_queue)
        if current == goal:
            return path, expanded
        if current in visited:
            continue
        visited.add(current)
        expanded += 1
        for direction, neighbour in graph[current]:
            heappush(pr_queue, (cost + heuristic(start, neighbour, goal), cost + 1,
                                path + direction, neighbour))
    return "NO WAY!"


def draw_path(maze_map, path, start):
    labels = [  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a'
              , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
              , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
              , 'x', 'y', 'z']
    row, col = start
    count = 0
    # print(row, col)
    maze_sol = maze_map.copy()
    for direction in path:
        if direction == 'E':
            col += 1
        elif direction == 'S':
            row += 1
        elif direction == 'W':
            col -= 1
        elif direction == 'N':
            row -= 1
        if maze_sol[row][col] == '%':
            print('Bad path')
        elif maze_sol[row][col] == '.':
            maze_sol[row][col] = labels[count]
            count += 1
    row, col = start
    for direction in path:
        if direction == 'E':
            col += 1
        elif direction == 'S':
            row += 1
        elif direction == 'W':
            col -= 1
        elif direction == 'N':
            row -= 1
        if maze_sol[row][col] == '%':
            print('Bad path')
        elif maze_sol[row][col] == ' ':
            maze_sol[row][col] = '.'
    return maze_sol


def parse_file(fname):
    maze_file = open(fname, 'r')
    maze_map = []
    start = ()
    goal_dict = {}
    index_dict = {}
    row = 0
    col = 0
    count = 0
    for line in maze_file:
        char_list = []
        col = 0
        for char in line:
            if char == '\n': 
                continue
            char_list.append(char)
            if char == 'P':
                start = (row, col)
                goal_dict[count] = start
                index_dict[start] = count
                count += 1
            elif char == '.':
                goal = (row, col)
                goal_dict[count] = goal
                index_dict[goal] = count
                count += 1
            col += 1
        row += 1
        maze_map.append(char_list)
    maze_file.close()

    return maze_map, start, goal_dict, index_dict


def write_sol_to_file(fname, maze_sol):
    maze_file = open(fname, 'w')
    for line in maze_sol:
        for char in line:
            maze_file.write(char)
        maze_file.write('\n')
    maze_file.close()
    
def perm(k):
    k = tuple(k)
    lk = len(k)
    if lk <= 1:
        yield k
    else:
        for i in range(lk):
            s = k[:i] + k[i+1:]
            t = (k[i],)
            for x in perm(s):
                yield t + x
                
                
