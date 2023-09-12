/*
---- Input ----
int positive
Number of times to repeat the say process


---- Output ----
str w/ ints only


---- General cases & example I/O ----
F(1) = "1"
F(n) = say output of F(n - 1)

Testcase auto-generated I/O examples.
1 -> "1"
2 -> "11"
3 -> "21"
4 -> "1211"
5 -> "111221"
6 -> "312211"
7 -> "13112221"
8 -> "1113213211"


---- Edge cases ----
1 -> str(input) = "1"
Q: 0 or negative int possible? (Constraint: No. n >= 1)


---- High level ----
What does "say" mean?
Given an int string -> Read it aloud: count digits & say the value -> write numbers for what you hear from prev step

For N, get int string from N - 1. F(N) will READ str output of F(N - 1)
So for the generated I/O, the say steps were:
F(1) = "1"
2 -> Read "1" = One 1 = "11"
3 -> Read "11" = Two 1 = "21"
4 -> Read "21" = One 2, One 1 = "1211"
5 -> Read "1211" = One 1, One 2, Two 1 = "111221"

Say "digits" = (Count + digit value) * x where x is number of digit value changes from the left.

So to say any digits string, from left to right, count how many digits are the same.
If a new digit gets found, append count & current digit. i.e. sayString += str(count) + str(curDigit)

Repeat this say process N times.


---- Algorithm/Pseudo ----

guard N > 1

_curDigitsStr = "1" as we start from 1

For N - 1 times
    _nextDigitsStr = ""

    Traverse _curDigitsStr
        Count how many same digits are together in _curDigitsStr
        _nextDigitsStr.append count & curDigit

    _curDigitsStr = _nextDigitsStr

return _curDigitsStr

---- Time complexity: O(x^n) ----
The time is dependent on the length of digits string each step as counting digits left to right.
From F(n - 1) to F(n), how much length change is there?
What is the rate of change for the length of digits string?

Copy-paste from I/O section:
1 -> "1"
2 -> "11"
3 -> "21"
4 -> "1211"
5 -> "111221"
6 -> "312211"
7 -> "13112221"
8 -> "1113213211"

The length is, but not seeing a clear pattern from the total length.
1 -> 2 -> 2 -> 4 -> 6 -> 6 -> 8 -> 10

Any pattern to the number of digits itself or any cycle? As they relate to the length.
1 -> 11 -> 21 -> 1211 -> 111221 -> 312211
Not seeing any clear pattern.

let x denote a random integer, but still can't find pattern.
x -> 1x -> 111x -> 311x -> 13211x

IF length doubled for each digit, the time complexity will be O(2^n)
2^n = (length change rate) ^ (for EACH increase of n)
“1”
“11”
“1111”
“11111111”.  Length is 8 after three iterations. 2^3 = 8

For this problem, the closest time complexity I can get is x^n as I can't see clear rate of growth.

---- Space complexity: O(x^n) ----
Only the output string requires memory.
Although the problem statements sounds like recursion, there is no recursion stack.

Just like time, space is dependent on the length of generated digits string.
So the space has the same complexity as time.
*/


class Solution {
    func countAndSay(_ n: Int) -> String {
        guard n > 1 else { return "1" }

        var curDigits: [String] = ["1"]

        for _ in 0..<(n - 1) {
            var nextDigits = [String]()
            var (i, count) = (0, 0)

            while i < curDigits.count {
                for digit in curDigits[i...] {   // AFAIK, no O(n) copy for array slicing in swift
                    guard digit == curDigits[i] else { break }
                    count += 1
                }

                nextDigits += [String(count), curDigits[i]]
                i += count
                count = 0
            }

            curDigits = nextDigits
        }
        
        return curDigits.joined()
    }
}