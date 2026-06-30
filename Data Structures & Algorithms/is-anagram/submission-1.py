class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # countS, countT = defaultdict(int), defaultdict(int)
        # for i in range(len(s)):
        #     countS[s[i]] =   countS[s[i]] + 1
        #     countT[t[i]] =   countT[t[i]] + 1
        # return countS == countT

        if len(s) != len(t):
            return False
        A={} ; B={}
        for i in range(len(s)):
            A[s[i]] = A.get(s[i],0) + 1
            B[t[i]] = B.get(t[i],0) + 1
        return A==B

