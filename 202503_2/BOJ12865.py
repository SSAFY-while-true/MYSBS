import sys
input = sys.stdin.readline

N, V = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (V + 1)


for items in bag:
    now_w = items[0]
    now_v = items[1]
    for i in range(V, now_w - 1, -1):
        dp[i] = max(dp[i], dp[i - now_w] + now_v)


print(max(dp))