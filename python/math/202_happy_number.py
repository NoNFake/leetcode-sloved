class Solution:
    def isHappy(self, n: int) -> bool:
        MAX_NUM = 2**31-1
        # MAX_NUM = 2*2
        # if n 
        r = str(n)
        seen = []
        while r != '1' and int(r) < MAX_NUM:
            o = 0
            for i in r:
                o += int(i)**2
                if str(o) in seen:
                    return False
                # print(f"o:: {o}")
            r = str(o)
            seen.append(r)
            # print(seen)
            # print(f"r: {r} | o: {o}")
            # break

        return True if r == '1' else False 





for _ in [
    1,
    2,
    17,
    19

]:
    print(
        Solution().isHappy(
            _
        )
    )