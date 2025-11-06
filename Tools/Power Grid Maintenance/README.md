# Power Grid Maintenance

## INFO

**Index**: 3607

**Level**: Medium

**Link**: [Daily Question 2025-11-06](https://leetcode.com/problems/power-grid-maintenance/?envType=daily-question&envId=2025-11-06)

---

## DESCRIPTION

You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections , where each element connections[i] = [u i , v i ] indicates a connection between station u i and station v i . Stations that are directly or indirectly connected form a power grid .

Initially, all stations are online (operational).

You are also given a 2D array queries , where each query is one of the following two types:

- [1, x] : A maintenance check is requested for station x . If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x . If no operational station exists in that grid, return -1.

- [2, x] : Station x goes offline (i.e., it becomes non-operational).

[1, x] : A maintenance check is requested for station x . If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x . If no operational station exists in that grid, return -1.

[2, x] : Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

## EXAMPLE

### Example 1

    Input:
    c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
    Output:
    [3,2,3]

### Example 2

    Input:
    c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]
    Output:
    [1,-1]

---

## CONTRAINTS

- 1 <= c <= 10^5
- 0 <= n == connections.length <= min(10^5 , c \* (c - 1) / 2)
- connections[i].length == 2
- 1 <= u i , v i <= c
- u i != v i
- 1 <= queries.length <= 2 \* 10^5
- queries[i].length == 2
- queries[i][0] is either 1 or 2.
- 1 <= queries[i][1] <= c
