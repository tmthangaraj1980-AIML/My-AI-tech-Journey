# Day 6 - LeetCode 167: Two Sum II

## Problem
Given a sorted array of integers, find two numbers such that they add up to a target value.

Return the indices of the two numbers using 1-based indexing.

## Example

Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]

## Approach: Two Pointers

Since the array is sorted:

- If current sum is equal to target, return the indices.
- If current sum is greater than target, move the right pointer left.
- If current sum is less than target, move the left pointer right.

## Python Code

```python
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        two_sum = numbers[left] + numbers[right]

        if two_sum == target:
            return [left + 1, right + 1]
        elif two_sum > target:
            right -= 1
        else:
            left += 1

    return []
