class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sarr = nums1 + nums2
        sarr.sort()
        result = 0
        idx = 0

        if len(sarr) % 2 != 0:
            idx = len(sarr) // 2
            result = sarr[idx]
            return result

        else:
            idx = len(sarr) // 2
            result = sarr[idx] + sarr[idx -1]
            result /= 2
            return result
