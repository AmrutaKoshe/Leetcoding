'''
Counting Words with a Given Prefix - \

You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.

---------------------------------------------------------------------------------------------------------------------------------------------------------
APPROACH 1: Using startswith() 
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1

        return ans
    
'''
Time Complexity: For each word, startswith checks up to len(pref) characters.
O(m*n) - where m is length of pref, and n is the length of words

Space Complexity: O(1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------
APPROACH 2: Using Slicing
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        pref_len = len(pref)
        for word in words:
            if word[:pref_len] == pref:
                ans += 1
            
        return ans
    

'''
Time Complexity: O(m*n)
Space Complexity: O(1)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

APPROACH 3: Using filter
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(list(filter(lambda word: word.startswith(pref), words)))
    
'''
We're basically doing the same thing, but we're using the filter() function.

Syntax of filter: 
filter( function, iterable)

This will return a filter object, which contains the elements of the iterable for which the function returns true. Since filter returns an iterable, we have to convert it to a list.

Time Complexity: O(m*n)
Space Complexity: O(1)
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
APPROACH 4: Uisng Trie



'''




