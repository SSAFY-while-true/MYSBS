from collections import deque

def friend_bfs(start):
    visited = {start}
    queue = deque([(start,0)])
    friend_2 = 0

    while queue:
        cur, dist = queue.popleft()
        if dist == 2:
            continue

        for next_num in adj_list[cur]:
            if next_num not in visited:
                visited.add(next_num)
                friend_2 += 1
                queue.append((next_num, dist+1))

    return friend_2

N = int(input())
adj_list = [[] for _ in range(N)]
for friend_num in range(N):
    friendship = list(input())
    for idx in range(N):
        if friendship[idx] == 'Y':
            adj_list[friend_num].append(idx)

result = 0
for num in range(N):
    result = max(result, friend_bfs(num))

print(result)
