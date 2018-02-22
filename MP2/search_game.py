from collections import deque, defaultdict
from copy import deepcopy
from heapq import heappop, heappush

class Q:
    def __init__(self, arr):
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
        pass

    def get_factorys(self):
        return ['A', 'B', 'C', 'D', 'E']
    def get_graph(self):
        return {
            'A':[(277, 'E'), (673, 'C'), (1064, 'B'), (1401, 'D')],  
            'B':[(337, 'E'), (958, 'C'), (1064, 'A'), (1934, 'D')], 
            'C':[(399, 'E'), (673, 'A'), (958, 'B'), (1001, 'D')], 
            'D':[(387, 'E'), (1001, 'C'), (1401, 'A'), (1934, 'B')], 
            'E':[(277, 'A'), (337, 'B'), (387, 'D'), (399, 'C'), ]}
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


    def get_dist (self, fact_0, fact_1):
        graph = self.get_graph()
        for elem in graph[fact_0]:
            if elem[1] == fact_1:
                return elem[0]
        return 99999
