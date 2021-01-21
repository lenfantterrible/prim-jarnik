#!/bin/python3.8
from sys import maxsize
from functools import cmp_to_key
import hashlib 


class Node:
    def __init__(self, name, cost=maxsize, prev=None):
        self.name = name 
        self.cost = cost 
        self.prev = prev
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.name == other.name)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.__repr__())
    
    def __str__(self):
        return self.__repr__()


class Graph:
    v = set() 
    e = list()

    def add(self, input_str):
        splitted = input_str.split()
        node1 = Node(splitted[0])
        node2 = Node(splitted[1])
        cost = int(splitted[2])
        self.v.add(node1)
        self.v.add(node2)
        self.e.append((cost, node1, node2))
    
    def get_neighbours(self, node, pq):
        out = list()
        for edge in self.e:
            if(edge[1] == node or edge[2] == node):
                if(edge[1] in pq or edge[2] in pq):
                    out.append(edge)
        return out 

    def remove_vertice(self, node):
        for edge in self.e:
            if(edge[1] == node or edge[2] == node):
                self.e.remove(edge)
        self.v.remove(node)


def compare(item1, item2): #comparator for PriorityQueue 
    return item1.cost - item2.cost 


def prim(g): 
    s = list(g.v)[0]
    s.cost = 0 
    mst = list() 

    pq = list()
    for vertice in g.v: 
        pq.append(vertice)
    pq = sorted(pq, key=cmp_to_key(compare), reverse=True) 

    while(len(pq) > 0):
        v = pq.pop()

        if v.prev is not None:
            mst.append((v, v.prev)) 
        
        for edge in g.get_neighbours(v, pq):
            u = edge[1] if edge[2] == v else edge[2] 
            if u.cost > edge[0]:
                u.cost = edge[0] # edge[0] = weight 
                u.prev = v 
                pq[pq.index(u)] = u
                pq = sorted(pq, key=cmp_to_key(compare), reverse=True) # decrease key of U 

    return mst


if __name__ == '__main__':
    g = Graph() 
    while(True):
        inp = input() 
        if(inp == '-1'):
            break 
        g.add(inp)

    print(prim(g))
