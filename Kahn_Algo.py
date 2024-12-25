'''
Kahn's Algorithm is used for Topological Sorting.
Topological Sorting is basically ordering the nodes of a Directed Acyclic Graph (A graph where edges are directed, but there is no cycle present) such that for every directed edge u->v in the graph, u comes before v in the ordering.

Example :
graph = {
    0: [1,2],
    1: [3,4],
    2: [],
    3: [4],
    4: []
}

One possible topological order would be 0,1,2,3,4
Even 0,2,1,3,4 is correct.

Algorithm Approach- 

- We first calculate the in-degree(number of incoming edges) for each node in the graph.
For our example, in_degree = [0,1,1,1,2]

-Then, we initialize the queue with all nodes that have in-degree 0.

-While the queue is not empty, we remove one node from the queue, add it to the topological order (result), and for all its neighbours, we subtract 1 from their in-degrees.
If a neighbour's in-degree becomes 0, we add it to the queue so that it can be processed.

-If the length of topological order = num of nodes, the graph is DAG and we got the result.

EXAMPLE WALKTHROUGH:- 
in_degree = [0,1,1,1,2]

Therfore, queue = [0]
Remove 0 out and put it into result. For neighbours (1 and 2), reduce in-degree by 1.
res = [0], in_degree = [0,0,0,1,2]
Add 1 and 2 to queue because in_degree = 0.

queue = [1,2]
Remove 1, put it into result and reduce in_degree by 1 for 3 and 4.
res = [0,1], in_degree = [0,0,0,0,1]
Add 3 to queue

queue = [2,3]
Remove 2
res = [0,1,2]

queue = [3]
Remove 3 and reduce in_degree by 1 for 4.
res = [0,1,2,3], in_degree = [0,0,0,0,0]
Add 4 to queue

queue = [4]
Remove 4.
res = [0,1,2,3,4]
'''

from collections import deque

def kahn(numNodes, graph):
    
    #initialise in_degree array
    in_degree = [0]*numNodes
    
    #Fill in_degree by iterating over the graph (adjacency list)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            
    #Initialise queue with all nodes with in-degree=0
    queue = deque([i for i in range(numNodes) if in_degree[i]==0])
    #we're supposed to pass an interable (list,tuple, string etc.) while initialising a deque
    
    top_order = []
    
    while queue:
        node = queue.popleft()
        top_order.append(node)
        
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)
                
    if len(top_order) == numNodes:
        return top_order
    else:
        return []
        
numNodes = 5

graph = {
    0: [1,2],
    1: [3,4],
    2: [],
    3: [4],
    4: []
}

print(kahn(numNodes, graph))

'''
TIME COMPLEXITY:
In-degree calculation: O(V+E)
Queue processing: Each vertex and edge is processed once, therefore O(V+E)

Overall = O(V+E)

SPACE COMPLEXITY:
In-degree array: O(V)
Queue: O(V)
(We are not considering the adjacency list O(V+E) bcoz that would be a given input if this was a leetcode problem and in coding challenges, we only consider "additional" space utilised.)

Overall = O(V)
'''