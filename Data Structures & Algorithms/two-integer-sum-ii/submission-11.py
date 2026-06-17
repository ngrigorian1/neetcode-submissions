class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while (right < len(numbers)):
            add = numbers[left] + numbers[right]
            print(add)
            if add == target:
                return [left+1, right+1]
            elif add < target:
                right += 1
                left += 1
            else:
                left -= 1
        