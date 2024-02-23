class Solution(object):

    def uniquePaths(self,grid):

        M,N = len(grid),len(grid[0])
        dp = [0]*N
        dp[N-1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]==1:
                    dp[c] = 0
                elif c+1<N:
                    dp[c] = dp[c]+dp[c+1]
        return dp[0]

