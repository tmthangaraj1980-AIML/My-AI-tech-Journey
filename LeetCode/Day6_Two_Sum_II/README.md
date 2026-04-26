# Day 6 - LeetCode 167: Two Sum II

## 📌 Problem
Given a sorted array of integers, return indices of two numbers such that they add up to a target.

---

## 🧠 Approach: Two Pointers

Since the array is sorted:

- If sum == target → return indices
- If sum > target → move right pointer left
- If sum < target → move left pointer right

---

## 💻 Implementation

### 🔹 LeetCode Submission Version
```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l= 0
        r = len(numbers) - 1

        while left < right:
            two_sum = numbers[l] + numbers[r]

            if two_sum == target:
                return [l + 1, r + 1]
            elif two_sum > target:
                r -= 1
            else:
                l += 1

        
