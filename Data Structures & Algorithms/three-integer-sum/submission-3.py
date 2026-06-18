class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        seen = set()
        res = []

        nums = sorted(nums)

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                triplet = tuple([nums[i], nums[left], nums[right]])
                if s == 0 and triplet not in seen:
                    seen.add(triplet)
                    res.append([nums[i], nums[left], nums[right]])
                elif s > 0: 
                    right -= 1
                else:
                    left += 1
        return res

# -1, -1, 0, 1, 1
