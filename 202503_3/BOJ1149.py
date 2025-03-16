import sys
input = sys.stdin.readline

N= int(input())
street = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = street[0]

for i in range(1, N):
    dp[i][0] = street[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = street[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = street[i][2] + min(dp[i-1][0], dp[i-1][1])


print(min(dp[-1]))