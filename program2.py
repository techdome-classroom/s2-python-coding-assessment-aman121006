class Solution(object):
    def romanToInt(self, s):
        # Dictionary to map Roman numerals to integers
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # Variable to store the integer result
        result = 0
        
        # Traverse through the string
        for i in range(len(s)):
            # If the current numeral is less than the next numeral, subtract its value
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                # Otherwise, add its value
                result += roman_map[s[i]]
        
        return result