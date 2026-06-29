class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstr = ''
        # for i in s:
        #     if i.isalnum():
        #         newstr = newstr + i.lower()
        # return newstr == newstr[::-1]

        l=0
        r=len(s) - 1
        while l<r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower()!=s[r].lower():
                    return False
                l=l+1
                r=r-1
            elif s[l].isalnum():
                r-=1
            else:
                l+=1

        return True