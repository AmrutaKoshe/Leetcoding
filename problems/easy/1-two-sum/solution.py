from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store number:index pairs
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement exists in hash map, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found (though problem guarantees a solution exists)
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2] 