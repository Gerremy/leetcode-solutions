class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Dictionary mapping closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        # Stack to keep track of opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop from stack if not empty, else use dummy char
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the correct opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push onto stack
                stack.append(char)

        # In the end, the stack should be empty if all brackets matched
        return not stack
