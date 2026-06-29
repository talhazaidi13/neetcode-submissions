class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            j = i+1; days=0
            if j<len(temperatures) and (temperatures[i] < temperatures[j]) :
                    days = days+1
            else:
                # days=0 
                while j<len(temperatures) and temperatures[i] >= temperatures[j]:
                    j=j+1
                    if j < len(temperatures):
                       days = j-i
                    else:
                        days=0
                    
            result.append(days) 
        return result   