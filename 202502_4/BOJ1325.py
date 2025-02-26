from collections import deque
import sys

input = sys.stdin.readline


def BFS_computer(start_num):
    queue = deque([start_num])
    visited = [0] * (N + 1)
    visited[start_num] = 1
    hack_com = 1

    while queue:
        current_com = queue.popleft()

        for next_com in adj_list[current_com]:
            if visited[next_com] == 0:
                visited[next_com] = 1
                hack_com += 1
                queue.append(next_com)

    return hack_com


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

max_hack = 0
result = []

for i in range(M):
    computer_A, computer_B = map(int, input().split())
    adj_list[computer_B].append(computer_A)

for num in range(1,N+1):
    if not adj_list[num]:
        continue
    temp_hack = BFS_computer(num)
    if temp_hack > max_hack:
        max_hack = temp_hack
        result = [num]
    elif temp_hack == max_hack:
        result.append(num)

print(*result)



