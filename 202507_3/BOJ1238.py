import heapq
import sys
input = sys.stdin.readline


def dijkstra(start, target):
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if node == target:
            return curr_dist
        
        if distance[node] < curr_dist:
            continue
        for edge_cost, adj_node in adj_list[node]:
            new_dist = curr_dist + edge_cost
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                heapq.heappush(pq, (new_dist, adj_node))

    return distance

def dijkstra2(start):
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)
    
        if distance[node] < curr_dist:
            continue
        for edge_cost, adj_node in adj_list[node]:
            new_dist = curr_dist + edge_cost
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                heapq.heappush(pq, (new_dist, adj_node))

    return distance


N, M, X = map(int,input().split()) # N: 노드 개수 M: 간선수 X: 목표도시

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((c, b))

## 목표가 2라면 1-> 2가기 스타트 노드를 1로해å서 결과[2]확인
## 이제 2에서 2 다시 와야하니까 이건 스타트 노드 2[1] 이 두개 더한것의 맥스를 구하면 되나?

result = 0
costs = dijkstra2(X)
for i in range(1, N+ 1):
    if i != X:
        result = max(dijkstra(i, X) + costs[i], result)
print(result)   # 되네
