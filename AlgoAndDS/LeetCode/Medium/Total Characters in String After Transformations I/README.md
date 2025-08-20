# Total Characters in String After Transformations I

## INFO

**Index**: 3335

**Level**: Medium

**Link**: [Daily Question 2025-05-13](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13)

---

## DESCRIPTION

You are given a string `s` and an integer `t`, representing the number of **transformations** to perform. In one **transformation**, every character in `s` is replaced according to the following rules:

- If the character `"z"`, replace it with the string `"ab"`.
- Otherwise, replace it with the **next** character in the alphabet. For example, `'a'` is replaced with `'b'`. `'b'` is replaced with `'c'`, and so on.

Return the **length** of the resulting string also **exactly** `t` transformations.

Since the answer may be very large, reutrun it **modulo** $10^9 + 7$.

## EXAMPLE
### Example 1:

    Input: s = "abcyy", t = 2
    
    Output: 7

    Explanation:
    
    - First Transformation (t=1):
        - 'a' becomes 'b'
        - 'b' becomes 'c'
        - 'c' becomes 'd'
        - 'y' becomes 'z'
        - 'y' becomes 'z'
        - String after the first transformation: "bcdzz"
    - Second Transformation (t=2):
        - 'b' becomes 'c'
        - 'c' becomes 'd'
        - 'd' becomes 'e'
        - 'z' becomes 'ab'
        - 'z' becomes 'ab'
        - String after the second transformation: "cdeabab"
    - Final Length of the String: the string is "cdeabab", which has 7 characters.

### Example 2:

    Input: s = "azbk", t = 1
    
    Output: 5

    Explanation:
    
    - First Transformation (t=1):
        - 'a' becomes 'b'
        - 'z' becomes 'ab'
        - 'b' becomes 'c'
        - 'k' becomes 'l'
        - String after the first transformation: "babcl"
    - Final Length of the string: The string is "babcl", which has 5 characters.


---

## CONTRAINTS

- $1 \leq$ `s.length` $\leq 10^5$
- `s` consists only of lowercase English letters.
- $1 \leq$ t $\leq 10^5$