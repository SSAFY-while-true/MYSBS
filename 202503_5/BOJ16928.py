from collections import deque
import sys
input = sys.stdin.readline


def game_bfs(start):
    visited = [0] * 101
    queue = deque([start])
    visited[start] 

    while queue:
        cur = queue.popleft()

        for dice in range(1, 7):
            next_i = cur + dice

            if next_i == 100:
                return visited[cur] + 1

            elif next_i > 100:
                continue


            if game_map[next_i] != 0:
                next_i = game_map[next_i]

            if visited[next_i] == 0:
                visited[next_i] = visited[cur] + 1
                queue.append(next_i)


    return visited[100]

N, M = map(int, input().split())
game_map = [0] * 101

for _ in range(N + M):
    start, end = map(int, input().split())
    game_map[start] = end

print(game_bfs(1))
