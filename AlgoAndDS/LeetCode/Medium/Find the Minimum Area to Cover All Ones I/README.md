# Find the Minimum Area to Cover All Ones I

## INFO

**Index**: 3195

**Level**: Medium

**Link**: [Daily Question 2025-08-22](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22)

---

## DESCRIPTION

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

## EXAMPLE

### Example 1:

    Input: grid = [[0,1,0],[1,0,1]]

    Output: 6

    Explanation:

    The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.


### Example 2:

    Input: grid = [[1,0],[0,0]]

    Output: 1

    Explanation:

    The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

---

## CONTRAINTS

- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 0 or 1.
- The input is generated such that there is at least one 1 in grid.