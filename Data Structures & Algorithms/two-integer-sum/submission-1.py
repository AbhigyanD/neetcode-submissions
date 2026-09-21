class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = []
        for i in range(0,len(nums)):
            for j in range (0,i):
                if nums[i]+nums[j] == target:
                    c.append(j)
                    c.append(i)
        return c
        