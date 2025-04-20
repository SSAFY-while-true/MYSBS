N = int(input())
soldier = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)
result = N - max(dp)
print(result)
