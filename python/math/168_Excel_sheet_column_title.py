class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        df = []
        
        while columnNumber > 0:
            columnNumber -= 1
            d = columnNumber % 26
            df.append(chr(65 + d))
            columnNumber//=26

        return "".join(df[::-1])




        # if columnNumber > 26:
        #     c = columnNumber // 26
        #     g = columnNumber % 26
        #     print(f"c: {c} | g: {g}")
            
        #     df  = dd[c-27] + dd[g]


        # else:
        #     df = dd[columnNumber -1 ]
        # return df




# for _ in range(2147483647):
#     print(_)
#     print(
#         Solution().convertToTitle(
#             _
#         )
#     )


for _ in [
    # 1,
    # 2,
    27, 
    # 28,
    701,
    # 2147483647
]:
    print(
        Solution().convertToTitle(
            _
        )
    )