
"""
Question 3: Kth Smallest Element in an Array
Topic: Arrays
DSA Sheet: Love Babbar 450 DSA Questions
Platform: GeeksforGeeks
Language: Python

Problem Statement:
Given an unsorted array of integers and an integer k,
find the kth smallest element in the array.

Example 1:
Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7

Example 2:
Input: arr = [7, 10, 4, 3, 20, 15], k = 4
Output: 10

Approach:
Randomized QuickSelect Algorithm

1. Select a random pivot element.
2. Partition the array around the pivot.
3. Compare the pivot's final index with k - 1.
4. Continue searching in the required partition.
5. Return the kth smallest element.

Time Complexity:
Expected: O(n)
Worst Case: O(n^2)

Auxiliary Space: O(1)

Note: The algorithm modifies the input array.

Problem Reference:
https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/
"""

import random


class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    def kthSmallest(self, arr, k):
        if k < 1 or k > len(arr):
            return -1

        low = 0
        high = len(arr) - 1
        target = k - 1

        while low <= high:
            # Choose a random pivot
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

            # Partition the array
            pos = self.partition(arr, low, high)

            if pos == target:
                return arr[pos]
            elif pos > target:
                high = pos - 1
            else:
                low = pos + 1

        return -1


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    obj = Solution()
    print("Kth Smallest Element:", obj.kthSmallest(arr, k))
