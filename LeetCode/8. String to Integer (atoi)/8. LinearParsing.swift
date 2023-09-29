/*
---- Input ----
String with mix of: space, -, +, digits, lowercase & uppercase English letters.


---- Output ----
int parsed from input string.
Values in 32 bit range. So min & max values clamped to: -2^31 & 2^31 - 1


---- General cases & Example I/O ----
+ and - are only for signs and not arithmetic?
Problem states: "Ignore the rest of the string after the digits."
So arithmetic is not possible as a sign and digits after a number will be ignored.

Inputs with case description
"  -010101 space sign zero num" -> -10101
"  -     5-10 space between sign and num" -> 0
"  word -5-10 word before sign num" -> 0
"  word-5-10" -> 0
"  010101 space binary" -> 10101
"  123 space num then words" -> 123
"123 num then words" -> 123
"words then num 123" -> 0


---- Edge cases ----
No digits? (Rule #4: Return 0)
Input str with large number. Over/underflow?
(Assumption: the environment is limited to only 32 bit so can't use double type to store value outside of 32 bit range)


---- High level ----
Parse positive/negative number from string input.

Looking at I/O examples from above and reading the problem,
input can be simplified to two outcomes.
0 for input without valid number
32 bit int for intput with valid number

Then the question is, when does the input have a valid number?
Valid number exists when pseudo-Regex format is satisfied:
(0-n Whitespaces)(0-1 + or -)(1-n VALID DIGITS)(0-n Everything else including extra digits after non-digits)
So look for first +, -, or digit from the left to find valid digits. If above regex not satisfied, return 0.

After the sign (if it exists), trim leading zeroes.
Then check if the valid number doesnt cause under/overflow

Should not add digit unless there will be no overflow from new extra digit.
Can check this by comparing current value to Int.max without the last digit. (Int.max / 10)
Case 1. If curVal > Int.max/10, can't add any degit. Always overflow
Case 2. If curVal == Int.max/10, then the last digit of Int.max determines overflow happens or not.
Overflow if new digit > Int.max % 10

Similar process as underflow. Sign gets multipled at the end as well.
Int.max & Int.min last digits are different.
But check of case 1 for both overflow & underflow are the same.
Case 2 is similar, but slightly different because of different last digit.


---- Algorithm/Pseudo ----

i = Get index of first non-whitespace char
if has + or -, set positive/negative sign & i++
if input[i] == letter, return 0
curVal = 0

while input[i] == digit
    Check under/overflow && if out of range, return min/max
    curVal = curVal * 10 + digit
    i++

return curVal

Note there is no need to trim leading zeroes as curVal & digit will be both 0 when leading zeroes encountered.
Also note that the check for both under/overflow can be simplified.
Max last digit = 7 & Min last digit = 8
Appending last digit as 8 will cause overflow error so will return Int.max
Appending last digit as 8 will not cause underflow error, so can return Int.min
So technically 8 is not causing an underflow error, but just like for the overflow scenario,
we will still return Int.min, so we can return Int.min & Int.max whenever the last digit > 7 and check the sign.


---- Time complexity: O(N) ----
To traverse input string. Worst case is input string is whitespace or all zeroes


---- Space complexity: O(1) ----
Only using variables to hold some integers.

*/

class Solution {
    func myAtoi(_ s: String) -> Int {
        let s = Array(s)
        guard s.count > 0 else { return 0 }
        
        let firstNonSpaceCharIndx = s.firstIndex { $0 != " " } ?? s.count
        let (hasFirstCharSign, hasNegSign) = containsSignChar()
        let sign = hasNegSign ? -1 : 1
        var i = firstNonSpaceCharIndx + (hasFirstCharSign ? 1 : 0)
        let outputParsedInt = parseInt()

        // Not sure if multiple nested functions increase code readability
        func containsSignChar() -> (Bool, Bool) {
            guard firstNonSpaceCharIndx < s.count else { return (false, false) }
            let c = s[firstNonSpaceCharIndx]
            return (Set(["-", "+"]).contains(c), c == "-")
        }

        func parseInt() -> Int {
            // Guard not needed but added for sake of completeness. Handles non-digits char after sign. i.e: "  -   42"
            guard i < s.count, s[i].isNumber else { return 0 }

            var magnitude = 0
            while i < s.count, let digit = s[i].wholeNumberValue {
                guard isNotOutOfRangeAfterAdding(digit, to: magnitude) else {
                    return Int(hasNegSign ? Int32.min : Int32.max)
                }

                magnitude = magnitude * 10 + digit
                i += 1
            }

            func isNotOutOfRangeAfterAdding(_ digit: Int, to magnitude: Int) -> Bool {
                let (maxNoLastDigit, lastDigitOfMax) = (Int32.max / 10, Int32.max % 10)
                let outOfRangeForAnyExtraDigit = maxNoLastDigit < magnitude
                let digitTooBigForMagnitude = digit > lastDigitOfMax && maxNoLastDigit == magnitude
                return (outOfRangeForAnyExtraDigit || digitTooBigForMagnitude) == false
            }

            return sign * magnitude
        }

        return outputParsedInt
    }
}