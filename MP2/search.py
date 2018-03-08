import operator
from collections import deque, defaultdict
from copy import deepcopy
from heapq import heappop, heappush

class Q:
    def __init__(self, arr=[]):
        self.q = arr

    def pop(self):
        elem = self.q[0]
        del self.q[0]
        return elem

    def peek(self, idx = 0):
        return self.q[idx]

    def push(self, elem):
        self.q.append(elem)

    def size(self):
        return len(self.q)

    def to_string(self):
        ret_str = ''
        for elem in self.q:
            ret_str +=  elem + ' '
        return ret_str

class Factory_Map:
    def __init__(self):
        self.graph = {
            'A':[(277, 'E'), (673, 'C'), (1064, 'B'), (1401, 'D')],  
            'B':[(337, 'E'), (958, 'C'), (1064, 'A'), (1934, 'D')], 
            'C':[(399, 'E'), (673, 'A'), (958, 'B'), (1001, 'D')], 
            'D':[(387, 'E'), (1001, 'C'), (1401, 'A'), (1934, 'B')], 
            'E':[(277, 'A'), (337, 'B'), (387, 'D'), (399, 'C'), ]}
        self.factories = ['A', 'B', 'C', 'D', 'E']
        pass

    def get_factorys(self):
        return self.factories
    def get_graph(self):
        return self.graph
    def get_widget1(self):
        widget = Q(['A', 'E', 'D', 'C', 'A'])
        return widget   
    def get_widget2(self):
        widget = Q(['B', 'E', 'A', 'C', 'D'])
        return widget   
    def get_widget3(self):
        widget = Q(['B', 'A', 'B', 'C', 'E'])
        return widget   
    def get_widget4(self):
        widget = Q(['D', 'A', 'D', 'B', 'D'])
        return widget   
    def get_widget5(self):
        widget = Q(['B', 'E', 'C', 'B', 'D'])
        return widget   
    
    def get_len(self, widget):
        return widget.size()

    def get_dist(self, start, goal):
        pr_queue = []
        graph = self.get_graph()
        heappush(pr_queue, (0, '', start))
        visited = set()
        while pr_queue:
            cost, path, current = heappop(pr_queue)
            if current == goal:
                return cost, path
            if current in visited:
                continue
            visited.add(current)
            for distance, neighbour in graph[current]:
                heappush(pr_queue, (cost + distance, path + neighbour, neighbour))
        return -1
    
    def get_frontier(self, widgets):
        frontier = {}
        for widget in widgets:
            if not widget.size() == 0:
                factory = widget.peek()
                if not factory in frontier:
                    frontier[factory] = 1
                else:
                    frontier[factory] += 1
        return frontier
        
    
