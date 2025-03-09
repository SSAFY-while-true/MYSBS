from collections import deque

def wall_BFS(maze):

    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0,0,1)])
    visited[0][0][1] = 1

    
    while queue:
        cur_i, cur_j, chance = queue.popleft()

        if cur_i == N - 1 and cur_j == M - 1:
            return visited[cur_i][cur_j][chance]
        
        for dir in range(4):
            ni = cur_i + di[dir]
            nj = cur_j + dj[dir]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == 0 and visited[ni][nj][chance] == 0:
                    visited[ni][nj][chance] = visited[cur_i][cur_j][chance] + 1
                    queue.append((ni, nj, chance))

                elif maze[ni][nj] == 1 and chance == 1 and visited[ni][nj][0] == 0:
                    visited[ni][nj][0] = visited[cur_i][cur_j][chance] + 1
                    queue.append((ni, nj, 0))
                    
    return -1


                        
                



N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]


print(wall_BFS(maze))