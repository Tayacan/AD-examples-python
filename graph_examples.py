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


if __name__ == "__main__":
    minimum_spanning_example()
