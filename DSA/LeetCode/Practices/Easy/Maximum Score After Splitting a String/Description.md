# Maximum Score After Splitting a String

## Info
Index: 1422

Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01

## Problem Description
Given a string `s` of zeros and ones, the goal is to return the maximum score after splitting the string into two non-empty substrings (i.e., left substring and right substring).

The score after splitting a string is calculated as:
- The number of zeros (`0`) in the left substring.
- Plus the number of ones (`1`) in the right substring.

### Example 1

**Input:**
```
s = "011101"
```

**Output:**
```
5
```

**Explanation:**
All possible ways of splitting `s` into two non-empty substrings are:
- `left = "0"`, `right = "11101"`, score = `1 + 4 = 5`
- `left = "01"`, `right = "1101"`, score = `1 + 3 = 4`
- `left = "011"`, `right = "101"`, score = `1 + 2 = 3`
- `left = "0111"`, `right = "01"`, score = `1 + 1 = 2`
- `left = "01110"`, `right = "1"`, score = `2 + 1 = 3`

### Example 2

**Input:**
```
s = "00111"
```

**Output:**
```
5
```

**Explanation:**
When `left = "00"` and `right = "111"`, we get the maximum score `2 + 3 = 5`.

### Example 3

**Input:**
```
s = "1111"
```

**Output:**
```
3
```

## Constraints

- `2 <= s.length <= 500`
- The string `s` consists of characters `'0'` and `'1'` only.