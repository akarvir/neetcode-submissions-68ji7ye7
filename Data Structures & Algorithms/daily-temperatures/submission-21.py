class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result=[0]*n
        stack = []
        # stack shall be monotonically decreasing all times, so peek
        for i in range(n):
            if stack and temperatures[i] > stack[-1][1]:
                while stack and stack[-1][1] < temperatures[i]:
                    index, val = stack.pop()
                    result[index] = i-index
            stack.append((i,temperatures[i]))
        return result
            
            
