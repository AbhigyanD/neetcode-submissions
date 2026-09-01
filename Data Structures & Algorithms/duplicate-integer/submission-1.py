class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=0
        i=0
        for i in range (len(nums)):
            if nums[i] in nums[:i:]:
                c=c+1
        if c>0:
            return True
        else:
            return False        