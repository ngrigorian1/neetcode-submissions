class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # sort -> count
        # 2 20 4 10 3 4 5
        # 2 3 4 4 5 10 20
        # [2 3 4 5]
        # not efficient n^2 log n

        # 2 20 4 3 -> convert to set

        # 4 3 20 2

        # 4-1 in set? yes
        # add and skip
        # 3-1 in set? yes
        # skip
        # 20 -1 in set? no
        # this is a starter number -> make set -> look for 20+1? no. done save len of set
        # 2-1 in set? no: starter num
        #     2 -> 2+1 in set? yes -> 3+ 1 in set? yes -> 4+1 in set? no stop. len save compare to max

        s = set(nums)
        longest = 0

        for num in nums:
            if num-1 in s:
                continue
            # starter num:
            length = 1
            prev = num
            while(prev+1 in s):
                print(prev+1)
                length += 1
                prev += 1
            
            if length > longest:
                longest = length
        
        return longest
            




        

