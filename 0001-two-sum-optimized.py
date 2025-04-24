class Solution(object):                                        # "object" means this class inherits from Python’s base class. 
                                                               # A class is like a blueprint that organizes related functions (methods) and data.

    def twoSum(self, nums, target):                            # Define a method that takes in the list of numbers and a target integer
        dictionary = {}                                        # Initialize an empty dictionary to store previously seen numbers and their indices

        for i, num in enumerate(nums):                         # Loop through the list while keeping track of both index (i) and value (num)
            complement = target - num                          # Calculate the number needed to reach the target from the current number
            if complement in dictionary:                       # Check if that needed number has already been seen
                return [dictionary[complement], i]             # If yes, return its stored index and the current index
            dictionary[num] = i                                # Otherwise, store the current number and its index in the dictionary
