T = int(input())

for tc in range(1, T+1):
    N = int(input())

    dp = [1] * (N + 1)
    for i in range(4, N + 1):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[N])