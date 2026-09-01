class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = []
        l = len(nums)
        for i in range (l):
            for j in range (i):
                if nums[i] + nums[j] == target:
                    o.append(j)
                    o.append(i)
                    return o
        return o