class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        length = 1
        substring = set()

        i = 0
        j = 1
        substring.add(s[0])

        while j < len(s):
            if s[j] in substring:
                substring.discard(s[i])
                i += 1
            else:
                substring.add(s[j])
                length = max(length, j-i+1)
                j += 1

        return length