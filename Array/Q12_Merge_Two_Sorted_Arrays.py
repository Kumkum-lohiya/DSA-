
"""
Question 12: Merge Two Sorted Arrays Without Extra Space
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given two sorted arrays a[] and b[] of sizes
n and m respectively, merge them in sorted
order without using an extra array.

After merging:
- Array a[] should contain the first n
  smallest elements.
- Array b[] should contain the remaining
  m largest elements.
- Both arrays must remain sorted.

Examples:

Example 1:
Input:
a = [1, 3, 5, 7]
b = [0, 2, 6, 8, 9]

Output:
a = [0, 1, 2, 3]
b = [5, 6, 7, 8, 9]

Example 2:
Input:
a = [10, 12]
b = [5, 18, 20]

Output:
a = [5, 10]
b = [12, 18, 20]

Approach: Two Pointers + Swapping + Sorting

1. Initialize pointer i at the last index of a.
2. Initialize pointer j at the first index of b.
3. Compare a[i] and b[j].
4. If a[i] is smaller, move i backward.
5. Otherwise, swap a[i] and b[j].
6. Move both pointers after swapping.
7. Sort both arrays individually.
8. The arrays are modified in-place.

Time Complexity:
O(n log n + m log m + min(n, m))

Auxiliary Space:
No extra array is created.
Python's built-in sorting may use O(n + m)
additional memory in the worst case.
"""


class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)

        # Initialize two pointers
        i = n - 1
        j = 0

        # Compare elements from both arrays
        while i >= 0 and j < m:

            if a[i] < b[j]:
                i -= 1

            else:
                # Swap misplaced elements
                a[i], b[j] = b[j], a[i]

                i -= 1
                j += 1

        # Sort both arrays after swapping
        a.sort()
        b.sort()
