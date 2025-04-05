from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

house_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house_list.append((i, j))
        elif city_map[i][j] == 2:
            chicken_list.append((i, j))


min_result = float('inf')

for test_case in combinations(range(len(chicken_list)), M):
    selected_chickens = [chicken_list[x] for x in test_case]
    temp_min = 0

    for start_i, start_j in house_list:
        if min_result <= temp_min:
            break
        house_chicken_dist = abs(start_i - selected_chickens[0][0]) + abs(start_j - selected_chickens[0][1])
        for idx in range(1, M):
            house_chicken_dist = min(house_chicken_dist, abs(start_i - selected_chickens[idx][0]) + abs(start_j - selected_chickens[idx][1]))

        temp_min += house_chicken_dist
        
    else:
        min_result = min(temp_min, min_result)   ## << 이상황 궁금하긴함.. 저기서 break에 안걸리면 무조건 최소니까 내려온건데 왜 여기서 값을 확인할 때마다 min을 해야하는거지?

print(min_result)