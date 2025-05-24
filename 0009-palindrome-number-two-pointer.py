class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # okay so I need to read in the number
        # then count the number of digits in the input
        # then i need to have a counter that starts from the beginning of the input and a counter at the end
        # set the parameters of the counter to be half the input
        # then I need to compare the number at each counter
        # if the numbers aren't the same, return false
        # if the numbers are the same, increment/decrement the counter until you get to the middle

        a = str(x);
        c = len(a);

        i = c - 1;
        j = 0;
        k = c // 2;

        if x < 0:
            return False;

        while i >= k and j < k:
            if a[i] != a[j]:
                return False;
            i = i - 1;
            j = j + 1;
        
        return True;
        
