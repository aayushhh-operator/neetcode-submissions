class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if int(len(s)) != int(len(t)):
            return False

        count = [0] * 26

        for i in range(int(len(s))):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        if count == [0] * 26:
            return True
        else: 
            return False