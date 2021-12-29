# OOP_Ex3

A directed weighted graph which runs graph algorithms such as center, shortest path, and TSP

![github-small](https://github.com/Israel0545488592/OOP_Ex3/blob/master/GUI/Figure_1.png)


The main idea of the implementation is to use python dictionary as hashMap

The graph implementation is under classes.py.
In addition, we implemented another few assisting structures.

Name            |Description
---             | --- |
DiGraph         |Implements GraphInterface.
Path            | Represents a weighted path in graph
TagHeap         | A data structure to hold the graph as heap


### Path
An assist structure to hold a path when implementing path-related algorithms (such as shortest path and TSP) 

### TagHeap
An assist structure to hold temporary information for ShortestPath method

## GraphAlgo
Implements GraphAlgoInterface.py
We added a few additional algorithms to assist us

dijkstra(src, dst) - returns a single sourced shortest path from src to dest.
implemented using Tag heap and path mentioned above.

DFS -  Depth-First search, used to check whether a graph is connected one way.

Transpose - transposes the graph, flips the edges "inside-out".

isConnected - returns whether a graph is strongly connected, using DFS and transpose as mentioned above.
Used for finding the graph's center that would exist only when it is connected.

## Motivation
The purpose of the assignment is to make a comparison between programming languages unto a similar projects.

In this assignment we implemented a much more efficient structure compared to previous one. 
More detail can be found in our wiki.
