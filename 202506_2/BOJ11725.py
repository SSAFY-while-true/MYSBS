from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num_list = deque([])
par = [0] * (N+1)

for _ in range(N-1):
    p, c = map(int, input().split())
    if p == 1:
        par[c] = p
    elif c == 1:
        par[p] = c
    elif par[p] != 0:
        par[c] = p
    elif par[c] != 0:
        par[p] = c
    else:
        num_list.append((p, c))


while num_list:
    pair = num_list.popleft()
    p , c = pair
    if par[p] == 0 and par[c] == 0:
        num_list.append((p, c))
        continue
    else:
        if par[p] != 0:
            par[c] = p
        else:
            par[p] = c
        

for num in par[2:]:
    print(num)