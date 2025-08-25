# Count Square Submatrices with All Ones

## INFO

**Index**: 498

**Level**: Medium

**Link**: [Daily Question 2025-08-25](https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25)

---

## DESCRIPTION

Given an `m x n` matrix `mat`, return _an array of all the elements of the array in a diagonal order._


 

## EXAMPLE

### Example 1:

    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]

### Example 2:

    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]

---

## CONTRAINTS

- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- -10^5 <= mat[i][j] <= 10^5