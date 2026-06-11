class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        output = []
        flag = 0

        for i in nums:
            if i != 0:
                sum = sum*i
            else:
                flag += 1

        for i in nums:
            if i != 0:
                if flag == 0:
                    output.append(int(sum/i))
                else:
                    output.append(0)
            else:
                if flag > 1:
                    output.append(0)
                else:
                    output.append(int(sum))

        return output