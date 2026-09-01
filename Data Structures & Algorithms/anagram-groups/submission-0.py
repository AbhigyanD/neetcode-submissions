class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # 1. Create a unique key by sorting the string
            # "eat" becomes "aet", "tea" also becomes "aet"
            sorted_s = "".join(sorted(s))
            
            # 2. Add the original string to the list belonging to that key
            anagram_map[sorted_s].append(s)

        # 3. Return only the values (the groups)
        return list(anagram_map.values())
            