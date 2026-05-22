class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        result=False
        for i in nums:
            if i not in map:
                map[i]=1
            else:
                map[i]+=1
                result=True
        return result