n, m = map(int, input().split())
"""
파스칼 삼각형이다
"""
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(i + 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])