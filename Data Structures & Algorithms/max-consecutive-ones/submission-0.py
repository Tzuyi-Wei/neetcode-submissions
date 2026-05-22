class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total=0
        maxtotal=0
        for i in nums:
            if i==1:
                total+=1
            else:
                total=0
            if total > maxtotal:
                maxtotal=total
        return maxtotal
                