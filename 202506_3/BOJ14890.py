def is_fly(arr):
    now_num = arr[0]
    temp_count = 0
    i= 0

    while i < N:
        if abs(now_num - arr[i]) >= 2:
            return 0
        

        if now_num == arr[i]:   # 그대로면 카운트만 측정
            temp_count += 1
            i += 1
        elif now_num < arr[i]:  # 높아지면
            if temp_count < X :
                return 0
            now_num = arr[i]
            temp_count = 1
            i += 1

        else:                   # 낮아지면
            if i + X - 1 < N :
                for add_i in range(1, X):
                    if arr[i] != arr[i + add_i]:
                        return 0
                i = i + X - 1
                now_num = arr[i]
                temp_count = -1
    
            else:
                return 0
    return 1


N, X = map(int, input().split())
airstrip = [list(map(int, input().split())) for _ in range(N)]
airstrip_col = list(map(list, zip(*airstrip)))

result = 0

for i in range(N):
    result += is_fly(airstrip[i])
    result += is_fly(airstrip_col[i])


print(result)

