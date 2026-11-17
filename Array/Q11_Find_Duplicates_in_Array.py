
"""
Question 11: Find Duplicates in an Array
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array arr[] containing non-negative
integers, find all elements that appear more
than once in the array.

Return the duplicate elements in ascending order.

Examples:

Example 1:
Input: arr = [2, 3, 1, 2, 3]
Output: [2, 3]

Explanation:
Elements 2 and 3 appear twice.

Example 2:
Input: arr = [1, 2, 3, 4]
Output: []

Explanation:
No element appears more than once.

Example 3:
Input: arr = [0, 1, 2, 0, 0, 2]
Output: [0, 2]

Explanation:
Element 0 appears three times,
and element 2 appears twice.

Approach: Frequency Array

1. Find the length n of the input array.
2. Create a frequency array initialized with zeros.
3. Traverse the input array and count occurrences.
4. Traverse the frequency array.
5. Add elements with frequency greater than 1
   to the result list.
6. Return the duplicate elements.

Assumption:
All array values lie between 0 and n.

Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def findDuplicates(self, arr):
        n = len(arr)

        # Initialize frequency array
        freq = [0] * (n + 1)

        # Store duplicate elements
        ans = []

        # Count occurrences of each element
        for num in arr:
            freq[num] += 1

        # Find elements appearing more than once
        for i in range(n + 1):
            if freq[i] > 1:
                ans.append(i)

        return ans
