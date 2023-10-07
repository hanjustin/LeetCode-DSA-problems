# Input:
"""
Two strings A & B.
A & B both have same letters except B has one extra letter.
A & B letters may or may not shuffled.
"""


# Output:
"""
One string letter. This letter only present in the longer input.
"""


# General cases & example I/O:
"""
Original letter orders + one extra char at the beginning or end
abc & abcd -> d
abc & dabc -> d

Shuffled
abc & cbad -> d
abc & cbda -> d
"""


# Edge cases:
"""
All same letters
ddd & dddd -> d

Q: Empty string possible?
A: Yes
Then this could be a base case. If one input is empty, return other

Q: Any special characters?
A: No. Only lowercase letters.

Q: Guaranteed only one letter difference?
A: Yes
"""


# High level
"""
Sorting -> Two pointers to find extra char
Frequency counting using hashmap.

Use 26 size array. Find char with extra frequency.
"""


# Algorithm / Pseudo:
"""
letterFreq

Iterate A
    increment letterFreq by one for each letter

Iterate B
    if count == 0 for letter
        Return this letter
    decrement letterFreq by one for each letter
"""


# Time complexity: O(N)
"""
Iterating input A + Iterating input B
O(2N) = O(N)
"""


# Space Complexity: O(1)
"""
There are only 26 letters. Size of frequency array is always 26.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original_letters = set(s)
        for c in t:
            if c not in original_letters:
                return c