class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Add 1 to convert from 0-indexed to 1-indexed
                return [left + 1, right + 1]
            
            elif current_sum < target:
                left += 1  # The sum is too small, move the left pointer up
            else:
                right -= 1  # The sum is too large, move the right pointer down
                
        return []
