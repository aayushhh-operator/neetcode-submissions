class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        if int(len(s)) != int(len(t)):
            return False

        for i in range(int(len(s))):
            if s[i] in dic1:
                dic1[s[i]] = dic1[s[i]] + 1
            else:
                dic1[s[i]] = 1

            if t[i] in dic2:
                dic2[t[i]] = dic2[t[i]] + 1
            else:
                dic2[t[i]] = 1
        
        if dic1.keys() != dic2.keys():
            return False

        for key in dic1:
            if dic1[key] == dic2[key]:
                continue
            else:
                return False
        return True
