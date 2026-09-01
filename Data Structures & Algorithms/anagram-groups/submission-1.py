class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a standard dictionary
        anagram_map = {}

        for s in strs:
            # Create the canonical key (sorted string)
            key = "".join(sorted(s))
            
            # If the key isn't in the map, initialize it with an empty list
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Append the original string
            anagram_map[key].append(s)

        # Return the grouped values
        return list(anagram_map.values())