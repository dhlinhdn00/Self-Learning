# Number of Zero-Filled Subarrays

## INFO

**Index**: 2348

**Level**: Medium

**Link**: [Daily Question 2025-07-16](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/?envType=daily-question&envId=2025-07-16)

---

## DESCRIPTION

Given an integer array `nums`, return the number of _**subarrays** filled with 0_.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## EXAMPLE

### Example 1:

    Input: nums = [1,3,0,0,2,0,0,4]

    Output: 6

    Explanation: 

    There are 4 occurrences of [0] as a subarray.
    There are 2 occurrences of [0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.


### Example 2:

    Input: nums = [0,0,0,2,0,0]

    Output: 9

    Explanation:

    There are 5 occurrences of [0] as a subarray.
    There are 3 occurrences of [0,0] as a subarray.
    There is 1 occurrence of [0,0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

### Example 3:

    Input: nums = [2,10,2019]

    Output: 0

    Explanation: There is no subarray filled with 0. Therefore, we return 0.

---

## CONTRAINTS

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`