# Input:
"""
String only consisting '(' or ')'
"""

# Output:
"""
Count number of parenthesis needed to make string VALID.
"""

# General cases & example I/O:
"""
valid string. ()
invalid string. (()

Input: ((), Output: 1
Input: )()(, Output: 2
"""

# Edge cases:
"""
Empty string (Constraint says: len >= 1)
All open or all close. ((((((
"""

# High level:
"""
What does VALID string mean?
Equal # of open & close parenthesis
AND
there is open before each close. Meaning: ))(( is invalid although has the same count.

To change from invalid to valid:
If a ) is seen before (, need to add (
After (, there needs to be ). If ( does not have ), need to add )
"""

# Algorithm:
"""
Iterate from left to right.
Keep `open` variable for count of (
If ( is seen, `open` += 1.
If ) is seen, `open` -= 1. But if `open` = 0, `total_move` += 1
At the end of the input iteration, add remaining open count. `total_move` += `open`
"""

# Complexity:
"""
Time: O(n), iterating input
Space: O(1), just using variables for pointers and to hold count
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        remaining_open_count = total_move = 0

        for parenthesis in s:
            if parenthesis == "(":
                remaining_open_count += 1
            else:
                if remaining_open_count == 0:
                    total_move += 1
                else:
                    remaining_open_count -= 1
        
        return total_move + remaining_open_count