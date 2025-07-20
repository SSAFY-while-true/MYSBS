H, W = map(int, input().split())
world = list(map(int, input().split()))

total_water = 0
temp_water = 0
now_height = world[0]
max_idx = 0
for idx in range(1, W):
    
    # 크거나 같을 경우는 현재를 바꿔준다.
    if now_height <= world[idx]:
        total_water += temp_water
        temp_water = 0
        now_height = world[idx]
        max_idx = idx
    # 작을 경우는 임시 빗물에 넣어놓는다
    else:
        temp_water += now_height - world[idx]

# 이제는 오른쪽에서 한번 max_idx 까지 확인하면 쓸어온다
now_height = world[-1]
for idx in range(W-1, max_idx-1, -1):
    
    # 크거나 같을 경우는 현재를 바꿔준다.
    if now_height <= world[idx]:
        now_height = world[idx]
    # 이번에는 바로 결과에 넣는다
    else:
        total_water += now_height - world[idx]

print(total_water)