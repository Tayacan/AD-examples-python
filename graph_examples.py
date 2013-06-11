from graph import *

def minimum_spanning_example():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    g = Graph([a,b,c,d,e],
            [
                Edge(a,b,2,False),
                Edge(a,c,3,False),
                Edge(b,d,1,False),
                Edge(c,e,4,False),
                Edge(c,d,2,False),
                Edge(b,e,3,False)
                ]
            )

    print g

def dijkstra_fail():
    # graph where dijkstra's fails.
    nodes = []
    edges = []
    nodes.append(Node('a'))
    nodes.append(Node('b'))
    nodes.append(Node('c'))
    nodes.append(Node('d'))

    edges.append(Edge(nodes[0],nodes[1],4))
    edges.append(Edge(nodes[0],nodes[2],2))
    edges.append(Edge(nodes[1],nodes[2],-3))
    edges.append(Edge(nodes[2],nodes[3],1))

    g = DiGraph(nodes,edges)
    print g

if __name__ == "__main__":
    #minimum_spanning_example()
    dijkstra_fail()
