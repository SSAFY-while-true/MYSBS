from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num_list = deque([])
par = [0] * (N+1)

adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


queue = deque([1])
par[1] = 1  


while queue:
    cur = queue.popleft()
    for nxt in adj_list[cur]:
        if par[nxt] == 0:
            par[nxt] = cur
            queue.append(nxt)
        

for num in par[2:]:
    print(num)