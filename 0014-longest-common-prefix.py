class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # You need to scan the array and 
        # strs[0] = flower
        # loop through the 
        # you need to take each string and characterize it
        # and make an array for each of the characers in one string word
        # then you need to loop through each array, comparing the first characters
        # if any of the 
        
        prefix = ""  # variable to store the common prefix

        if len(strs) == 1:  # if the input is of length 1
            return strs[0]  # return the only input string

        for j in range(len(strs[0])):  # loop through the length of the first word
            current_char = strs[0][j]  # get the jth character of the first word

            for i in range(1, len(strs)):  # loop through the rest of the words
                current_word = strs[i]  # this is the ith word

                if j >= len(current_word) or current_word[j] != current_char:
                    # if the current word is too short OR the jth character doesn't match
                    return prefix  # return the prefix built so far

            prefix += current_char  # add the matching character to the prefix

        return prefix  # return the final common prefix
