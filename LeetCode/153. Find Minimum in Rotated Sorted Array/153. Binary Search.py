# Input:
"""
int arr that is sorted and rotated.
values are UNIQUE.

Q: Can value be negative?
A: Yes
"""


# Output:
"""
one integer. Min val from the input arr
"""


# General cases & example I/O:
"""
* Min to the right
[3,4,5,6,7,8,9, 1,2] -> 1

* Min to the left
[6, 1,2,3,4,5] -> 1

* Some rotation
[2,3, 0,1] -> 0

* No rotation
[0,1,2,3] -> 0

* All positive
[6,7,10, 1,2,3,4] -> 1

* All negative
[-4,-3,-2, -100] -> -100

* Neg & Positive
[99, -10, -9, -8, 0, 1, 2] -> -10
"""


# Edge cases:
"""
Q: Empty arr? Return value?
A: At least one value
* So that means base case len == 1, return first element

Q: Can it have 0 rotation?
A: Y. n times rotation is same as 0 rotation.
* In this case, the first element is the output
"""


# High level:
"""
We want to find min, and doing linear search O(N) time will be trivial.
Use binary search to make time O(log N) by halving search space.
Each time need to decide to keep left or right.
Need to know min is to the left or to the right. How?

After rotation, arr becomes
[LEFT, MAX, MIN, RIGHT]

All values to the left of min are greater than the values to the right due to the original sorting.
Given random index, MID, if we know whether MID is at the left portion or right portion,
we can decide which side to discard.

To keep min in the search space,
If mid is at left side, discard left portion.
If mid is at right side, discard right portion.

How to know if mid is in left or right side?
Notice the left side is sorted from leftmost to Max inclusive.
Also same for the right side, Min to rightmost is sorted inclusive.
So if mid is in right, it will be smaller than rightmost element as values are all unique.
Continue to discard right & left until one element left, which will be the Min.
"""


# Algorithm/Pseudo:
"""
while l < r
    Base case:
    if len == 1 OR left < right (not in rotated array)
        return first element

    if mid in right (right val > mid val)
        discard right of mid
    else
        discard left of mid
"""


# Time complexity O(log N):
"""
Using binary search to cut search space half every time
"""


# Space complexity O(1):
"""
Only storing left & right for search space
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
 
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        return nums[l]