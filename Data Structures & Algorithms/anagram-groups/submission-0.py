class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test =  {}
        for s in strs:
            sort=''.join(sorted(s))
            if sort not in test:
                  test[sort] = []
            test[sort].append(s)
        return list(test.values())