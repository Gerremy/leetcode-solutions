class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack) - len(needle) + 1): # loop through the length of haystack
            if haystack[i] == needle[0]: # if haystack at the current index matches the first character in needle
                for j in range (len(needle)): # loop through the length of needle
                    if haystack[i + j] != needle[j]: # if haystack at the corresponding index to needle does not equal needle
                        break # escape the loop
                else: # if the loop above ran without breaking
                    return i   # return the index of the first occurance of the needle in the haystack
        return -1 # if you've returned nothing thus far, that means that you didn't find a match so return -1
