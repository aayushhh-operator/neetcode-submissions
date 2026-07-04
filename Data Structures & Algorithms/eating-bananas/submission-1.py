import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        m = max(piles)

        l, r = 1, m

        while l<=r:
            t = 0
            mid = int((l+r)/2)

            for i in range(len(piles)):
                t+=(math.ceil(piles[i]/mid))
            
            if t<=h:
                k = mid
                r = mid-1
            elif t > h:
                l = mid+1

        return k