# Name 8. String to Integer (atoi)

## Difficulty - Medium

**Link** to the problem -> https://leetcode.com/problems/string-to-integer-atoi/description/

# Solution

```
Space complexity - O(1) ; Time complexity - O(n) + additional overhead with strip() and s = s[1:]

1. Remove whitespace with strip()
2. Read + or - if first character
3. Iterate over the string and check if character is numeric. If so then break
4. If digit then use res = res * 10 + digit. Which handles leading zeros and reads a correct number each time
5. Check if boundaries were hit
```


