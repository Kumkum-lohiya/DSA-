
"""
Question 1: Reverse an Array
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array of integers, reverse the order of its
elements and return the reversed array.

Example 1:
Input:  arr = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Example 2:
Input:  arr = [10, 20, 30, 40]
Output: [40, 30, 20, 10]

Constraints:
- The array may contain positive, negative, or zero values.
- The array may be empty or contain a single element.

Goal:
Implement a function to reverse the array.

Time Complexity: To be analyzed after implementation.
Space Complexity: To be analyzed after implementation.

Problem Reference:
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
"""


 "Solution"
class Solution:
    def reverseString(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
