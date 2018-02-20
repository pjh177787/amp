# This is a class implemented for queue data structure

from collections import deque
from heapq import heappop, heappush


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


def heuristic(start, cell, goal):
    manhattan = abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])
    return manhattan


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


def draw_path(maze_map, path, start, goal):
    row, col = start
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
        else:
            maze_sol[row][col] = '.'
    if not (row, col) == goal:
        print('Bad path')
    return maze_sol


def parse_file(fname):
    maze_file = open(fname, 'r')
    maze_map = []
    start = ()
    goal = ()
    row = 0
    col = 0
    for line in maze_file:
        char_list = []
        col = 0
        for char in line:
            if char == '\n': 
                continue
            char_list.append(char)
            if char == 'P':
                start = (row, col)
            elif char == '.':
                goal = (row, col)
            col += 1
        row += 1
        maze_map.append(char_list)
    maze_file.close()
    return maze_map, start, goal


def write_sol_to_file(fname, maze_sol):
    maze_file = open(fname, 'w')
    for line in maze_sol:
        for char in line:
            maze_file.write(char)
        maze_file.write('\n')
    maze_file.close()
    