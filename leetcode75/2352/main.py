def equalPairs(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)

    columnGrid = [[] for _ in range(n)]

    i, j = 0, 0
    while j < n:
        while i < n:
            columnGrid[j].append(grid[i][j])
            i += 1
        j += 1
        i = 0
