
"""
Question 7: Rotate Array by One
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array arr[], rotate the array by one
position in the clockwise direction.

The last element should move to the first
position, and all remaining elements should
shift one position to the right.

Example 1:
Input:  arr = [1, 2, 3, 4, 5]
Output: arr = [5, 1, 2, 3, 4]

Example 2:
Input:  arr = [9, 8, 7, 6, 4, 2, 1, 3]
Output: arr = [3, 9, 8, 7, 6, 4, 2, 1]

Approach: Two-Reversal Technique

Step 1:
Reverse the first n-1 elements of the array.

Step 2:
Reverse the entire array.

This moves the last element to the beginning
while preserving the order of other elements.

Time Complexity: O(n)
Auxiliary Space: O(1)

The original array is modified in-place.
"""


class Solution:
    def rotate(self, arr: list[int]) -> None:
        n = len(arr)

        # Step 1: Reverse the first n-1 elements
        left = 0
        right = n - 2

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        # Step 2: Reverse the entire array
        start = 0
        end = n - 1

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
