def dfs(i, j, n, m, grid, visited):
    count = 0
    if 0 <= i < n and 0 <= j < m and grid[i][j] == "." and not visited[i][j]:
        visited[i][j] = True
        count = 1 + dfs(i - 1, j, n, m, grid, visited) + dfs(i + 1, j, n, m, grid, visited) + dfs(i, j - 1, n, m, grid, visited) + dfs(i, j + 1, n, m, grid, visited)
    return count


def largest_connected_dots(n, grid):
    m = len(grid[0])
    max_dots = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                visited = [[False for j in range(m)] for i in range(n)]
                max_dots = max(max_dots, dfs(i, j, n, m, grid, visited))
    return max_dots


n = int(input())
grid = [input().split() for _ in range(n)]

print(largest_connected_dots(n, grid))
