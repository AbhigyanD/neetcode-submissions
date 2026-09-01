class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        c=0
        si=0
        t_list = list(t)
        
        for char in s:  
            if char in t_list:
                t_list.remove(char)
                c += 1
            si += 1

        if si != c:
            return False
        return True
