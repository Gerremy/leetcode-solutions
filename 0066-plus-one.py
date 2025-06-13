class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)
        j = 1

        if i == 0:
            return [1]
        else:
            if i == 1:
                if digits[i - j] != 9:
                    digits[i - j] += 1
                else:
                    return [1,0]
            else:
                if digits[i - j] != 9:
                    digits[i - j] += 1
                else:
                    while (i - j >= 0) and (digits[i - j] == 9):
                        digits[i - j] = 0
                        j += 1
                    if i - j < 0:
                        digits.insert(0, 1)
                    else:
                        digits[i - j] += 1
        
        return digits
