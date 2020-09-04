# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# RELATED TOPICS: Graph Traversal
# APPROACH: We need to traverse the above matrix and find out how many connected lands can be formed
# Lets do it using dfs and try to count how many lands are connected and form island Don't forget to mark the visited land

class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or row == len(grid):
            return
        
        if col < 0 or col >= len(grid[0]):
            return
        
        if grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row - 1 , col)
        self.dfs(grid, row + 1 , col)
        
        
    def numIslands(self, grid):
        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)
        return count


