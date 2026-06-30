class Solution:
    def isHappy(self, n: int) -> bool:
        visit = []
        
        while n not in visit:
            visit.append(n)
            n = self.sumofsq(n)
            if n==1:
                return True
        return False

    def sumofsq(self, n):
        sum1 = 0
        while n:
            tmp = n%10
            square = tmp * tmp
            sum1+=square
            n = n//10
        return sum1