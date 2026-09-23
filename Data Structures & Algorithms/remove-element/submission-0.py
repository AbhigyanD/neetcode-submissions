class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = []
        for num in nums:
            if num == val:
                continue
            c.append(num)
        for i in range(len(c)):
            nums[i] = c[i]
        return len(c)
        