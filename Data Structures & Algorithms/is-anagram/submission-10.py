class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = "".join(sorted(s))
        newT = "".join(sorted(t))
        if(len(s) != len(t)):
            return False
        for i in range(len(newS)):
            if(newS[i] != newT[i]):
                return False
        return True