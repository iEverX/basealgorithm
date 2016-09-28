# n for floors left and k for eggs left
def drop(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, k + 1):
        dp[0][k] = 0
    for i in range(n + 1):
        dp[i][1] = i
    
    for i in range(1, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = 1 + min(max(dp[x - 1][j - 1], dp[i - x][j]) for x in range(1, i + 1))

    return dp[n][k]


print(drop(10, 2))
print(drop(10, 3))
print(drop(100, 2))