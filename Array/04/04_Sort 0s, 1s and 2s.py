
"""
Question 4: Sort an Array of 0s, 1s and 2s
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array containing only 0s, 1s and 2s,
sort the array in ascending order without using
any built-in sorting function.

Example 1:
Input:  arr = [0, 2, 1, 2, 0]
Output: [0, 0, 1, 2, 2]

Example 2:
Input:  arr = [2, 2, 1, 0, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Approach: Counting Method

Time Complexity: O(n)
Auxiliary Space: O(1)

Problem Reference:
https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
"""


class Solution:
    def sort012(self, arr):
        c0 = 0
        c1 = 0
        c2 = 0

        # Count occurrences of 0, 1 and 2
        for num in arr:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        idx = 0

        # Place all zeros
        for i in range(c0):
            arr[idx] = 0
            idx += 1

        # Place all ones
        for i in range(c1):
            arr[idx] = 1
            idx += 1

        # Place all twos
        for i in range(c2):
            arr[idx] = 2
            idx += 1

        return arr
