# Input:
"""
str with digits and period.
Assume string only has digits and periods.
"""

# Output:
"""
str that is modified version of the input.
same as input string except "." gets replaced by "[.]"
"""

# General cases & example I/O:
"""
Period in between numbers.
Numbers value seem to be from 0 to 255
Numbers length can be from 1 to 3

0.0.0.0 -> 0[.]0[.]0[.]0
255.10.255.0 -> 255[.]10[.]255[.]0
"""

# Edge cases:
"""
Question: Can input be "0000" or "...."?
(Constraint says: Input is valid ip. So assume this means starts & ends with digit and period in between digits)
"""

# High level:
"""
All "." need to become "[.]", so find "." and replace them.
Everything else including the relative position needs to stay the same.
"""

# Algorithm:
"""
Each time splitting or concatenating strings for seeing a period creates new string in Python so this will be O(N) operation.

So like a String Builder, will create array to store output characters and combine them at the end.
O(1) while traversing & storing components.
O(N) operation at the end for combining.

Iterate left to right checking if current character is a period or not.
If it is a period add "[.]" to the array.
If it is a number, add the number to the array.
Join the array to create the output & return it
"""

# Complexity:
"""
Time: O(N) for iterating the input & combining the components
Space: O(N) for storing the string components and for the output string
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_components = []
        
        for char in address:
            component = char if char.isdigit() else "[.]"
            ip_components.append(component)

        return "".join(ip_components)