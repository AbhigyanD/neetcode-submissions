class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Check characters column by column
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # If we reach the end of any string or characters don't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
                    
        return strs[0]