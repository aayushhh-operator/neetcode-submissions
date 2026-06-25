from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        strings = []

        for i in range(len(s)):
            if s[i] in freq:
                temp = freq.copy()

                for j in range(i, len(s)):
                    if s[j] in temp and temp[s[j]] > 0:
                        temp[s[j]] -= 1

                        if all(v == 0 for v in temp.values()):
                            strings.append(s[i:j+1])
                            break

        if not strings:
            return ""

        word = strings[0]

        for string in strings:
            if len(string) < len(word):
                word = string

        return word