# -*- coding: utf-8 -*-

class Node:
    def __init__(self,id=None):
        self.id = id

    def __str__(self):
        if self.id is None:
            return "Node"
        return str(self.id)

class Edge:
    def __init__(self,from_node,to_node,weight = 1,directed = True):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

        self.connector = " -> "
        if not directed:
            self.connector = " -- "

    def __repr__(self):
        return str(self.from_node).replace(" ","_") + self.connector + str(self.to_node).replace(" ","_") + " [label=" + str(self.weight) + "]"


class DiGraph:
    def __init__(self,nodes,edges):
        self.nodes = nodes
        self.edges = edges

    def __repr__(self):
        s = "digraph {\n"
        for e in self.edges:
            s += "    " + str(e) + "\n"

        s += "}"

        return s

class Graph(DiGraph):
    def __init__(self,nodes,edges):
        DiGraph.__init__(self,nodes,edges)

    def __repr__(self):
        s = "graph {\n"
        for e in self.edges:
            s += "    " + str(e) + "\n"

        s += "}"

        return s

