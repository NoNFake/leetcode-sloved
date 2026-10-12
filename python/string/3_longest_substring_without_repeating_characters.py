class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        seen = {}
        ans = left= 0

        for right, x in enumerate(s):
            if x in seen and seen[x] >= left:
                left = seen[x] +1

            seen[x] = right

            # print(seen)
            ans =max(ans, right - left+1)
        return ans