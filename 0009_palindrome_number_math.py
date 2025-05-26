class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes
        # Numbers ending in 0 are not palindromes unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):                                 # checks if the number is negative or if the number ends in 0 (divisible by 10 and non-zero)
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10                                                    # this divides x by 10 and then the remainder is the last digit in the number
            reversed_half = reversed_half * 10 + digit                        # takes the current number in the 'reversed-half' space and bumps it up an order of 10, and then puts the new digit where the zero would be
            x = x // 10

        # Handles both even and odd digit lengths                             
        return x == reversed_half or x == reversed_half // 10                 # checks if the halves equal each other, if the number has an even number or odd number of digits
