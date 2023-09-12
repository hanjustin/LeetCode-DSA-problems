# Input:
"""
Arr of int & null to representing binary tree node
"""

# Output:
"""
2D arr with each row representing level of binary tree.
Each row traversal direction changes. Cur lvl: L -> R, Nxt lvl: R -> L
Only int values are present and null values from the input are gone
"""

# General cases & example I/O:
"""
[3, | 4,7] -> [[3], [7,4]]
[3, | 6,8, | 1, null,null, 2] -> [[3], [8, 6], [1, 2]]
"""

# Edge cases:
"""
Empty arr. Return empty arr
len == 1 arr. Return [[Root]]
Completely unbalanced tree (Linked List)
"""

# High level:
"""
To get output from input,
1. Row has nodes in the same level
2. Traversal direction needs to change for each row
Even lvl: L -> R
Odd lvl: R -> L

For #1, BFS using queue first comes to mind.
For #2, change traversal direction while creating rows or after creating rows.
If reverse odd lvl rows after creating all levels, there will be extra work at the end. This extra work could be avoided by reversing directions while creating them.

Add node beginning of the list to have reversed direction level.
If array gets used, inserting in the beginning will be costly. So use deque instead for creating row levels.
"""

# Algorithm/Pseudo:
"""
Traversing the tree: queue + BFS
Creating row levels: deque

Initialize _queue with root
While _queue is not empty, continue BFS traversal.
    Start BFS lvl traversal by:
    - Save _queue.count. This is cur tree lvl's nodes count.
    - Output direction L -> R or R -> L? Can figure this out by having another int as _cur_lvl,
      but can avoid by just using count of results array.

    For _queue.count, (to build row_lvl)
        _node = pop left of _queue
        Add _node to left or right of _cur_row_deque
        If children exist, add to _queue.

    Add _cur_row_deque to _all_rows

Return saved _all_rows
"""

# Time Complexity - O(N):
"""
Time to traverse all nodes = N
"""

# Space Complexity - O(N):
"""
BFS traversal queue - N. For completely balanced tree, the last row has N leaves.
Result array contains all nodes - N
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes_queue = deque([root])
        row_lvls = []

        while nodes_queue:
            cur_row_count = len(nodes_queue)
            cur_row_lvl = deque()
            cur_row_l_to_r_direction = len(row_lvls) % 2 == 0

            for _ in range(cur_row_count):
                node = nodes_queue.popleft()
                if cur_row_l_to_r_direction:
                    cur_row_lvl.append(node.val)
                else:
                    cur_row_lvl.appendleft(node.val)

                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
                
            row_lvls.append(cur_row_lvl)

        return row_lvls