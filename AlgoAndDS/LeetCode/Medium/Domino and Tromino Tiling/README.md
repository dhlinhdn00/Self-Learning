# Domino and Tromino Tiling

## INFO

**Index**: 790

**Level**: Medium

**Link**: [Daily Question 2025-05-05](https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=daily-question&envId=2025-05-05)

---

## DESCRIPTION

You have two types of tiles: a 2×1 domino shape and a tromino shape. You may rotate these shapes.

<p align="center">
    <img src="./lc-domino.jpg" alt="description-1" />
</p>

Given an integer n, return *the number of ways to tile a 2×n board*. Since the answer may be very large, return it **modulo** $10^9 + 7$.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squres occupied by a tile.

## EXAMPLE
### Example 1:

<p align="center">
    <img src="./lc-domino1.jpg" alt="example-1" />
</p>
    
    Input: n = 3
    Output: 5
    Explanation: The five different ways are show above.

### Example 2:

    Input: n = 2 
    Output: 1

---

## CONTRAINTS

- 1 $\leq$ n $\leq$ 1000