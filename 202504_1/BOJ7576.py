import sys
input = sys.stdin.readline

import heapq

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
pq = []

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            visited[i][j] = True
            heapq.heappush(pq, (0, i, j))
        elif tomato_box[i][j] == -1:
            visited[i][j] = True

d_day = 0
while pq:
    plus_day, cur_i, cur_j = heapq.heappop(pq)
    d_day = plus_day

    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
        next_i = cur_i + dir[0]
        next_j = cur_j + dir[1]

        if 0 <= next_i < N and 0 <= next_j < M:
            if not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                next_day = plus_day + 1
                heapq.heappush(pq, (next_day, next_i, next_j))

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            d_day = -1
            break

print(d_day)



