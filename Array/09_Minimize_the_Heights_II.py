
"""
Question 9: Minimize the Heights II
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array arr[] representing the heights
of N towers and a positive integer k.

For each tower, you must perform exactly one
of the following operations:
1. Increase its height by k.
2. Decrease its height by k.

The final height of every tower must be
non-negative.

Find the minimum possible difference between
the maximum and minimum tower heights after
modification.

Examples:

Example 1:
Input:
arr = [1, 5, 8, 10]
k = 2

Output:
5

Explanation:
Modified heights can be [3, 3, 6, 8].
Difference = 8 - 3 = 5.

Example 2:
Input:
arr = [3, 9, 12, 16, 20]
k = 3

Output:
11

Explanation:
Modified heights can be [6, 12, 15, 13, 17].
Difference = 17 - 6 = 11.

Approach: Sorting + Greedy

1. Sort the array in ascending order.
2. Initialize the result with the difference
   between the largest and smallest heights.
3. Consider each possible split position:
   - Increase elements before the split by k.
   - Decrease elements from the split onward by k.
4. Skip a split if decreasing the first
   element of its right partition gives
   a negative height.
5. Calculate the minimum and maximum heights.
6. Update the minimum difference.
7. Return the final result.

Time Complexity: O(n log n)
Auxiliary Space: O(n) worst case in Python,
depending on sorting implementation.
"""


class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)

        # Sort tower heights
        arr.sort()

        # Initial difference
        res = arr[n - 1] - arr[0]

        # Check all possible split positions
        for i in range(1, n):

            # Tower height cannot become negative
            if arr[i] - k < 0:
                continue

            # Minimum possible height
            minH = min(arr[0] + k, arr[i] - k)

            # Maximum possible height
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)

            # Update minimum difference
            res = min(res, maxH - minH)

        return res
