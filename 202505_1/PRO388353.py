from collections import deque

def solution(storage, requests):
    def my_bfs(strat_i, start_j, n, m):
        visited = [[False] * m for _ in range(n)]
        visited[strat_i][start_j] = True
        dq = deque([(strat_i, start_j)])

        while dq:
            cur_i, cur_j = dq.popleft()
            
            for dir in ((1,0),(-1,0),(0,1),(0,-1)):
                ni = cur_i + dir[0] 
                nj = cur_j + dir[1]
                if ni < 0 or nj < 0 or ni == n or nj == m:
                    return True

                if new_storage[ni][nj] == 0:
                    return True
                
                if not visited[ni][nj] and new_storage[ni][nj] == -1:
                    visited[ni][nj] = True
                    dq.append((ni,nj))
        return False

    new_storage = []
    for i in range(len(storage)):
        new_storage.append(list(storage[i]))
    n = len(new_storage)
    m = len(new_storage[0])
    
    answer = 0
    for request in requests:
        if len(request) == 2:
            isall = True
        else:
            isall = False

        for i in range(n):
            for j in range(m):
                if isall:
                    if new_storage[i][j] == request[0]:
                        new_storage[i][j] = -1
                else:
                    if i == 0 or j == 0 or i == n-1 or j == m-1:
                        if new_storage[i][j] == request[0]:
                            new_storage[i][j] = -1
                    else:
                        for dir in [(0,1), (1,0), (0,-1),(-1,0)]:
                            ni = i + dir[0]
                            nj = j + dir[1]
                            
                            if new_storage[ni][nj] == 0 and new_storage[i][j] == request[0]:
                                new_storage[i][j] = -1
                                break
                
        for k in range(n):
            for l in range(m):
                if new_storage[k][l] == -1 and my_bfs(k, l, n, m):
                    new_storage[k][l] = 0


    for i in range(n):
        for j in range(m):
            if type(new_storage[i][j]) == str:
                answer += 1

    return answer
