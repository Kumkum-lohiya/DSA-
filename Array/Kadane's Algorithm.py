
"""
Question 8: Maximum Subarray Sum (Kadane's Algorithm)
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array of integers, find the maximum
possible sum of a contiguous subarray.

A contiguous subarray consists of consecutive
elements from the original array.

Examples:

Example 1:
Input: arr = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation:
The subarray [7, -1, 2, 3] has the maximum
sum of 11.

Example 2:
Input: arr = [-2, -4, -1, -5]
Output: -1
Explanation:
The maximum sum is obtained from [-1].

Example 3:
Input: arr = [5, 4, 1, 7, 8]
Output: 25
Explanation:
The entire array has the maximum sum.

Approach: Kadane's Algorithm

1. Initialize res and max_ending with arr[0].
2. Traverse the array from the second element.
3. For each element, decide whether to:
   - Extend the previous subarray.
   - Start a new subarray from the current element.
4. Update res with the maximum sum found so far.
5. Return res.

Time Complexity: O(n)
Auxiliary Space: O(1)

Note:
This solution also handles arrays containing
only negative elements.
"""


class Solution:
    def maxSubarraySum(self, arr):
        # Initialize maximum sum
        res = arr[0]

        # Maximum subarray sum ending at current index
        max_ending = arr[0]

        # Traverse the array from the second element
        for i in range(1, len(arr)):

            # Extend previous subarray or start a new one
            max_ending = max(max_ending + arr[i], arr[i])

            # Update the overall maximum sum
            res = max(max_ending, res)

        return res
