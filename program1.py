class Solution(object):
    def isValid(self, s):
        # Dictionary to map closing brackets to corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop from stack if not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element is the correct opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)
        
        # Check if the stack is empty
        return not stack