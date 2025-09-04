# Valid Word

## INFO

**Index**: 3136

**Level**: Easy

**Link**: [Daily Question 2025-07-15](https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15)

---

## DESCRIPTION

A word is considered valid if:

- it contains a minimum of 3 characters

- it contains only digits (0-9) and English letters (uppercase and lowercase)

- it includes at least one vowel

- it includes at least one consonant

You are given a string `word`

Return `true` if `word` is valid, otherwise, return `false`

## EXAMPLE
### Example 1:

    Input: word = "234Adas"
    Output: true
    Explanation: This word satisfies the conditions.

### Example 2:

    Input: word = "b3"
    Output: false
    Explanation: The length of this word is fewer than 3, and does not have a vowel.

### Example 3:

    Input: word = "a3$e"
    Ouput: false
    Explanation: This word contains a '$' character and does not have a consonant.

---

## CONTRAINTS

- `1 <= word.length <= 20`
- `word` consists of English uppercase and lowercase letters, digits, `'@'`, `'#'`, and `'$'`.