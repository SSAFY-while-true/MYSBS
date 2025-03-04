from collections import deque
import sys
input = sys.stdin.readline


def my_BFS(i, j):
    queue = deque([i])
    visited = [[0] * N for _ in range(N)]

    while queue:
        current_i = queue.popleft()

        for next_i in range(N):
            if adj_matrix[current_i][next_i] == 1 and visited[next_i][current_i] == 0:
                if next_i == j:
                    return True
                visited[next_i][current_i] = 1
                queue.append(next_i)
    return False

N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if result[i][j] == 0:
            if my_BFS(i,j):
                result[i][j] = 1

for idx in range(N):
    print(*result[idx])
