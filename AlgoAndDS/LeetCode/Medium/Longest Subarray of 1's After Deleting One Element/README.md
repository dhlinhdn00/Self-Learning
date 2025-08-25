# Longest Subarray of 1's After Deleting One Element

## INFO

**Index**: 1493

**Level**: Medium

**Link**: [Daily Question 2025-08-24](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

---

## DESCRIPTION

Given a binary array `nums`, you should delete one element from it.

Return _the size of the longest non-empty subarray containing only 1's in the resulting array_. Return 0 if there is no such subarray.



 

## EXAMPLE

### Example 1:

    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


### Example 2:

    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

### Example 3:

    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element.

---

## CONTRAINTS

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.