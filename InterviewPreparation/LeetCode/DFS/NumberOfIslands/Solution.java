package interview_preparation.LeetCode.DFS.NumberOfIslands;

class Solution {
    private int n;
    private int m;

    private void sink(char[][] grid, int i, int j) {
        // if we are out of bounds or on a '0', no need to DFS down this path anymore
        if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') {
            return;
        }

        // make sure we dont check this spot again
        grid[i][j] = '0';

        // all possible path we can DFS to from here ...
        sink(grid, i + 1, j);
        sink(grid, i - 1, j);
        sink(grid, i, j + 1);
        sink(grid, i, j - 1);
    }

    public int numIslands(char[][] grid) {
        // the solution counter we'll eventually add to
        int count = 0;

        // get the size of the matrix
        n = grid.length;
        if (n == 0) {
            return 0;
        }

        m = grid[0].length;

        // go through the entire matrix of DFS when we see a '1'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    sink(grid, i, j);
                    ++count;
                }
            }
            return count;
        }

        return count;
    }
}