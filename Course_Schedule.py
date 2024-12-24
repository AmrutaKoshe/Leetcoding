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


'''