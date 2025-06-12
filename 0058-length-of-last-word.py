class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = len(s) - 1
        count = 0

        if s[i] != " ":
            while i >= 0 and s[i] != " ":
                count += 1
                i -= 1
        else:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i == 0:
                if s[i] != " ":
                    return 1
                else:
                    return 0
            else:
                while i >= 0 and s[i] != " ":
                    count += 1
                    i -= 1
        
        return count
