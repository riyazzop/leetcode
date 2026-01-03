class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i<len(nums1):
            res.extend(nums1[i:])
        if j<len(nums2):
            res.extend(nums2[j:])
        reslen=len(res)
        if reslen%2==1:
            return res[reslen//2]
        return (res[reslen//2]+res[(reslen//2)-1])/2.0