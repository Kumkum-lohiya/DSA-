
"""
Question 6: Union of Two Arrays
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given two arrays a[] and b[], find their union.

The union contains all distinct elements present
in either array, without any duplicates.

Return the result in sorted ascending order.

Example 1:
Input:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

Output:
[1, 2, 3, 4, 5, 6]

Example 2:
Input:
a = [1, 1, 2, 3]
b = [2, 2, 4, 5]

Output:
[1, 2, 3, 4, 5]

Approach: Set Union

1. Convert both arrays into sets to remove duplicates.
2. Use the union operator (|) to combine both sets.
3. Sort the unique elements in ascending order.
4. Return the sorted list.

Time Complexity:
O(n + m + u log u) expected

Space Complexity:
O(n + m)

Where:
n = Length of first array
m = Length of second array
u = Number of unique elements
"""


class Solution:
    def findUnion(self, a, b):
        # Convert arrays into sets
        a = set(a)
        b = set(b)

        # Combine unique elements from both sets
        arr = a | b

        # Return the sorted union
        return sorted(arr)



OR



class Solution:
    def findUnion(self, a, b):
        unique = set()

        for num in a:
            unique.add(num)

        for num in b:
            unique.add(num)

        return sorted(unique)

