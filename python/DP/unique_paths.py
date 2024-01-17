# input: m = 3, n = 7
# output: 28

# top-down
def uniquePaths(m, n):
    memo = [[-1] * n for _ in range(m)]

    def dfs(r, c):
        unique_paths = 0
        if r == 0 and c == 0:
            memo[r][c] = 1
            return memo[r][c]

        if memo[r][c] == -1:
            if r-1 >= 0:
                unique_paths += dfs(r-1, c)
            if c-1 >= 0:
                unique_paths += dfs(r, c-1)
            memo[r][c] = unique_paths

        return memo[r][c]
    return print(dfs(m-1, n-1))


uniquePaths(3, 7)
# bottom-up -> 테이블을 채워나간다, dp table


def uniquePaths2(m, n):
    memo = [[-1] * n for _ in range(m)]
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    print(memo)
    return memo[m-1][n-1]


uniquePaths2(3, 7)
