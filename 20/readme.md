# Valid Parenthese

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

    Input: s = "()"

    Output: true

Example 2:

    Input: s = "()[]{}"

    Output: true

Example 3:

    Input: s = "(]"

    Output: false

Example 4:

    Input: s = "([])"

    Output: true

Example 5:

    Input: s = "([)]"

    Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

# Explanation

### Type of Problem: `stack`, `string`

#### How to solve it

- Add the opening bracket to the stack.
- If you encounter a closing bracket, check whether the top element of the stack is the corresponding opening bracket of the same type.
- Return True or False based on the behavior of the stack.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Solution

```Python
match = {')': '(', '}': '{', ']': '['}
stack = []
for l in s:
    if l in match.values():
        stack.append(l)
    elif l in match:
        if not stack or stack[-1] != match[l]:
            return False
        stack.pop()
    else:
        return False
return not stack
```
