# High level
"""
Feels as if there will be a way to even avoid O(26) space.

Only want to get one letter from the inputs.
Everything about the input can be discared, except one letter.
A number can become 0 by using XOR on itself. num ^ num

Since A & B have same letters except one, XOR of ALL letters will discard all letters except the extra letter
"""


# Algorithm / Pseudo:
"""
Iterate A letters:
    XOR all of them

Iterate B letters:
    XOR all of them

return combined XOR as this will be the unique letter left.
"""


# Time complexity: O(N)
"""
Iterate input A + Iterate input B
O(2N) = O(N)
"""


# Space Complexity: O(1)
"""
Only storing result of XOR
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_extra_letter_result = 0

        for c in s:
            xor_extra_letter_result ^= ord(c)
        
        for c in t:
            xor_extra_letter_result ^= ord(c)
        
        return chr(xor_extra_letter_result)