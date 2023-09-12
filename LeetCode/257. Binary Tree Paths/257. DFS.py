"""
- Input:
Binary tree node
Node contains integer value

- Output:
Arr of string for tree paths in ANY order.
Int values with "->" in between
i.e.
["1->2->3->4", "1->2->3"]
["1->2->3"]

- General cases:
One path (Singly linked list) (One leaf node)
Multiple root-to-leaf paths (Multiple leaf nodes)

Node with negative value. (How should this be represented in the output?)
i.e.
Tree with 1 & 2 output is ["1->2"]
Tree with -1 & -2 should ["-1->-2"]?

- Edge cases:
0 node tree (Constraint gurantees at least one node)
Unbalanced binary tree singly list style

- High level:
Start from root.
For each node, check children.
If has a left child, go down left.
If has a right child, go down right.
If both are not present, the node is a leaf node, and we got one full path.
Save this root-to-leaf path.
Move up to the parent while deleting the leaf node from traversed path.
Repeat these steps.

- Algorithm:
Start DFS from root.
The output asks for list of strings.
Creating new path by copying previous path string and adding new node will cost O(n) of the string
To avoid recreating string all the time, use backtracking to add/remove path and only build the whole string at leaf nodes.

Recursively traverse DFS,
Base case: If node is None, do nothing.
Save current node value to `path` keep track of traverse path
If both L & R are None,
    combine current path so far with "->" and add to results
else:
    DFS to left
    DFS to right

Now backtrack by:
POP current value from the path as when it has returned to the recursion call stack after going left & right, it means it has traversed left & right subtree and current node is no longer relavant for DFS traverse path.

return all saved results after initial dfs has ended.

- Complexity:
The output asks for strings of paths, and it takes O(h) tree height to build one path string. 

Time:
O(N * log N)

Time to traverse all nodes: O(N)

Time to build results output:
Completely unbalanced tree (Linked list):
Leaf count: 1
height of the tree: N
Time to build paths: O(N)

Completely balanced tree:
Leaf count: N/2
height of the tree: log(N)
Time to build paths: N/2 * log(N) = O(N/2 * log N) = O(N * log N)

Space: 
h is height of the tree and this will be the 
Recursion stack:
O(h). O(N) for LinkedList and O(log N) for completly balanced tree

Results string array:
Completely unbalanced tree (Linked list):
Results array: Leaf count (1) * height (N) = O(N)

Completely balanced tree:
Results array: Leaf count (N/2) * height (log N) = O(N * log N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        cur_path = []
        saved_paths = []

        def find_root_to_leaf_path(root: Optional[TreeNode]):
            if root is None:
                return

            cur_path.append(str(root.val))

            if root.left is None and root.right is None:
                root_to_leaf_path = "->".join(cur_path)
                saved_paths.append(root_to_leaf_path)
            else:
                find_root_to_leaf_path(root.left)
                find_root_to_leaf_path(root.right)
            cur_path.pop()
        
        find_root_to_leaf_path(root)
        return saved_paths