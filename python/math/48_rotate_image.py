class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d = len(matrix)
        for  i in range(d):
            for  j in range(i + 1, d):
            # matrix[i]
                print(f"{i} | {j}")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # print(matrix)
        for row in matrix:
            row.reverse()

        print(matrix)
            # for i, j, k in matrix[::-1]: m[1].append(j)
            # for i, j, k in matrix[::-1]: m[2].append(k)

     


        
        
        # print(m)

for _ in [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
]:
    print(
        Solution().rotate(
            matrix=_
        )
    )