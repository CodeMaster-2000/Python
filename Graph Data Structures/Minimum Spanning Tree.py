##==========================================================================
## Swethan Sivasegaran (20798865)
## CS 234 Spring 2023
## Assignment 3 Question 3
##==========================================================================
from stackqueue import Stack, Queue
from tree import OrderedTree
from graph import UndirectedGraph


##==========================================================================
## Q3:

## minimum_spanning_tree(g, id0): Given an UndirectedGraph g and the ID id0 
## of a particular node, return a minimum spanning tree rooted at the node
## with the given ID id0 of the type OrderedTree
## Effects: Mutates the vertex colour of every vertex in the given
## UndirectedGraph g such that the vertex colour of every vertex is white
## except the vertices of g that have a path to the node in the
## UndirectedGraph g that has the given ID id0. These vertices have vertex
## colour black.
## Requires: Given UndirectedGraph g is connected and there exists a node
## in g with ID id0
## minimum_spanning_tree: UndirectedGraph int -> OrderedTree
##==========================================================================
def minimum_spanning_tree(g: UndirectedGraph, id0: int) -> OrderedTree:
    vertex_list = g.vertices()
    length = len(vertex_list)
    for i in range(length):
        vertex = vertex_list[i]
        g.set_vertex_colour(vertex, "white")
    min_span_tree = OrderedTree()
    vertices = Queue()
    vertex = min_span_tree.add_leaf(None, id0)
    g.set_vertex_colour(id0, "black")
    vertices.enqueue(vertex)
    while (vertices.is_empty() == False):
        vertex = vertices.dequeue()
        vertex_id = min_span_tree.value (vertex)
        neighbours = g.neighbours(vertex_id)
        length = len(neighbours)
        for i in range (length):
            child = neighbours[i]
            if (g.vertex_colour(child) == "white"):
                leaf = min_span_tree.add_leaf(vertex, child)
                g.set_vertex_colour(child, "black")
                vertices.enqueue(leaf)
    return min_span_tree
##==========================================================================
## Testing for Q3:
## You may copy your edges_to_graph function here, or otherwise create
## the value g to help test your function.

#g = UndirectedGraph()
#g.add_vertex(16)
#g.add_vertex(41)
#g.add_vertex(11)
#g.add_vertex(71)
#g.add_vertex(12)
#g.add_edge(16, 41)
#g.add_edge(11, 41)
#g.add_edge(11, 71)
#g.add_edge(12, 41)
#g.add_edge(12, 71)
## These trees should exactly match what is shown in the diagram.  If
## they have the right nodes, but the wrong order, that indicates you
## are traversing in the wrong order.

#t = minimum_spanning_tree(g, 16)
#assert type(t) == OrderedTree, "t is not an OrderedTree"
#print(t)

#print(minimum_spanning_tree(g, 11))

#print(minimum_spanning_tree(g, 71))
##==========================================================================
