
"""
Question 1: Spiral Matrix Traversal
Topic: Matrix
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given a 2D matrix of size rows x cols,
return all elements of the matrix in spiral order.

Spiral traversal follows four directions:
1. Left to Right
2. Top to Bottom
3. Right to Left
4. Bottom to Top

Continue until all elements are visited.

Example 1:
Input:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:
Input:
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

Output:
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Approach: Four Boundary Pointers

1. Initialize top, bottom, left, and right.
2. Traverse the top row from left to right.
3. Traverse the right column from top to bottom.
4. Traverse the bottom row from right to left.
5. Traverse the left column from bottom to top.
6. Update boundaries after each traversal.
7. Repeat until all elements are visited.

Time Complexity: O(rows * cols)
Auxiliary Space: O(1)
Output Space: O(rows * cols)
"""


class Solution:
    def spirallyTraverse(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        # Initialize four boundaries
        top = 0
        left = 0
        bottom = rows - 1
        right = cols - 1

        ans = []

        while top <= bottom and left <= right:

            # 1. Traverse top row (Left to Right)
            for i in range(left, right + 1):
                ans.append(mat[top][i])

            top += 1

            # 2. Traverse right column (Top to Bottom)
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])

            right -= 1

            # 3. Traverse bottom row (Right to Left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])

                bottom -= 1

            # 4. Traverse left column (Bottom to Top)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])

                left += 1

        return ans
