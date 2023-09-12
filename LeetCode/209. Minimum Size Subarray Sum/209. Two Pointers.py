# Input:
"""
int arr. elements are ALL POSITIVE.
int value target. Look for a subarray with sum >= target.
"""

# Output:
"""
Int >= 0. Len of smallest subarray with sum GREATER OR EQUAL to the input target
0 if no subarray can sum to the target
"""

# General cases & example I/O:
"""
[2, 3, 6, 7, 4], 11 -> 2. [2, 3, 6] and [6, 7] sums to greater than 11. Choose the smaller len subarr
[2, 3, 1, 4], 5 -> 2. Two subarr same length
"""

# Edge cases:
"""
[1, 2, 3, 4], 4 -> 1 when arr element has a target value
[1, 2, 3, 4], 8 -> 0 when no subarr can sum to the target.
[1, 2, 3, 4], 99999 -> 0, Total sum of arr is < target, always return 0.
arr len = 0 possible? (Constraint says arr will have at least 1 element)
For arr len = 1, just check 0th element with the target to return 0 or 1.
"""

# High level:
"""
(1) Generate a subarray -> (2) Get sum -> (3) Check length smaller if sum == target

For step 1, do we really need to generate subarrays?
For the desired output, what really matters? Just need to know there is a subarr with certain length & sum.
Actual values inside the subarr does not need to be known.

For step 2, would generating prefix sum arr be useful?
For prefix sum arr with j > i, potential answer if (prefix_sum[j] - prefix_sum[i]) >= target since this means the subarr sum was >= target.

Notice to get the smallest subarr, the best way will be finding LARGE elements. Larger the element, shorter the subarr can be to meet the target goal. Also the input is ALL POSITIVE. So this means arr[i to j + 1] sum will be always larger than arr[i to j] as extra arr[j+1] item has been added.

So say input is [1, 1, 1, 1, 999, 1] & target is 10. The subarray will continue to increase until 999 gets found and then smaller subarr between arr[0:4] could be checked by reducing the range and subtracting values starting from the left. Decreasing range guarantees decreasing sum because values are ALL POSITIVE.

The above points sound like two pointer sliding windows approach could work for this problem as ALL POSITIVE plays as an important factor for this approach to work.

For ALL POSITIVE, there was a good consistent reasoning when moving the right pointer, which was to increase the sum.
If negative values are in the input, probably O(N^2) time complexity solution unless memory gets used. 
New reasoning & approach required for negative numbers as the input dynamic is different. Increasing subarr does not consistently increase the sum as a new num could be positive or negative.
"""

# Algorithm:
"""
Base case:
If len == 1, return 1 if arr[0] element >= target.

Target could be greater than sum of all values, so set initial min_len as N + 1 to indicate subarr not found. If subarr gets found, the value will be <= N

Use R & L pointers to denote as range of current subarray.
Iterate the input arr and add it to current subarray sum. This will be R pointer.
When cur_sum >= target after new R pointer val gets added, the condition became satisfied, so check sub array's length.
While cur_sum >= target, reduce sub array range & the sum by moving L pointer.

Return the min len IF there was a sub arr sum >= target
"""

# Complexity:
"""
Time: O(N) for iterating the input arr
Space: O(1) for just variables for indices & sum of subarr
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1 if nums[0] >= target else 0

        l, cur_sum = 0, 0
        min_subarr_len = N + 1

        for r in range(N):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_subarr_len = min(min_subarr_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
                
        return 0 if min_subarr_len > N else min_subarr_len