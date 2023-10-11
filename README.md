Showing how I would approach coding interviews with data structures & algo problems.

* Multiple approaches or optimizations for some problems. `(Search 'Approach 1')`

* Untimed as for problems that I got stuck, came back to them at a later point in time for fresh perspectives.

---
[LeetCode Profile](https://leetcode.com/hanjustin/)

[![LeetCode stats](https://leetcode-stats-six.vercel.app/?username=hanjustin)](https://leetcode.com/hanjustin/)

## Problem analysis steps

<details>
  <summary><h3>Template:</h3> (Click)</summary>
Most problems were analyzed and broken down into following sections when solving them.

```
# Input

# Output

# General cases & example I/O
  Q: (Clarification Question)
  A: (Clarification Answer)

# Edge cases
  Base case if exists

# High level

# Algorithm/Pseudo

# Time/Space complexity

Code
```
</details>

## Most recent LeetCode submissions

<details>
  <summary><h3>Medium:</h3></summary>

| #    |                                          LeetCode Problem Link                                                                      |                                  My Analysis & Code                                                                               |   Time     |    Space   |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------|------------|------------|
| 8    | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)                                                   | [LinearParsing.swift](/LeetCode/8.%20String%20to%20Integer%20(atoi)/8.%20LinearParsing.swift)                                     | O(n)       | O(1)       |
| 38   | [Count and Say](https://leetcode.com/problems/count-and-say/)                                                                       | [Counting.swift](/LeetCode/38.%20Count%20and%20Say/38.%20Counting.swift)                                                          | O(x^n)     | O(x^n)     |
| 103  | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)                 | [BFS.py](/LeetCode/103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/103.%20BFS.py)                                       | O(N)       | O(N)       |
| 153  | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)                         | [Binary Search.py](/LeetCode/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/153.%20Binary%20Search.py)                     | O(log N)   | O(1)       |
| 162  | [Find Peak Element](https://leetcode.com/problems/find-peak-element/)                                                               | [Binary Search.py](/LeetCode/162.%20Find%20Peak%20Element/162.%20Binary%20Search.py)                                              | O(log N  ) | O(1)       |
| 209  | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                                               | [Two Pointers.py](/LeetCode/209.%20Minimum%20Size%20Subarray%20Sum/209.%20Two%20Pointers.py)                                      | O(N)       | O(1)       |
| 649  | [Dota2 Senate](https://leetcode.com/problems/dota2-senate/)                                                                         | [Two Queues.py](/LeetCode/649.%20Dota2%20Senate/649.%20Two%20Queues.py)                                                           | O(N)       | O(N)       |
| 658  | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements)                                                    | [Binary Search.py](/LeetCode/658.%20Find%20K%20Closest%20Elements/658.%20Binary%20Search.py)                                      | O(log N + k)  |   O(1)  |
| 852  | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)                                     | [Binary Search.py](/LeetCode/852.%20Peak%20Index%20in%20a%20Mountain%20Array/852.%20Binary%20Search.py)                           | O(log N)   | O(1)       |
| 921  | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)                       | [Counting.py](/LeetCode/921.%20Minimum%20Add%20to%20Make%20Parentheses%20Valid/921.%20Counting.py)                                | O(N)       | O(1)       |
| 986  | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)                                           | [Two Pointers.swift](/LeetCode/986.%20Interval%20List%20Intersections/986.%20Two%20Pointers.swift)                                | O(N + M)   | O(N + M)   |
| 1115 | [Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/)                                                 | [Semaphore.py](/LeetCode/1115.%20Print%20FooBar%20Alternately/1115.%20Semaphore.py)                                               | -          | -          |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/)                                                     | [Two Stacks.py](/LeetCode/1472.%20Design%20Browser%20History/1472.%20Two%20Stacks.py)                                             | Visit: <br> O(1) <br><br> Back & <br>Forward: <br> O(min(k, h)) | O(N * M)      |

</details>

<details>
  <summary><h3>Easy:</h3></summary>


| #    |                                           LeetCode Problem Link                                                                     |                                 My Analysis & Code                                                                                |   Time     |   Space    |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------|------------|------------|
| 257  | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)                                                               | [DFS.py](/LeetCode/257.%20Binary%20Tree%20Paths/257.%20DFS.py)                                                                    | O(N log N) | O(N log N) |
| 389  | [Find the Difference](https://leetcode.com/problems/find-the-difference/)                                                           | [Approach 1: HashMap.py](/LeetCode/389.%20Find%20the%20Difference/389.%20Hashmap.py)                                              | O(N)       | O(1)       |
|      |                                                                                                                                     | [Approach 2: Bitwise XOR.py](/LeetCode/389.%20Find%20the%20Difference/389.%20Bitwise%20XOR.py)                                    | O(N)       | O(1)       |
| 1108 | [Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)                                                   | [Linear Search.py](/LeetCode/1108.%20Defanging%20an%20IP%20Address/1108.%20Linear%20Search.py)                                    | O(N)       | O(N)       |
| 1114 | [Print in Order](https://leetcode.com/problems/print-in-order/)                                                                     | [Concurrency Lock.py](/LeetCode/1114.%20Print%20in%20Order/1114.%20Concurrency%20Lock.py)                                         | -          | -          |
| 1232 | [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)                                     | [Slope.py](/LeetCode/1232.%20Check%20If%20It%20Is%20a%20Straight%20Line/1232.%20Slope.py)                                         | O(N)       | O(1)       |

</details>


## Problems I got stuck

Saved analysis notes of problems I got stuck on the first try. May return to them once I 'forget' the problem context & my initial approach.

**To be updated later**

