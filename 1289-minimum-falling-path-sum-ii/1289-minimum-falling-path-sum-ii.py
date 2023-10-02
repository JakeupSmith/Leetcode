class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        DP = [[0 for _ in range(n)] for _ in range(n)]
        
        #initialize the first row of DP
        
        for j in range(n):
            DP[0][j] = grid[0][j]
        
        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    DP[i][j] = min(DP[i -1][1:]) + grid[i][j]
                elif j == n -1:
                    DP[i][j] = min(DP[i -1][:j]) + grid[i][j]
                else:
                    DP[i][j] = min(min(DP[i -1][:j]), min(DP[i-1][j+1:])) + grid[i][j]
        return min(DP[n-1])