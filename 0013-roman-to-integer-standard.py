class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Okay so you need to store the increment values
        # Then when you get an input, you just swap the values and add
        # The only exceptions are when
        #   I is placed before V to make 4
        #   I is placed before X to make 9
        #   X is placed before L to make 40
        #   X is placed before C to make 90
        #   C is placed before D to make 400
        #   C is placed before M to make 900

        roman_numeral_conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # Okay so you can go through the input and compare the first and second numbers. If the value in the dictionary at the first number is greater than the value in the dictionary at the second number, then just take the first number and store it or add it to the previous number. If the value in the dictionary at the first number is less than the value in the dictionary at the second number, than subtract the value in the dictionary at the first number from the value in the dictionary at the second number and store it or add it to the previous number. Continue through the input until there is no more second number. Then whatever your sum is is your answer.

        total = 0

        for i in range(len(s) - 1):
            if roman_numeral_conversion[s[i]] >= roman_numeral_conversion[s[i + 1]]:
                total += roman_numeral_conversion[s[i]]
            else:
                total -= roman_numeral_conversion[s[i]]
        
        total += roman_numeral_conversion[s[-1]]

        return total

        


        
