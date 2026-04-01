##==========================================================================
## Swethan Sivasegaran (20798865)
## CS 234 Spring 2023
## Assignment 3 Question 2
##==========================================================================
from stackqueue import Stack, Queue
from graph import UndirectedGraph

##==========================================================================
## Q2a:

## Start with an empty UndirectedGraph:
mygraph = UndirectedGraph()

## Add steps here as necessary.
mygraph.add_vertex(51)
mygraph.add_vertex(81)
mygraph.add_vertex(10)
mygraph.add_vertex(13)
mygraph.add_vertex(16)
mygraph.add_vertex(12)
mygraph.add_vertex(41)
mygraph.add_vertex(71)
mygraph.add_vertex(11)
mygraph.add_edge(51, 10)
mygraph.add_edge(13, 10)
mygraph.add_edge(16, 41)
mygraph.add_edge(11, 41)
mygraph.add_edge(41, 12)
mygraph.add_edge(71, 12)
mygraph.add_edge(71, 11)
## This verifies that you haven't accidentally turned replaced mytree
## with an object of the wrong type.
assert type(mygraph) == UndirectedGraph, "mygraph is not an UndirectedGraph" 


##==========================================================================
## Q2b:

## edges_to_graph(edges): Given a list of edges, returns an UndirectedGraph
## that contains only the edges in the given edge list and the vertices
## associated with it.
## edges_to_graph: list[tuple[int, int]] -> UndirectedGraph
##==========================================================================
def edges_to_graph(edges: list[tuple[int, int]]) -> UndirectedGraph:
    edge_graph = UndirectedGraph()
    length = len(edges)
    for i in range(length):
        vertex_list = edge_graph.vertices()
        edge = edges[i]
        vertex_one = edge[0]
        vertex_two = edge[1]
        length = len(vertex_list)
        exist_one = False
        exist_two = False
        for i in range(length):
            vertex = vertex_list[i]
            if (vertex == vertex_one):
                exist_one = True
            if (vertex == vertex_two):
                exist_two = True
        if (exist_one == False):
            edge_graph.add_vertex(vertex_one)
        if (exist_two == False):
            edge_graph.add_vertex(vertex_two)
        edge_graph.add_edge(vertex_one, vertex_two)

    return edge_graph
##==========================================================================
## Testing for Q2b:
print(edges_to_graph([(10, 13)]))
print(edges_to_graph([(10,13),(10,51),(11,41),(11,71),(12,41),(12,71),(16,41)]))
##==========================================================================


##==========================================================================
## Q2c:

## connected_subgraph(g,v): Given an UndirectedGraph g and vertex v, returns
## a new UndirectedGraph containing vertex v and all vertices that have a path
## to v in the given UndirectedGraph g. In addition, all edges that are
## incident to these vertices are included as well. Essentially, the function
## returns the component containing vertex v of the given UndirectedGraph g.
## Effects: Mutates the vertex colour of each vertex in the given
## UndirectedGraph g. More specifically, all vertices have vertex colour white
## except the vertices that are part of the component containing vertex v in
## the given UndirectedGraph g. These vertices have vertex colour black.
## Requires: v is a vertex in the given UndirectedGraph g
## connected_subgraph: UndirectedGraph int -> UndirectedGraph
##==========================================================================
def connected_subgraph(g: UndirectedGraph, v: int) -> UndirectedGraph:
    subgraph = UndirectedGraph()
    vertices = Queue()
    vertices.enqueue(v)
    vertex_list = g.vertices()
    length = len(vertex_list)
    for i in range(length):
        vertex = vertex_list[i]
        g.set_vertex_colour(vertex, "white")
    while (vertices.is_empty() == False):
        vertex = vertices.dequeue()
        g.set_vertex_colour(vertex, "black")
        neighbours = g.neighbours(vertex)
        length = len(neighbours)
        for i in range(length):
            neighbour = neighbours[i]
            if (g.vertex_colour(neighbour) == "white"):
                vertices.enqueue(neighbour)
    length = len(vertex_list)
    for i in range(length):
        vertex = vertex_list[i]
        if (g.vertex_colour(vertex) == "black"):
            subgraph.add_vertex(vertex)
    length = len(vertex_list)
    for i in range(length):
        vertex = vertex_list[i]
        if (g.vertex_colour(vertex) == "black"):
            index = i + 1
            while (index < length):
                neighbour = vertex_list[index]
                if (g.are_adjacent(vertex, neighbour)):
                    subgraph.add_edge(vertex, neighbour)
                index = index + 1
            
            
    return subgraph
##==========================================================================    
## Testing for Q2c:

print(connected_subgraph(mygraph, 16))
print(connected_subgraph(mygraph, 51))
print(connected_subgraph(mygraph, 81))
##==========================================================================
