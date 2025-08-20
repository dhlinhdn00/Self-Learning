# Set Matrix Zeroes

## INFO

**Index**: 73

**Level**: Medium

**Link**: [Daily Question 2025-05-21](https://leetcode.com/problems/set-matrix-zeroes/?envType=daily-question&envId=2025-05-21)

---

## DESCRIPTION

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0's`.

You must do it **in place**.

## EXAMPLE

### Example 1:

<p align="center">
    <img src="./mat1.jpg" alt="example-1" />
</p>

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

### Example 2:

<p align="center">
    <img src="./mat2.jpg" alt="example-2" />
</p>

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

---

## CONTRAINTS

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-231 <= matrix[i][j] <= 231 - 1`
