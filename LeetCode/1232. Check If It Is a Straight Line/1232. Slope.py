# Input:
"""
2D array. Only 2 columns
Each row represents a point x, y
"""


# Output:
"""
Bool. Whether ALL points are in a straight line
"""


# General cases & I/O:
"""
Straight line
[[0, 0], [1, 4], [2, 8], [3, 12]] -> True

Not straight line
[[1,2], [4, 9], [100, 1000]] -> False

Q: Are input points in sorted order with X & Y?
i.e. can my first example be in this order:
[[0, 0], [3, 12], [1, 4], [2, 8]]
A: No clarification provided. Will assume not in any order

Q: Can X or Y be negative?
A: Yes
"""


# Edge cases:
"""
Q: Empty input? Input with 1 point? Return T or F?
A: input len >= 2

Input with 2 points = ALWAYS straight line

Input with same points. [[0,0], [0,0], [0,0], [0,0]].
A: Not possible. All points unique

Horizontal or vertical line? Where all X or Y coordinates are equal? Maybe special cases that might need to be handled.
"""


# High level:
"""
From high school memory, straight line: y = mx + b
Mathematically speaking, m is the slope and b seems to determine position of the line on the y-axis. It determines (0, b) point. So it seems b doesnt matter and m which is the slope seems to be the more important factor to see if multiple points are in the same line.

This is because intuitively speaking, the exponential curve is not a straight line because the rate of change is keep increasing. So straight line's slope is the rate of change which is a in this case will be a constant.

Slope = change in y / change in x
Slope1 = y2 - y1 / x2 - x1
Slope2 = y3 - y1 / x3 - x1
Keep slope1 and use it to compare it to all other slopes of other points. They all should be the same for it to be a straight line.

The above approach seems to be fine for most cases, but the edge case of VERTICAL LINE seems like it could cause a problem. All x's are equal and it will cause division by zero so need to handle this case.

Mathematically, the division could be avoided. Instead of dividing, multiply x delta to the other side. This approach will work because all points are unique so this means when deltaX = 0, deltaY must not be 0 so checking the straight line in this approach will work.
Slope1 = Slope2
y2 - y1 / x2 - x1 = y3 - y1 / x3 - x1
y2 - y1 * x3 - x1 = y3 - y1 * x2 - x1
"""


# Algorithm/Pseudo:
"""
delta_y_const = y2 - y1
delta_x_const = x2 - x1

for all (x, y) after point2
    delta_y_cur = y - y1
    delta_x_cur = x - x1
    return false if delta_y_const * delta_x_cur != delta_y_cur * delta_x_const
"""


# Time Complexity: O(N)
"""
Time to traverse all points from the input
"""


# Space Complexity: O(1)
"""
Only storing 2 values
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        y_delta, x_delta = self.getDeltas(coordinates[0], coordinates[1])

        for cur_point in coordinates[2:]:
            cur_y_delta, cur_x_delta = self.getDeltas(coordinates[0], cur_point)
            if y_delta * cur_x_delta != cur_y_delta * x_delta:
                return False

        return True

    def getDeltas(self, point1: List[int], point2: List[int]) -> Tuple[int, int]:
            y_delta = point2[1] - point1[1]
            x_delta = point2[0] - point1[0]
            return (y_delta, x_delta)