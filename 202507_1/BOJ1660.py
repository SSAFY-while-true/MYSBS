N = int(input())

triangle = 1
tetrahedron = []
tetrahedron_num = 1

for triangle_num in range(2, 125):  # 사면체 숫자 찾기/ 항상 +1 볼꺼니까 여기서는 2부터 늘어나게 세팅
    triangle += triangle_num

    tetrahedron_num += triangle
    if tetrahedron_num > N:  #더 큰숫자는 필요없으니까 멈추기
            break
    tetrahedron.append(tetrahedron_num)


dp = [float('INF')] * (N + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    # 기본적으로 1 추가한다고 생각
    dp[i] = dp[i - 1] + 1
    for num in tetrahedron:
        if i >= num:
            # 현재 내값, 넘버만큼 뒤의 값 + 1 둘중에 최소로 갱신
            dp[i] = min(dp[i], dp[i - num] + 1)
        else:
            break
print(dp[N])