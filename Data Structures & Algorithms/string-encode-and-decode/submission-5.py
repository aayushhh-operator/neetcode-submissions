class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        i = 1
        for s in strs:
            string += s
            string += "😀"
            i += 1

        return string

    def decode(self, s: str) -> List[str]:
        result = []
        count = 1
        string = str()
        for i in range(len(s)):
            if s[i] != "😀":
                string += str(s[i])
            else:
                result.append(string)
                count += 1
                string = ""

        return result