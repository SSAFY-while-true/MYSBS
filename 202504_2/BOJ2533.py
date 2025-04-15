import sys
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj_list[u].append(v)       # 일방으로 하는게 포인트!!

dp = [[0, 0] for _ in range(N + 1)]

dp[1][0] = 0
dp[1][1] = 1

