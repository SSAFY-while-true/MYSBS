from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
mirro = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

start_i = -1
for i in range(n):
    for j in range(m):
        if mirro[i][j] == 2:
            start_i, start_j = i, j
            visited[i][j] = 0
            break
    if start_i > -1:
        break

queue = deque([(start_i, start_j)])

while queue:
    cur_i, cur_j = queue.popleft()
    for dir in  [(1,0),(-1,0),(0,1),(0,-1)]:
        ni = cur_i + dir[0]
        nj = cur_j + dir[1]

        if 0 <= ni < n and 0 <= nj < m:
            if mirro[ni][nj] == 1 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[cur_i][cur_j] + 1
                queue.append((ni, nj))


for i in range(n):
    for j in range(m):
        if mirro[i][j] == 0:
            visited[i][j] = 0
    print(*visited[i])