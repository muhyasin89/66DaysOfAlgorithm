class Solution:
    def dfs(self, i, j, m, n, grid):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(i - 1, j, m, n, grid)
        self.dfs(i, j - 1, m, n, grid)
        self.dfs(i + 1, j, m, n, grid)
        self.dfs(i, j + 1, m, n, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i, j, len(grid), len(grid[0]), grid)
        return cnt
