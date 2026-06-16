class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzero=1
        prev=1

        for num in nums:
            if num == 0:
                nonzero = prev
            else:
                nonzero = num * nonzero
            prev = num * prev
        
        # now prev = prod all nums and nonzero = all besides 0

        res = []
        for num in nums:
            if num == 0:
                res.append(nonzero)
            else:
                res.append(prev//num)
        
        return res