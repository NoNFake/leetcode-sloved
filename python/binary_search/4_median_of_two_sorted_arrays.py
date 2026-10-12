class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = nums1 + nums2
        m.sort()
        s = len(m)
        if s % 2 == 0:
            d = s // 2
            m_1 = m[d-1]
            m_2 = m[d]

            return (m_1 + m_2) / 2 
        else: 
            d = s // 2
            return m[d]