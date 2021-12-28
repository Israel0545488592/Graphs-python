# OOP_Ex3

![github-small](https://github.com/Israel0545488592/OOP_Ex3/blob/master/GUI/Figure_1.png)



The main idea of the implementation is to use python dictionary as hashMap

The graph implementation is under classes.py.
In addition, we implemented another few assisting structures.

Name            |Description
---             | --- |
DiGraph         |Implements GraphInterface.
Path            | Represents a weighted path in graph
TagHeap         | A data structure to hold the graph as heap


### DiGraph
Field|Description
--- | --- |
Nodes| a dict of node ids
Edges| a dict of a dict of edges, the upper dict representing the source
MC| Modification counter

### Path
An assist structure to hold a path when implementing path-related algorithms (such as shortest path and TSP) 

Field|Description
--- | --- |
Graph| Holds the graph that path is in
rout| A list of nodes within the path, ordered with the route (from last to first)
Weight| The overall weight of the path

Function|Description
--- | --- |
get_length()| returns the route's length
add(nod)| Adds a given node to the start of the route
update_weight()| updates the weight of the graph with the last added node
remove(last)| removes the last node from the route whenever last is true, otherwise removes the first
merge(p)| merges and connects path p into the current path

### TagHeap
An assist structure to hold temperry information fore ShortesPath method

Field|Description
--- | --- |
Graph| Holds the graph to allow access to the weights of the edges and tags of the nodes
min| An id of the node that holds the minimal weight value
values| a list holds the weight of a node in relation to a path

Function|Description
--- | --- |
get_min()| returns the min's value
get(ind)| returns the value of node with given index
relax(val, ind)| relaxes the value of a node with given index
update_chosen(ind)| updates the node's tag with given index
update_min()| updates all the values that aren't done (tag = 0)

## GraphAlgo
Implements GraphAlgoInterface.py
We added a few additional algorithms to assist us

dijkstra(src, dst) - returns a single sourced shortest path from src to dest.
implemented using Tag heap and path mentioned above.


DFS -  Depth-First search, used to check whether a graph is connected one way.

Transpose - transposes the graph, flips the edges "inside-out".

isConnected - returns whether a graph is strongly connected, using DFS and transpose as mentioned above.
Used for finding the graph's center that would exist only when it is connected.
