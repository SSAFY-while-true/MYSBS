import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for today in range(1, N + 1):
    take_time, pay = schedule[today -1]

    if today - 1 + take_time <= N:
        dp[today - 1 + take_time] = max(dp[today - 1 + take_time], dp[today -1] + pay)

    dp[today] = max(dp[today-1], dp[today])


print(max(dp))