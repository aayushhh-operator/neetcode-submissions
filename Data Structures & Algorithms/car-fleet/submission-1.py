class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        times = []
        stack = []

        for i in range(len(position)):
            arr.append([position[i], speed[i]])

        arr.sort(key = lambda x:x[0], reverse=True)
        
        for i in range(len(arr)):
            time = (target-arr[i][0])/arr[i][1]
            times.append(time)

        for i in range(len(times)):
            if stack and stack[-1] >= times[i]:
                continue
            stack.append(times[i])

        return len(stack)