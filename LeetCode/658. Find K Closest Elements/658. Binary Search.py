"""
- Input:
Sorted int arr. (Numbers unique? Constraint doesn't say numbers are unique)
Neg & Positive int

- Output:
Partial array of input.
Order intact
Asks for k numbers. Didnt say k distinct numbers, so assume [1,1,1,1,1] is valid output.

- Cases:
x is in the middle of arr
x is at the end of arr
Multiple x in arr

- Edge case:
x is not in the arr
k larger than len of arr. (Constraint says: k is within array length)

- High level:
Find index of x or CLOSEST index in arr
Pick element to the right & left until k elements picked.

What index when duplicates or value not found?
Duplicates try using left most index.
For not found, choose the next element > x.
The next greater element could be the closest or the next smaller element could be the closest. Either way, they are next to each other as arr is sorted.

How to get k elements at the end of the array?
Pick one by one if available. If at the right end, pick left elements. Vice-versa

- Algorithm:
Use binary search to find index of x or next greater element

Get k number of elements.
sliding window to pick one by one
Use l & r pointers as excluding boundary.
For exclusion, the count will be: r - l - 1
For inclusion, the count will be: r - l + 1
For same value, LOWER INDEX is closer
r pointer starts at the index from binary search

Complexity:
Time: O(log N + K) for binary search and picking k elements
Space: O(1). O(K) if new array is created to store and return k elements.

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        r = self.binarySearch(arr, x)
        l = r - 1
        while (r - l - 1) < k:
            if r == len(arr) or (l >= 0 and abs(arr[l] - x) <= abs(arr[r] - x)):
                l -= 1
            else:
                r += 1
        
        return arr[(l + 1) : r]

    def binarySearch(self, arr: List[int], target: int) -> int:
            l, r = 0, len(arr) - 1

            while l < r:
                mid = l + (r - l) // 2
                if arr[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            return l