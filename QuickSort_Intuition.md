## Quick Sort Intuition:-

In quick sort, we need to choose a pivot and then modify the array such that the pivot takes its correct position in the array.
This means all the elements less than the pivot would be on the left side of the pivot whereas all the elements greater than it would be on its right side.

This works as follows - 
We take 2 pointers i and j.

To get a good idea about the intuition behind this, consider that all the elements before and including array[i] are those that are smaller than the pivot.
And pointer j is just used to traverse through the array.

Every time you traverse through the array, you check whether array[j] <= pivot. If this is the case, we need to increment i by 1 and then swap array[i] with array[j].
However, if array[j] > pivot, you do nothing and keep traversing.
After you reach the last element, which is the pivot, you swap array[i+1] with pivot and this ensures that the pivot is in the correct position.

---------------------------------------------------------------------------------------------------------------------------------------------------
Let's walk through an example to understand this better - 

Consider the array [8, 2, 4, 7, 1, 3, 9, 6, 5]

We would start with j=0 and i=-1.
Check if array[j] <= pivot -> nope -> do nothing

j=1 and i=-1
Check if array[j] <= pivot -> yep. So we increment i and swap array[i] with array[j]

Therefore, array = [2,8,4,7,1,3,9,6,5]

Now, i=0 and j=2 - once again 4<5 therefore, increament i and swap array[j] and array[i]

array = [2,4,8,7,1,3,9,6,5]

Now, i=1 and j=3 - do nothing
i=1 and j=4 -> i+=1 and swap(array[j], array[i])

*One more thing to note here is that all the elements before and including i are all smaller than the pivot, whereas all the elements between i and j are those that are larger than the pivot.*

array = [2,4,1,7,8,3,9,6,5]

i=2 and j=5 -> i+=1 and swap(array[j], array[i])

array = [2,4,1,3,8,7,9,6,5]

Now we keep incrementing j till it reaches the pivot.
And then swap array[i+1] with array[j] (Before all elements till array[i] are smaller than pivot)

Therefore, final array = [2,4,1,3,5,7,9,6,8]

-- This was just one iteration to place the pivot in its correct position. We do this recursively on both sides of the pivot to get a final sorted array at the end.






