class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res=1
        for x in nums:
            res*=x
        if res>0:
            return 1
        elif res<0:
            return -1
        return 0
