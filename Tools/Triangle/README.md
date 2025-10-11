# Triangle

## INFO

**Index**: 120

**Level**: Medium

**Link**: [Daily Question 2025-09-25](https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25)

---

## DESCRIPTION

Given a triangle array, return the minimum path sum from top to bottom .

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

## EXAMPLE

### Example 1

    Input:
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output:
    11

### Example 2

    Input:
    triangle = [[-10]]
    Output:
    -10

---

## CONTRAINTS

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4
