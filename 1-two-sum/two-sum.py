class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i,v in enumerate(nums):
            diff = target - nums[i]
            if diff in dic:
                return [dic.get(diff),i]
            dic[v] = i
        