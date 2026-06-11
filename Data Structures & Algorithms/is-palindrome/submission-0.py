class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in s:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
                string.append(c.lower())

        n = len(string)

        for i in range(int(n/1)):
            if string[i] != string[n-i-1]:
                return False

        return True