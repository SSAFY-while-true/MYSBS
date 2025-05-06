import sys
input = sys.stdin.readline

n = int(input())
pascal = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = pascal[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j > 0 and j != i:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + pascal[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + pascal[i][j]
        else:
            dp[i][j] = dp[i-1][j] + pascal[i][j]

print(max(dp[-1]))