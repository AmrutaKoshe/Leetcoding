# 1. Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers in the array such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Examples
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Input: nums = [3,2,4], target = 6
Output: [1,2]
```

## Approach & Explanation
We can solve this using a hash map to store the numbers we've seen and their indices. For each number:
1. Calculate the complement (target - current number)
2. If the complement exists in our hash map, we've found our pair
3. If not, store the current number and its index in the hash map
4. Continue until we find a solution

This approach allows us to find the solution in a single pass through the array.

## Time Complexity
- O(n) where n is the length of the input array
- We only need to traverse the array once

## Space Complexity
- O(n) to store at most n elements in the hash map

## Additional Notes
- The hash map approach trades space complexity for better time complexity
- A brute force approach would be O(n²) time complexity but O(1) space complexity 