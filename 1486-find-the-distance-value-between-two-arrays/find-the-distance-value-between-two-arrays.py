class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        l = 0
        for i in range(len(arr1)):
            valid = True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    valid = False
                    break
            if valid:
                l += 1
        return l
