N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

dp[1][0] = 0
for i in range(1, 10):  # 1부터 9까지는 각각 1개씩 존재
    dp[1][i] = 1


for i in range(1, N):
    for j in range(10):
        if j == 0 : # 0이면 앞으로 만 보내주고
            dp[i+1][1] += dp[i][0]
        elif j == 9 :   # 9라면 뒤로만 보내주고
            dp[i+1][8] += dp[i][9]  
        else:
            dp[i+1][j-1] += dp[i][j]    # 아니면 앞과 뒤로 분배
            dp[i+1][j+1] += dp[i][j]



print(sum(dp[N])%1000000000)

"""
9로 끝나면 0만 올수 있다
0으로 끝나면 1만 올수 있다
9, 0으로 끝나는 예외의 경우만 측정하면 됨
"""