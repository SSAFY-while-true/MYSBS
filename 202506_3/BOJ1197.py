import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]

# 그래프 입력 받기
for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((c, b))
    adj_list[b].append((c, a))

visited = [False] * (V + 1)
hq = [(0, 1)]
total_cost = 0

while hq:
    cost, cur = heapq.heappop(hq)

    if visited[cur]:
        continue

    visited[cur] = True
    total_cost += cost

    for next_cost, next_node in adj_list[cur]:
        if not visited[next_node]:
            heapq.heappush(hq, (next_cost, next_node))

print(total_cost)
