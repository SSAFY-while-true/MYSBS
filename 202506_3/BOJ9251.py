words_a = list(input())
words_b = list(input())

len_a = len(words_a)
len_b = len(words_b)

dp = [[0] * (len_b+1) for _ in range(len_a + 1)]
for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if words_a[i-1] == words_b[j-1]:    # 하나씩 미뤘으니까 -1씩해줌
            dp[i][j] = dp[i-1][j-1] + 1     # 겹쳤다면 해당되지않은 곳에서 +1 좌상단
        else:
            if dp[i-1][j] > dp[i][j-1] :    # 안겹쳤으면 이전픽 혹은 안픽 중에 더 큰거 dp에 채워넣기
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[-1][-1])