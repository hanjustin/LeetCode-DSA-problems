"""
- Input:
int array with height numbers

- Output:
index of peak
ANY of the peaks if there are multiple
peak can be ANY index including beginning & end as out of bound is considered -Inf

- Examples:
Input: [1, 5]
Output: 1. val 5 is greater than -Inf & 1

Input: [1, 10, 5, 20]
Output: 1 or 3. There are two peaks val 10 & 20.

- General cases:
1 peak
Multiple peaks

- Edge cases:
negative value height? (Constraint says: neg val possible)
If input is [1, 5, 5, 1], is multiple 5s considered as the same pick? Is pick index 1 or 2?
(Constraint says: value next to each other can't be the same. So this will be invalid input)
No peak case? Due to the constraint right & left values can't be equal, there ALWAYS will be a peak.
Peak at the begin/end of the arr

- High level:
Constraint: Time complexity O(log N) -> means binary search
How to reduce search range in half & determine to get rid of left or right?
Given a random index, how to determine whether peak is to the right or left?

Say val of mid index = X.
If R > X or L < X, what does this mean? Anything to say about range in between mid & R or L?
What does peak element mean?
Peak element = greater than left & right element.
arr[mid] could be a peak element or it is not a peak element.
If arr[mid] is not a peak element, it means left or right is is greater. That greater left or right element COULD be a peak element. Repeatedly, the greater element could check itself if it is a peak element by comparing values to left & right.
So if right element is greater than mid index, then this guarantees there is at least one peak as arr[mid] as even if the greatest element is at the end of the arr, due to the constraint out of bound being -Inf, the last element becomes the peak.
So for every binary search, keep section with the greater element and throw away the section with smaller element.

- Algorithms:

Binary search with condition to check if the mid index is a peak.
If there is an element that is greater, that means mid index is not a peak, so mid index can be discarded.
Keep the side with a greater element and discard the other side with smaller element.
The side with greater element guarantees there will be a peak due to values beside being UNIQUE & out of bound being -Inf as in the worst case if the right side is all sorted in ascending order, the last element will be a peak.

If right element is bigger, move the left pointer right to the mid index to discard the left section.
if nums[mid] < nums[mid + 1]
l = mid + 1

- Complexity:
Time: O(log n)
Space: O(1)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            
            # No need to check out of bound as out of bound can happen only if peak is the last element.
            # Which means mid index should be len(N) - 1, but for this to happen L & R needs to be equal
            # But the while loop terminates when L & R are equal
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l