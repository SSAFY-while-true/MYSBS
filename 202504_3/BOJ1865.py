import sys   
input = sys.stdin.readline


T = int(input())

for tc in range(1,T+1):
    N, M, W = map(int, input().split())
    road_adj = [[] for _ in range(N + 1)]
    worm_adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        road_adj[S].append((E, T))
        road_adj[E].append((S, T))


    for _ in range(W):
        S, E, T = map(int, input().split())
        worm_adj[S].append((E, -T))

    dist = [0] * (N + 1)
    negative_cycle = False

    for _ in range(1, N):
        updated = False
        for u in range(1, N + 1):

            for v, w in road_adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True

            for v, w in worm_adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break

    for u in range(1, N + 1):
        for v, w in road_adj[u]:
            if dist[v] > dist[u] + w:
                negative_cycle = True
                break
        if negative_cycle:
            break
        for v, w in worm_adj[u]:
            if dist[v] > dist[u] + w:
                negative_cycle = True
                break
        if negative_cycle:
            break

    print("YES" if negative_cycle else "NO")
