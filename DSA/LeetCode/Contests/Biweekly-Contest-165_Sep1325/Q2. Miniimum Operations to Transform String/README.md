# Find N Unique Integers Sum up to Zero

## INFO

**Index**: 3675

**Level**: Medium

**Link**: [Q2-Weekly-Contest-466](https://leetcode.com/problems/minimum-operations-to-transform-string/description/)

---

## DESCRIPTION

You are given a string s consisting only of lowercase English letters.

You can perform the following operation any number of times (including zero):

Choose any character c in the string and replace every occurrence of c with the next lowercase letter in the English alphabet.

Return the minimum number of operations required to transform s into a string consisting of only 'a' characters.

Note: Consider the alphabet as circular, thus 'a' comes after 'z'.

## EXAMPLE
### Example 1:

    Input: s = "yz"

    Output: 2

    Explanation:

    Change 'y' to 'z' to get "zz".
    Change 'z' to 'a' to get "aa".
    Thus, the answer is 2.

### Example 2:

    Input: s = "a"

    Output: 0

    Explanation:

    The string "a" only consists of 'a'​​​​​​​ characters. Thus, the answer is 0.

---

## CONTRAINTS

- 1 <= s.length <= 5 * 10^5
- s consists only of lowercase English letters.