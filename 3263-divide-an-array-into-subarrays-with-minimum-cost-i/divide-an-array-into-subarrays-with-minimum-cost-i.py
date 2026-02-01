class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fmin=smin=float('inf')
        for num in nums[1:]:
            if num<fmin:
                smin=fmin
                fmin=num
            elif num<smin:
                smin=num
        print(fmin,smin)
        return nums[0]+fmin+smin