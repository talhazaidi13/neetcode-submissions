class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2

        def divide(merged):
            if len(merged)<=1:
                return merged
            n = len(merged)//2
            left = divide(merged[:n])
            right = divide(merged[n:])
            return conqer (left, right)
        
        def conqer(l, r):
            i=0; j=0 ; res=[]
            while i < len(l) and j< len(r):
                # print("i,j, l,r", [i, j, l, r])
                if l[i] <= r[j]:
                    res.append(l[i])
                    i=i+1
                else:
                    res.append(r[j])
                    j=j+1
            res.extend(l[i:])
            res.extend(r[j:])
            return res

        sortarr = divide(merged)
        print(sortarr)
        n = len(sortarr)
        if n%2==0:
            mid = n//2
            return  (sortarr[mid-1] + sortarr[mid])/2
        else:
            mid = n//2
            return  sortarr[mid]
            

            