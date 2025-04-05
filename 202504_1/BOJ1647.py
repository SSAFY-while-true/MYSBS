import sys
input = sys.stdin.readline

import heapq

def prim(start = 1):
    pq = [(0, start)]
    visited = [False] * (N + 1)
    key = [float('inf')] * (N + 1)
    total_cost = 0
    max_cost = 0    # 이 문제는 두마을로 쪼개야해서 가장 비싼 간선을 끊고 마을을 2개로 나눈다.
    
    while pq:
        cur_cost, cur_i = heapq.heappop(pq)
        if visited[cur_i]:
            continue
        visited[cur_i] = True
        total_cost += cur_cost
        max_cost = max(max_cost, cur_cost)

        for next_cost, next_i in adj_list[cur_i]:
            if not visited[next_i] and next_cost < key[next_i]:
                key[next_i] = next_cost
                heapq.heappush(pq, (next_cost, next_i))

    return total_cost - max_cost

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for i in range(M):
    house_a, house_b, cost = map(int, input().split())
    adj_list[house_a].append((cost, house_b))
    adj_list[house_b].append((cost, house_a))


print(prim())