
"""
Question 5: Move All Negatives to End
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an unsorted array containing positive and
negative integers, move all negative elements
to the end of the array.

Maintain the original relative order of both
non-negative and negative elements.

Modify the original array in-place.
Do not return a new array.

Example 1:
Input:  arr = [1, -1, 3, 2, -7, -5, 11, 6]
Output: [1, 3, 2, 11, 6, -1, -7, -5]

Example 2:
Input:  arr = [-5, 7, -3, -4, 9, 10, -1, 11]
Output: [7, 9, 10, 11, -5, -3, -4, -1]

Example 3:
Input:  arr = [5, -2, 0, 8, -3]
Output: [5, 0, 8, -2, -3]

Approach:
Stable Segregation using Two Lists

1. Traverse the given array.
2. Store non-negative elements in a positive list.
3. Store negative elements in a negative list.
4. Combine both lists while preserving their order.
5. Update the original array using slice assignment.

Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []

        # Separate non-negative and negative elements
        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        # Modify the original array without returning it
        arr[:] = positive + negative
