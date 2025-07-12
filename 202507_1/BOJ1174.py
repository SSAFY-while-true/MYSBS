def find_num(n):
    if n <= 10:
        return n - 1
    elif n > 1023:  # total_num으로 찾은수
        return -1
    dp = [[0] * 10 for _ in range(11)]  # 총 10자리까지 [자리수][숫자]

    total_num = 10  # 총나올 수 있는 숫자 0~9 10개는 깔고간다

    for i in range(10):
        dp[1][i] = 1

    
    ans = ''    # 정답이 담길 숫자
    left_num = n - 10 # 이제 찾아야 할숫자가 몇번째 크기인지 판단할 숫자
    # 10개의 경우는 이미 위에서 측정해서 뺀다
    for i in range(2, 11):
        if ans:
            break
        for j in range(10):
            if ans:
                break
            for k in range(j):  # 여기서 0~j-1까지는 작은수니까 그 수만큼 더해준다
                dp[i][j] += dp[i - 1][k]

            total_num += dp[i][j]
            if total_num >= n:
                ans += str(j)
                digit = i - 1 #  남은 자리수 를 본다
                break
            else:   # 조건을 만족하지 않은경우에 크기를 줄여준다
                left_num -= dp[i][j]

    # 이제부터는 바로 전 행을 기준으로 남은 숫자만큼을 계속 찾아 줄것이다.
    while digit > 0:    # 남은 자리수가 없으면 끝내기
        if left_num != 0:
            for j in range(10):
                if left_num - dp[digit][j] < 0:
                    digit -= 1
                    ans += str(j)
                    break
                elif left_num - dp[digit][j] == 0:
                    digit -= 1
                    ans += str(j)
                    left_num = 0
                    break
                else:
                    left_num -= dp[digit][j]
        else:
            # 이제부터는 가장 크게 가면 되니까
            # 이전수 - 1 이 정답이 된다
            ans += str(int(ans[-1]) - 1)
            digit -= 1

    return int(ans)

N = int(input())

print(find_num(N))
