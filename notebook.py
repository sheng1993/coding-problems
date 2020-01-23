from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        _m = 0
        for _n in range(n):
            while nums2[_n] > nums1[_m] and _m < m:
                _m += 1
            
            # shift all elements
            aux = nums1[_m]
            for i in range(_m, m):
                nums1[i + 1], aux = aux, nums1[i + 1]
            m += 1
            nums1[_m] = nums2[_n]


s = Solution()
arg1 = [1,2,3,0,0,0]
arg2 = [2,5,6]
s.merge(arg1, 3, arg2, 3)
assert arg1 == [1,2,2,3,5,6]

arg1 = [0]
arg2 = [1]
s.merge(arg1, 0, arg2, 1)
assert arg1 == [1]