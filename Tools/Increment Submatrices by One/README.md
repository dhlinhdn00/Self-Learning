# Increment Submatrices by One

## INFO

**Index**: 2536

**Level**: Medium

**Link**: [Daily Question 2025-11-14](https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14)

---

## DESCRIPTION

You are given a positive integer n , indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query . For each query[i] = [row1 i , col1 i , row2 i , col2 i ] , you should do the following operation:

- Add 1 to every element in the submatrix with the top left corner (row1 i , col1 i ) and the bottom right corner (row2 i , col2 i ) . That is, add 1 to mat[x][y] for all row1 i <= x <= row2 i and col1 i <= y <= col2 i .

Return the matrix mat after performing every query.

## EXAMPLE

### Example 1

    Input:
    n = 3, queries = [[1,1,2,2],[0,0,1,1]]
    Output:
    [[1,1,0],[1,2,1],[0,1,1]]
    Explanation:
    The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
    - In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
    - In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

### Example 2

    Input:
    n = 2, queries = [[0,0,1,1]]
    Output:
    [[1,1],[1,1]]
    Explanation:
    The diagram above shows the initial matrix and the matrix after the first query.
    - In the first query we add 1 to every element in the matrix.

---

## CONTRAINTS

- 1 <= n <= 500
- 1 <= queries.length <= 10^4
- 0 <= row1 i <= row2 i < n
- 0 <= col1 i <= col2 i < n
