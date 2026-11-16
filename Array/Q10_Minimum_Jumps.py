
"""
Question 10: Minimum Jumps to Reach End
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an array arr[] of non-negative integers,
where each element represents the maximum
number of steps that can be jumped forward
from that position.

Find the minimum number of jumps required
to reach the last index of the array.

Return -1 if the last index cannot be reached.

Examples:

Example 1:
Input: arr = [2, 3, 1, 1, 4]
Output: 2

Explanation:
Jump from index 0 to index 1,
then from index 1 to index 4.
Total jumps = 2.

Example 2:
Input: arr = [1, 1, 1, 1]
Output: 3

Example 3:
Input: arr = [3, 2, 1, 0, 4]
Output: -1

Explanation:
The last index cannot be reached.

Example 4:
Input: arr = [5]
Output: 0

Explanation:
Already at the last index.

Approach: Greedy Algorithm

1. Handle the single-element array case.
2. If the first element is zero, return -1.
3. Initialize:
   - count: Number of jumps taken.
   - maxReach: Farthest reachable index.
   - currEnd: End of the current jump range.
4. Traverse the array until the second-last index.
5. Update maxReach at each index.
6. When the current jump range ends:
   - Check if further progress is possible.
   - Increase the jump count.
   - Extend currEnd to maxReach.
7. Return the minimum number of jumps.

Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)

        # Already at the destination
        if n == 1:
            return 0

        # Cannot move from the starting position
        if arr[0] == 0:
            return -1

        count = 0
        i = 0
        maxReach = 0
        currEnd = 0

        while i < n - 1:

            # Update the farthest reachable index
            maxReach = max(maxReach, i + arr[i])

            # End of the current jump range
            if i == currEnd:

                # No further progress is possible
                if maxReach == currEnd:
                    return -1

                # Take another jump
                count += 1
                currEnd = maxReach

                # Destination is reachable
                if currEnd >= n - 1:
                    return count

            i += 1

        return count
