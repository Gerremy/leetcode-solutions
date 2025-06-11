class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == target:
                return mid
            if array[mid] < target:
                low = mid + 1
            if array[mid] > target:
                high = mid - 1
        
        return low
