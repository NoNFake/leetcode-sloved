class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dd = {chr(i): i - 65 for i in range(65, 91)}
        f = 0
        for i, x in enumerate(columnTitle[::-1]):
            f += (dd[x] +1) * (26**i)
        return f
        print(f)


for _ in [
    # "A",
    # "AB",
    "ZY"

]:
    print(
        Solution().titleToNumber(
            _
        )
    )