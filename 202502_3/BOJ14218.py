from collections import deque
# import sys

# input = sys.stdin.readline


def BFS_road(start=0):
    deq = deque([start])
    visited = [-1] * n
    visited[start] = 0

    while deq:
        current_city = deq.popleft()
        
        for next_city in range(n):
            if adj_matrix[current_city][next_city] == 1 and visited[next_city] == -1:
                visited[next_city] = visited[current_city] + 1
                deq.append(next_city)
    
    print(*visited)


n, m = map(int, input().split())

adj_matrix =[[0] * (n) for _ in range(n)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    adj_matrix[n1-1][n2-1] = 1
    adj_matrix[n2-1][n1-1] = 1

# BFS_road()

q = int(input())
for _ in range(q):
    fix1, fix2 = map(int, input().split())
    adj_matrix[fix1-1][fix2-1] = 1
    adj_matrix[fix2-1][fix1-1] = 1
    BFS_road()



