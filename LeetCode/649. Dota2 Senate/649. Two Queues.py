# Input:
"""
str of characters R & D
Can be any order and characters next to each other don't have to be different.
"""

# Output:
"""
Radiant or Dire depending on the winner
Winner is the one that is left at the end who can still vote
"""

# General cases & example I/O:
"""
RDRD -> Radiant
RRDD -> Radiant
DRDRR -> Dire
"""

# Edge cases:
"""
Empty string (Constraint says len >= 1)
len(N) == 1 or len(N) == 2. (Can return winner immediately by looking at input[0])
"""

# High level:
"""
Like a turn based game where the goal is to kick the next offensive player on the other team
Going from left to right order so the team on the left always has an initial advantage over the other team.
i.e. RDRD  Even though R & D have the same number of players, R team has advantage and wins for starting first.
The game continues until all players in the other team are eliminated.

What does 'smart enough and play the best strategy' mean?
For each move, the goal is to not only kick one player in the other team, but also to save a teammate.
This can be achieved by eliminating the NEXT player on the other team.

Say input RDRDD can be represented as with ordering number: (R1)(D1)(R2)(D2)(D3)
If R1 kicks D2 instead of D1, D1 can kick R2.
So it is best for R1 to kick D1 who goes first before D2 to save R2.

So to achieve the best strategy, R1 somehow needs to kick D1 and R2 also kick D2
Also at the end of the first round, D3 needs to somehow kick R1.
Before D3 makes the move, the ordering of players' moves look like:
(D3)(R1)(R2) - After two moves from input RDRDD
(R2)(D3) - (D3) kicked (R1). Now (D3) is after (R2)
(R2) - (R2) kicked (D3)

It seems as if the player who makes a move goes at the end of a move queue.
For the example RDRDD, if there is one move queue:
Q = (R1)(D1)(R2)(D2)(D3)
(R1) can easily be accessed and get moved to end of the queue,
but somehow needs to easily find & access (D1)

So instead of one queue, try two queues:
R_Q = (R1)(R2)
D_Q = (D1)(D2)(D3)

Need to know who makes first move, so change the numbering to the index of the input string.
R_Q = (R0)(R2)
D_Q = (D1)(D3)(D4)

(R0) will make the first move, but later on, it also might need to make a move again after the last element.
So change (R0) to (R5) to change the saved index from 0 to 5 which is adding N each time after making a move.
"""

# Algorithm:
"""
Iterate the input. Add index of 'R' and 'D' to R_Q and D_Q respectively.
Out of the two queues, pop the smaller element and add N to the value and add it back to the queue.
pop the first element of the other queue.
Repeat until R_Q or D_Q becomes empty.
Return winner of the team. "Radiant" if len(R_Q) > 0 else "Dire"
"""

# Complexity:
"""
Time: O(N) for iterating the input string. There could be multiple rounds but O(X # of times * N) becomes O(N)
Space: O(N) = O(2 * N) from the two queues
"""

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) <= 2:
            return "Radiant" if senate[0] == "R" else "Dire"
        
        N = len(senate)
        radiant_queue = deque()
        dire_queue = deque()

        for i, c in enumerate(senate):
            if c == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while len(radiant_queue) > 0 and len(dire_queue) > 0:
            next_move_team = radiant_queue if radiant_queue[0] < dire_queue[0] else dire_queue
            voter_lossing_team = dire_queue if radiant_queue[0] < dire_queue[0] else radiant_queue

            voter = next_move_team.popleft()
            next_move_team.append(voter + N)
            voter_lossing_team.popleft()
        
        return "Radiant" if radiant_queue else "Dire"