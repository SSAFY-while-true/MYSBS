n = int(input())

dp = [float('inf')] * (n + 1)
if n >= 5:
    dp[5] = 1
if n >= 4:
    dp[4] = 2
if n >= 2:
    dp[2] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1


if dp[n] == float('inf'):
    print(-1)
else:
    print(dp[n])