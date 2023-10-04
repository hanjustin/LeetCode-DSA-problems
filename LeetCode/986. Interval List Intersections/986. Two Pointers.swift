/*
---- Input:
Two 2D int arrays. Two lists length can be different.
Each array = list of ranges. Range has start & end int val
Each row = one range. Start & end = 1st & 2nd column respectively
Ranges disjoint & in sorted order.


---- Output:
Two 2D int arrays
Intersections of the ranges


---- General cases & example I/O:
1. Partial intersection range
[1, 10] & [5, 20] -> [5, 10]

2. Completely intersecting. One range within another bigger range
[1, 100] & [5, 10] -> [5, 10]

3. Intersection length = 0. Range1's end time & Range2's start time overlap
[1, 5] & [5, 10] -> [5, 5]

4. No intersections
[1, 2] & [100, 200] -> []


---- Edge cases:
One of the lists has 0 range = No intersections = Return empty array
[1, 1000] & [] -> []

A range is extremely large and contains all smaller ranges in other list
List1 = [[1, 1000]]
List2 = [[10, 20], [30, 40], [50, 60]]
List1 & List2 Input -> Output exactly same as List2


---- High level:
What does disjoint & sorted order mean?
For each list, the intervals have no overlapping.
List1[0] has range that is before range of List1[1].
Meaning, List1[0] has start & end value less than List1[1] start & end

Since this is true for both lists, this could be used to simplify intersection check process.
List1[0] range < List1[1] range
List2[0] range < List2[1] range

If List1[1] intersects with List2[0],
List1[0] could also intersect with List2[0], but
List1[0] can't intersect with List2[1].

Ok then what's the order of intersection checks of two lists?
Said above List2[0] could intersect with List1[1].
This happens only if List2[0].end > List1[0].end && List2[0].end > List1[1].start
So iterate two lists from left to right and repeatedly check two ranges.
Check if List1[0] & List2[0] has intersection.
Keep the range that has end time later and compare it to next range in the other list.

From left to right, iterate two lists with two different runners.
    Select two ranges from the two lists
        If there is intersection, add it to result.

    Check which runner to increment
        Keep one of the ranges from above.
        Increment to compare next range with the kept range.


---- Algorithms/Pseudo:

while i < N && j < M
    if range1 contains start or end of range2 has intersection. Vice versa
        add intersection

    if range1.end < range2.end
        increment runner1 to discard range1
    else
        increment runner2 to discard range2


---- Time Complexity: O(N + M)
N = list1.count, M = list2.count
Iterating two lists. The longer list will be the dominating factor how long it takes


---- Space Complexity: O(N + M)
Number of ranges determine number of intersections of the output array.

*/

class Solution {
    func intervalIntersection(_ firstList: [[Int]], _ secondList: [[Int]]) -> [[Int]] {
        var intersections = [[Int]]()
        var (i, j) = (0, 0)

        while i < firstList.count && j < secondList.count {
            if let intersection = intersection(of: firstList[i], and: secondList[j]) {
                intersections.append(intersection)
            }

            if firstList[i].end < secondList[j].end {
                i += 1
            } else {
                j += 1
            }
        }

        return intersections
    }

    func intersection(of range1: [Int], and range2: [Int]) -> [Int]? {
        let low = max(range1.start, range2.start)
        let high = min(range1.end, range2.end)
        let hasIntersection = low <= high

        return hasIntersection ? [low, high] : nil
    }
}

private extension Array { // Just for code readability
    var start: Element {
        return self[0]
    }

    var end: Element {
        return self[1]
    }
}