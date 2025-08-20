# Build Array from Permutation
## INFO

**Index**: 1920

**Level**: Easy

**Link**: [Daily Question 2025-05-06](https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-06)

---

## DESCRIPTION

Given a **zero-based permutation** nums **(0-indexed)**, build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 $\leq$ i $\leq$ nums.length and return it.

A **zero-based permutation** nums is an array of **distinct** integers from 0 to nums.length - 1 **(inclusive)**.

## EXAMPLE
### Example 1:
    
    Input: nums = [0,2,1,5,3,4]
    Output: [0,1,2,4,5,3]
    Explanation: The array ans is built as follows: 
    ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
        = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
        = [0,1,2,4,5,3]

### Example 2:

    Input: nums = [5,0,1,2,3,4]
    Output: [4,5,0,1,2,3]
    Explanation: The array ans is built as follows:
    ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
        = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
        = [4,5,0,1,2,3]

---

## CONTRAINTS

- 1 $\leq$ nums.length $\leq$ 1000
- 0 $\leq$ nums[i] $\leq$ nums.length
- The elements in nums are **distinct**