class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = str()
        i,j = len(a) -1, len(b)-1
        carry = 0
        while i>=0 or j >=0 or carry != 0:
            c = carry
            c += (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0)
            i-= 1
            j-=1

            carry = c // 2
            res += str(c%2)            

        return res[::-1]


for _ in [
    ["11", "1"],
    ["1010", "1011"]
]:
    print(
        Solution().addBinary(
            _[0], _[1]
        )
    )
    