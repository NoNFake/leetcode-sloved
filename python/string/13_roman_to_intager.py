class Solution:
    def romanToInt(self, s: str) -> int:
        # d = {
        #     1: "I",
        #     2: "II",
        #     3: "III",
        #     4: "IV",

        #     5: "V",
        #     6: "VI",
        #     7: "VII",
        #     8: "VIII",
        #     9: "IX",

        #     10: "X"
        # }

        dv = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10
        }

        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500,
            'M': 1000
        }

        t = 0
        n = len(s)

        for i in range(n):
            current = d[s[i]]
            print(current)
            if i+1 < n and current < d[s[i+1]]:
                t -= current
            else:
                t += current
        # print(t)
        return t
        # for i,x in enumerate(d):
        #     if d[x] in s:
        #         print(i)
        # print(d['III'])

print(
    Solution().romanToInt(
        s="XII"
    )
)