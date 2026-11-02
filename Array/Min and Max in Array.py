
"""
Question 2: Find Maximum and Minimum Element in an Array
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array of integers, find the maximum and
minimum elements present in the array.

Example 1:
Input:  arr = [3, 5, 4, 1, 9]
Output: Minimum = 1, Maximum = 9

Example 2:
Input:  arr = [-10, 20, 0, 15, -5]
Output: Minimum = -10, Maximum = 20

Example 3:
Input:  arr = [7]
Output: Minimum = 7, Maximum = 7

Constraints:
- The array contains at least one element.
- Elements can be positive, negative, or zero.
- Duplicate elements are allowed.

Goal:
Find and return both the minimum and maximum
elements of the given array.

Time Complexity: To be analyzed after implementation.
Space Complexity: To be analyzed after implementation.

Problem Reference:
https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
"""

"Solution"

class Solution:
    def getMinMax(self, arr):
        MIN = arr[0]
        MAX = arr[0]
        
        for i in arr:
            if i < MIN:
                MIN = i
            
            if i > MAX:
                MAX = i
            
            
        return [MIN,MAX]
                
        
