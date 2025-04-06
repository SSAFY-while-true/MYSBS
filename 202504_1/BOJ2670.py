import sys
input = sys.stdin.readline

N = int(input())
num_list = [float(input()) for _ in range(N)]
dp = num_list

for i in range(1, N):
    dp[i] = max(num_list[i], dp[i-1] * num_list[i])

print(f"{max(dp):.3f}")