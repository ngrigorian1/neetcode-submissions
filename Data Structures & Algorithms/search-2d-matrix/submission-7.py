class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) -1
        mid=0
        while (l <= r):
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][0] and target > matrix[mid][-1]:
                print(f"l={l} and r={r}")
                l = mid + 1
                print(f"l={l} and r={r} and {l <= r}")
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                return False
        if l > r:
            return False
        print(f"{target} > {matrix[mid][0]} and {target} > {matrix[mid][-1]}")
        print(mid)
        l=0
        r=len(matrix[mid])
        while(l <= r):
            mid2 = (l+r)//2
            if target == matrix[mid][mid2]:
                return True
            if target > matrix[mid][mid2]:
                l = mid2 + 1
            elif target < matrix[mid][mid2]:
                r = mid2 -1
        return False
            
