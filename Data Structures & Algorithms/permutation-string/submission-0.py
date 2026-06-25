class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        n1 = len(s1)
        n2 = len(s2)
        print(n1, n2)

        for c in s1:
            freq[ord(c) - ord('a')] += 1

        l = 0
        r = l + n1 - 1

        while r < n2:
            temp = freq.copy()
            for i in range(l, r+1):
                temp[ord(s2[i]) - ord('a')] -= 1
            if temp == ([0] * 26):
                return True
            l += 1
            r += 1

        return False