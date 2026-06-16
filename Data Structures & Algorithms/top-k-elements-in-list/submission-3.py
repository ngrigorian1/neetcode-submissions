class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1, 2, 2, 2, 3, 3

        # 1 : 1
        # 2 : 3
        # 3 : 2

        # b =[] [1][3][2] [] [] []
        # i = 0  1  2  3  4  5  6

        # ^ iterate backwards until res list len = k

        d = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            d[num] = d.get(num, 0) + 1
        for key, v in d.items():
            buckets[v].append(key)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
            if k == 0:
                return res
            
            


