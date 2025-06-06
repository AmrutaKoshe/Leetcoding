'''
We are basically given a directed graph and we want to detect if a loop is present in the graph or not.


METHOD 1: DFS 

For DFS implementation, make a visited array that will hold the following values - 
0 : not visited
1 : visiting
2 : visited

We traverse through the whole graph with depth first approach by traversing recursively through the neighbours. 
If we encounter a neighbour which is not yet visited i.e. visited[neighbour] == 0, 
we mark it as visiting, i.e. visited[neighbour] = 0.

If we come across a neighbour that is completely visited, i.e. 2, we return True (there is no loop for this particular neighbour).

However, if we encounter a neighbour that for which visited[neighbour] == 1, that means we have not completed visiting 
and there is a loop present here. Hence we return False for the whole program bcoz all the courses cannot be completed.

'''
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #convert the edge list into adjancency list.
    graph = {i:[] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    #all nodes are non-visited by default.
    #0: not visited, 1: visiting, 2:visited.
    visited = [0]*numCourses

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == 2:
            return True
        
        visited[course] = 0

        for neighbour in graph[course]:
            #if the dfs neighbour returns false, i.e. if there is loop in neighbour
            if not dfs(neighbour):
                return False
            
        #if we successfully go through all neighbours without any loop present, then we mark it as completed.
        visited[course] = 2
        return True

    for course in range(len(numCourses)):
        if visited[course] == 0:
            if not dfs(course):
                return False
        
    return True


'''
An example walkthrough where the answer would be TRUE - 

Consider the adjacency list:
0 : [1,2]
1 : [3,4]
2 : []
3 : [4]
4 : []

We'll start with visited = [0,0,0,0,0]

We will traverse through all the courses that are not already visited for range(len(numCourses)) 
0 is not visited, hence we'll mark it -- visited[0] = 1
Then, we go through the neighbours recursively.
1 is not visited, mark it -- visited[1] = 1
3 is not visited, mark it -- visited[3] = 1
4 is not visited, mark it -- visited[4] = 1
Now, there are no neighbours of 4. Hence, we complete the traversal for 4 -- visited[4] = 2.
Now, 3 has no other neighbours. Hence, complete traversal -- visited[3] = 2.
Now, the other neighbour of 1 is 4. But, visited[4] == 2 and we don't wanna traverse 4 again.
Hence return True and then mark visited[1] = 2.
The other neighbour of 0 is 2. 
Now, 2 has no neighbours. Hence, we finish the traversal and mark visited[2] = 2.
Now, 0 has no other neighbours left so we finish traversal and mark visited[0] = 2.

So, the visited array looks like - [2, 2, 2, 2, 2]
None of them have visited[n] = 0. hence, the for loop does not call the dfs function anymore and stops executing.
Hece, we return True at the end.

----------------------------------------------------------------------------------------------

Another example where a loop is detected i.e. FALSE

Consider the adjacency list:
0 : [1,2]
1 : [3]
2 : []
3 : [4]
4 : [1]

Initially, visited = [0,0,0,0,0]

We will traverse through all the courses that are not already visited for range(len(numCourses)) 
0 is not visited, hence we'll mark it -- visited[0] = 1
Then, we go through the neighbours recursively.
1 is not visited, mark it -- visited[1] = 1
3 is not visited, mark it -- visited[3] = 1
4 is not visited, mark it -- visited[4] = 1
Now, 1 is a neighbour for 4, but its already visited. Hence, return False.


TIME COMPLEXITY: 
E = number of edges(prerequisites list)
V = number of nodes(courses)

Since we're gonna traverse through all the nodes and edges once, it'll be O(V+E)

SPACE COMPLEXITY: 
Graph representation- Adjacency List takes O(V+E) space (but we won't consider this since its an input for the leetcode problem)
Visited array- takes O(V) space
Recursive Call Stack- takes O(V) space

Therefore, total space = O(V+E)

--------------------------------------------------------------------------------------------------------------------------------------\
METHOD 2: KAHN'S ALGORITHM W. BFS

Refer Kahn_Algo.py for the whole explanation.
But I'll still walkthrough a cyclic graph example here to see how it returns false.

graph = {
0: [1,2],
1: [3],
2: [],
3: [4],
4: [1]
}

in_degree = [0,2,1,1,1]

queue= [0], top_order = [0]
For 1 and 2, in-degree reduce by 1
in_degree = [0,1,0,1,1]
Push 2 to queue.

queue = [2]
top_order = [0, 2]
Now, 2 has no neighbours. 
So the queue is empty and we exit from the while loop.

The length of top_order is not equal to num of nodes. Hence, there is a cycle.

INTUITION Behind why Kahn Algorithm works for Cycle Detection:- 
If a cycle is present, there will always be nodes with non-zero in-degrees which will never get added to the queue.
When there is a 0 in_degree, that means all dependencies of that node have been removed, so no other node depends on this node.
But when there is a cycle, the nodes are inter-dependent on one another, so none of them can have 0 in-degree.

Hence, the while loop breaks without traversing through all nodes and the length of top_order is not equal to num nodes.

'''
from collections import deque

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #Adjacency list representation
    graph = {i:[] for i in range(numCourses)}

    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    in_degree = [0]*numCourses

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i]==0])

    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)

        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(top_order) == numCourses:
        return True

    else:
        return False
    
    '''
    TIME COMPEXITY: O(V+E)
    SPACE COMPLEXITY: O(V)

    '''