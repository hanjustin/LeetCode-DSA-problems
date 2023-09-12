# Input:
"""
new URL str for `visit`
# of steps for `back` & `forward`
"""

# Output:
"""
`void` for `visit`
new or current URL for `back` & `forward`
"""

# General cases & example I/O:
"""
Traverse history X number of steps backward or forward
Add a new page to history.

( ) denotes current position
Visit P1. (P1)
Visit P2. P1 - (P2)
Back 1. (P1) - P2
Forward 1. P1 - (P2)
Back 1. (P1) - P2
Visit P3. P1 - (P3)
"""

# Edge cases:
"""
Visit same page twice in a row (Assume this just adds the same page to the history just like any other page)
Higher number of back or forward steps than len(history) (Return URL at the start or end of the history)
"""

# High level:
"""
Need to store URL str.
There needs to be an order & need to able to move forward or backward.
One backward makes the current page to becomes the next forward page.
After one backward, should be able to get to the most recent forward. 
Needing access to the most recent forward page is like just another LIFO stack.

Possible DS to help
array, stack, queue, singly LL, doubly LL

1) One doubly LL.
2) Two stacks or two singly LL.
One stack/singly LL for prev history and the other stack/singly LL for forward history.
Will be able to have most recent prev and next accessible by having two LIFO storage.
Traverse action will move URL from one stack to another stack.
i.e. Move forward -> pop `forward_list` -> push popped element to `history` (vice versa)
3) Dynamic array for O(1) back & forward function, but insertion worst case O(n)
"""

# Algorithm:
"""
Doubly LL:
Traverse `prev` & `next` for `back` & `forward`
`Visit`: Add new `next` node to remove the existing `next` sublist.

Two stacks or singly LL:
Have two variables `history` & `forward_list`.
Have LIFO Access top of the stacks or keep pointer to the heads of singly LL
Have top of `history` as current page
New `visit` will make `forward_list` empty.
"""

# Complexity:
"""
Time:
For two stacks,
Visit: O(1).
Back & Forward: O(min(steps, len(history)))

For dynamic array,
Visit: O(n) & average of O(1)
Back & Forward: O(1), can use array index for instant access to prev/next

Space:
O(N * M). N is len of history & M is len of URL
"""

from collections import deque

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque([homepage])
        self.forward_list = deque()

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forward_list = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            new_forward = self.history.pop()
            self.forward_list.append(new_forward)
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_list:
            new_cur = self.forward_list.pop()
            self.history.append(new_cur)
            steps -= 1
        return self.history[-1]
