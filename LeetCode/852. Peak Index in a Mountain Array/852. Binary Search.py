"""
- Input:
int array with height numbers
peak index can't be at the beginning or end
peak index means 0 index to peak index is increasing
peak index means peak index + 1 to end of arr is decreasing

- Output:
index of peak

- General cases:
Peak on the left [1, 99, 5, 4, 3]
Peak on the right [1, 2, 3, 99, 5]
Peak in the middle [1, 2, 99, 4, 3]

- Edge cases:
if len == 3, then return 1
Value negative? (Constraints says: ALL positive)
arr without peak index? (Constraint says: GUARANTEED to exist)

- High level:
Constraint: O(log n) time complexity -> Asking to use binary search.

How to think of the problem using binary search frame?...
How to cut problem length in half?
Given a random index, how can I say peak will be in the right or left of the index?
What does peak index mean? It seems to mean MAX value of the arr
Left of peak is in increasing sorted order.
Right of peak is in decreasing sorted order.

So check the sorting order of the left/right half section of the binary search mid pointer.
If in increasing section, peak is to the right. Move L to mid.
If in decreasing section, peak is to the left. Move R to mid.
How to know whether the middle index is in increasing or decreasing section?
Compare mid to neighboring value

- Algorithm:
Just a typical binary search with condition adjustments.
Also can have the search range N - 2 as peak not at the end of array.

Condition: 
If arr[mid] > arr[mid + 1] then in decreasing section.
Move R to mid.
Else
Move L to mid + 1.

When L == R, it will be at the peak index as the search range kept getting halved when:
Increasing section meant at left side of the peak, so the LEFT half of the search range got deleted.
Decreasing section meant at right side of the peak, so the RIGHT half of the search range got deleted.

No need to check for out of bound error when making comparisons as constraint takes care of this edge case.
The middle index will always have neighboring values as peak index not at the end of the array and len >= 3.

- Complexity:
Time: O(log n)
Space: O(1)
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 3:
            return 1

        l, r = 1, len(arr) - 2

        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return l