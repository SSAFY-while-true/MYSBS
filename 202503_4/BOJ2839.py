N = int(input())

dp = [N + 1] * (N+1)
dp[0] = 0


for i in range(3, N + 1, 3):
    dp[i] = dp [i -3] + 1

for i in range(5, N + 1):
    dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[N] == N + 1:
    dp[N] = -1

print(dp[N])

