class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dict = defaultdict(int)
        arr = []

        for i in nums:
            dict[i] += 1
        
        for key, value in dict.items():
            arr.append([value, key])
        arr.sort()

        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result