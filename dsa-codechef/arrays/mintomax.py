class Solution:
    def count_non_minimum(self, nums):
        if not nums:
            return 0
        
        # Find the minimum value in the array
        m = min(nums)
        
        # Count how many elements are not equal to the minimum value
        operations = 0
        for x in nums:
            if x != m:
                operations += 1
                
        return operations