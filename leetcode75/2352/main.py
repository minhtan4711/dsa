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
    pair_count = 0
    for i in range(n):
        for j in range(n):
            if grid[i] == columnGrid[j]:
                pair_count += 1
    return pair_count
