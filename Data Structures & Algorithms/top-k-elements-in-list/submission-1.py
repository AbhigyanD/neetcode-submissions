class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        counts = Counter(nums)
        counts = Counter(nums)
        
        # 2. Extract the 'k' most common. 
        # .most_common(k) returns a list of tuples: [(3, 3), (2, 2)]
        most_common_items = counts.most_common(k)
        
        # 3. Pull out just the elements (the first item in each tuple)
        return [item[0] for item in most_common_items]
        