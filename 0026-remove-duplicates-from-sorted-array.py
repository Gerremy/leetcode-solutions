class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Okay so it sounds like our objective is not necessarily to remove things from the
        # array, but reorder them instead. So i serves as the front of the array and j is the
        # comparison pointer. If array[j] != array[i], then increment i because array[i] is
        # unique and make array[i] = array[j]. If array[j] == array [i], then increment j to
        # continue scanning the array. And since the array is already sorted, we don't have
        # to worry about duplicates showing up later. So then you keep going and eventually
        # all of the numbers before and including i will be unique.

        unique_index = 0

        for scanner in range(1, len(nums)):
            if nums[scanner] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[scanner]
        
        count = unique_index + 1
        return count
        
