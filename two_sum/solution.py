class Solution:
    def twoSum(self, nums, target):
        j = 1
        for i in nums:
            while j < len(nums):
                if i + nums[j] == target:
                    return(nums.index(i), j)
                j += 1
