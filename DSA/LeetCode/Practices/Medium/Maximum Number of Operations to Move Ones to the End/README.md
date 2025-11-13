# Maximum Number of Operations to Move Ones to the End

## INFO

**Index**: 3228

**Level**: Medium

**Link**: [Daily Question 2025-11-13](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13)

---

## DESCRIPTION

You are given a binary string s .

You can perform the following operation on the string any number of times:

- Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0' .

- Move the character s[i] to the right until it reaches the end of the string or another '1' . For example, for s = "010010" , if we choose i = 1 , the resulting string will be s = "0 001 10" .

Return the maximum number of operations that you can perform.

## EXAMPLE

### Example 1

    Input:
    s = "1001101"
    Output:
    4

### Example 2

    Input:
    s = "00111"
    Output:
    0

---

## CONTRAINTS

- 1 <= s.length <= 10^5
- s[i] is either '0' or '1' .
