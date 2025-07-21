def cost(cur, next):
    if cur == next:
        return 1
    elif cur == 0:  # 중앙
        return 2
    elif abs(cur - next) == 2:  # 대각선
        return 4
    else:
        return 3

command = list(map(int, input().split()))
n = len(command)

# 선택해야 하는 것 오른발? 왼발?
dp = [[[float('INF') for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]

dp[0][0][0] = 0

for i in range(n):
    next_step = command[i]
    for left in range(5):
        for right in range(5):
            # 같으면 계산하지 않음
            if dp[i][left][right] == float('INF'):
                continue
            
            if left != next_step:
                dp[i + 1][left][next_step] = min(dp[i + 1][left][next_step], dp[i][left][right] + cost(right, next_step))

            if right != next_step:
                dp[i + 1][next_step][right] = min(dp[i + 1][next_step][right], dp[i][left][right] + cost(left, next_step))

print(min(min(dp[n-1])))