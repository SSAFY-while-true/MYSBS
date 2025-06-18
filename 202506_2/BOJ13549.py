from collections import deque

def my_bfs(N, K):
    visited = [-1] * 100001
    dq = deque()
    dq.append(N)
    visited[N] = 0

    while dq:
        cur_time = dq.popleft()

        if cur_time == K:
            return visited[cur_time]

        next_time = cur_time * 2
        if 0 <= next_time < 100001 and visited[next_time] == -1:
            visited[next_time] = visited[cur_time]
            dq.appendleft(next_time)

        next_time = cur_time + 1
        if 0 <= next_time < 100001 and visited[next_time] == -1:
            visited[next_time] = visited[cur_time] + 1
            dq.append(next_time)


        next_time = cur_time - 1
        if 0 <= next_time < 100001 and visited[next_time] == -1:
            visited[next_time] = visited[cur_time] + 1
            dq.append(next_time)

N, K = map(int, input().split())
print(my_bfs(N, K))
