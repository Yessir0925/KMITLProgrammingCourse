"""Problem Statement :

Take input as a list of ordered pairs to construct a weighted directed graph. Then, display the shortest path using Dijkstra’s Shortest Path Algorithm.



 *** Shortest Path (Dijkstra's Algorithm) ***
Enter : v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3/v0 v1,v0 v2,v0 v3
v0 to v1 : v0->v1
v0 to v2 : v0->v1->v2
v0 to v3 : v0->v3
===== End of program ======




Input Format
The input consists of two parts, separated by /.

Part 1: Graph edges
Each edge is given as:

source weight destination
Multiple edges are separated by commas.
Example:

v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3
Means:

Edge from v0 → v1 with weight 1

Edge from v1 → v2 with weight 1

Edge from v2 → v3 with weight 1

Edge from v0 → v3 with weight 1

Part 2: Shortest path queries
Each query is written as:

start_vertex target_vertex
Multiple queries are separated by commas.
Example:

v0 v1,v0 v2,v0 v3
x"""