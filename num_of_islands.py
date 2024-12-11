# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#       0   1   2   3   4
#   0 ["1","1","1","1","0"],
#   1 ["1","1","0","1","0"],
#   2 ["1","1","0","0","0"],
#   3 ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# - m == grid.length
# - n == grid[i].length
# - 1 <= m, n <= 300
# - grid[i][j] is '0' or '1'.
# We need a dfs function:

def numIslands(grid):
    # Total number of islands.
    islandCount = 0
    # Define number of rows as length of the gird.
    rows = len(grid)
    # Define number of columns as length of the first row.
    cols = len(grid[0])

    def dfs(i, j):
        if i < 0 or  j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = 'v'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    # Loop over the grid.
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                print(islandCount)
                islandCount += 1
                dfs(i, j)

    return print(islandCount)



grid_1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["1","0","0","1","1"]
]

grid_2 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","0"]
]

numIslands(grid_1)
numIslands(grid_2)
