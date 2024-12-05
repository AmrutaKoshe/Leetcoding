# LC: 973 https://leetcode.com/problems/k-closest-points-to-origin/description/

'''
We are given a list of points in a 2D plane and a number K. We need to find K closest points to the origin (0,0), where distance = sqrt(x^2 + y^2).
Since we care about relative closeness, we can skip the square root part and just consider x^2 + y^2.

APPROACH 1 - Brute Force.
Calculate the distance for all points and store them in a list. 
Sort the list by distance.
Return the first K points.

TC - To calculate distances = O(n)
    Sorting the list = O(nlogn)
    Slicing = O(k)
    Overall = O(nlogn)

SC - O(n) for list of distances
'''

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    distances = [(x**2 + y**2, (x,y)) for x,y in points]
    distances.sort(key=lambda x:x[0])

    return [point for _,point in distances[:k]]

'''
APPROACH 2 - Max Heap (Optimal for large K)
Better approach since sorting all n points is unnecessary if we only need the K closest points.

Use a max heap to keep track of K closest points seen so far. Largest element in heap = farthest point, hence we want to calculate the smallest elements in heap.
We use max heap, because a max heap has the maximum element at the root, where each parent node is larger than its children. We pop elements from the root.
Hence, the larger elements will be popped out and the smaller distances (closest points) will remain.

Eg:  -7
    /  \
   -6  -5
NOTE: By default, the heap is a min heap in python. Hence, max heaps are implemented by negating the numbers and pushing them on the heap. 
Hence, the negative versions of larger numbers are at the top. They are then negated again to get the output

In the heap above, if K=2, -7 will be popped out. Hence, the points associated with -6 and -5 i.e. the smaller distances will be generated as the o/p.

TC- Heap operation takes O(log K). For each point, if heap size < k, we push the point to heap. If heap size >k, we push point + pop other point.
Hence, for n points, TC => O(nlogK)

SC- The heap stores k points at ny given time => O(k)
'''
import heapq
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    max_heap = []

    for x,y in points:
        distance = -(x**2 + y**2)
        heapq.heappush(max_heap, (distance, (x,y)))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for (_, point) in max_heap]


'''
APPROAH 3 - Quickselect (Optimal for Small K)
'''
