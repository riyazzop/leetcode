class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res=[0]*len(arr)
        greater=-1
        for i in range(len(arr)-1,-1,-1):
            res[i]=greater
            greater=max(greater,arr[i])
        return res