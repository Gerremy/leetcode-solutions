class Solution(object):                             # Define a class called Solution that will contain our function
    def twoSum(self, nums, target):                 # Define the function twoSum that takes in self, a list of numbers, and a target value

        """
        :type nums: List[int]                       # nums should be a list of integers
        :type target: int                           # target should be a single integer
        :rtype: List[int]                           # the function returns a list of two indices (integers)
        """

        for i in range(len(nums)):                  # Loop through the indices of the nums list from 0 up to (but not including) the length of nums
            for j in range(i + 1, len(nums)):       # Inner loop: check all indices after i to avoid checking the same pair twice
                if nums[i] + nums[j] == target:     # Check if the sum of the values at indices i and j equals the target
                    return [i, j]                   # Return the indices i and j if their values add up to the target
