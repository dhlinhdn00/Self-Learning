# Shifting Letters II

## Info
**Index**: 2381

**Link**: https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05

---

## Problem Description

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [starti, endi, directioni]`. For every `i`, shift the characters in `s` from the index `starti` to the index `endi` (inclusive):
- **Forward** if `directioni = 1`, or
- **Backward** if `directioni = 0`.

### Shifting Rules
- **Forward Shifting**: Replacing a character with the next letter in the alphabet (wrapping around so that `'z'` becomes `'a'`).
- **Backward Shifting**: Replacing a character with the previous letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return the final string after all such shifts to `s` are applied.

---

### Example 1
**Input**:
s = "abc" shifts = [[0,1,0],[1,2,1],[0,2,1]]

**Output**:
"ace"

**Explanation**:
1. Shift the characters from index `0` to `1` backward.  
   Result: `"zac"`
2. Shift the characters from index `1` to `2` forward.  
   Result: `"zbd"`
3. Shift the characters from index `0` to `2` forward.  
   Result: `"ace"`

---

### Example 2
**Input**:
s = "dztz" shifts = [[0,0,0],[1,1,1]]

**Output**:
"catz"

**Explanation**:
1. Shift the characters from index `0` to `0` backward.  
   Result: `"cztz"`
2. Shift the characters from index `1` to `1` forward.  
   Result: `"catz"`

---

## Constraints
- \(1 \leq s.\text{length}, \text{shifts}.\text{length} \leq 5 \times 10^4\)
- \(\text{shifts}[i].\text{length} == 3\)
- \(0 \leq \text{start}_i \leq \text{end}_i < s.\text{length}\)
- \(0 \leq \text{direction}_i \leq 1\)
- \(s\) consists of lowercase English letters.