dfs - recursion is easy
bfs - use double ended queue to implement the iterative approach


### Binary Search Trees

all values in its left side are less than the value in the node, all the values in its right subtree are
greater than the values in the node
values in the BST should be unique

With binary search tree searching, adding, removing can be done in O(log n) time on average

an inorder DFS (left, root, right) on a BST will handle the nodes in sorted order


### Graphs
directed or undirected: directed can only travel in one direction, undirected can travel in both directions
binary trees, the edges are directed, you can only go from parent to the child
connected component : group of nodes that are connected by edges, all nodes are reachable from the root
no. edges that can be used to reach a node are called the node's indegree
no. edges that are outgoing from the node are called the node's outdegree
nodes that are connected by an edge are called neighbors

cyclic - that the graph has a cycle
acyclic - graph doesn't has a cycle

hash map : that mapped integers to lists of integers

have a seen set or a seen array which will mark the index of the visited node, whichever is faster


Reorder edges : check how many edges you need to reorder that are away from 0




