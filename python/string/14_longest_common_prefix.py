class Solution:
    def longestCommonPrefix(self, strs:     
        list[str]) -> str:
        pref = strs[0]
        for s in strs[1:]:
            # print(s)
            while not s.startswith(pref):
                pref = pref[:-1]
                # print(pref)
        return pref
