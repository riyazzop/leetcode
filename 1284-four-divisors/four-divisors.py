class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total=0
        # for num in nums:
        #     divisers=[]
        #     for i in range(1,int(sqrt(num+1))+1):
        #         if len(divisers)>4:
        #             break
        #         if num%i==0:
        #             divisers.append(i)
        #             if i!=num//i:
        #                 divisers.append(num//i)
        #     if len(divisers)==4:
        #         total+=sum(divisers)
        # return total 

        total=0
        for num in nums:
            divisers=[]
            for i in range(1,int(sqrt(num))+1):
                if len(divisers)>4:
                    break
                if num%i==0:
                    divisers.append(i)
                    otherdiviser=num//i
                    if i!=otherdiviser:
                        divisers.append(otherdiviser)
            if len(divisers)==4:
                total+=sum(divisers)
        return total
