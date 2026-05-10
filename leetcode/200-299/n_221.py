"""
221. 最大正方形
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        if rows == 0 or columns == 0:
            return 0
        
        maxSide = 0

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '0':
                    continue
                maxSide = max(maxSide, 1)
                currentMaxSide = min(rows - i, columns - j)
                for k in range(1, currentMaxSide):
                    flag = True
                    if matrix[i + k][j + k] == '0':
                        break
                    for m in range(k):
                        if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                            flag = False
                            break
                    if flag:
                        maxSide = max(maxSide, k + 1)
                    else:
                        break

        return maxSide ** 2
    
    def method(self, matrix):
        m, n = len(matrix), len(matrix[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, ch in enumerate(row):
                if ch == '1':
                    f[i + 1][j + 1] = min(f[i][j], f[i][j + 1], f[i + 1][j]) + 1

        return max(map(max, f)) ** 2
                    



        

