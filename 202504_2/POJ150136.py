from collections import deque

def solution(land):
    def loaf_bfs(start_i, start_j, section:str):
        queue = deque([(start_i,start_j)])

        while queue:
            cur_i, cur_j = queue.popleft()

            for dir in [(1,0), (0,1), (-1,0), (0,-1)]:
                ni = cur_i + dir[0]
                nj = cur_j + dir[1]

                if 0<=ni< n and 0<=nj<m and land[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = section
                    loaf_dict[section] += 1
                    queue.append((ni, nj))

    answer = 0
    n = len(land)
    m = len(land[0])
    section = 1
    loaf_dict = {}
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                loaf_dict[str(section)] = 1
                visited[i][j] = str(section)
                loaf_bfs(i, j, str(section))
                section += 1

    for jdx in range(m):
        used_num = set()
        temp_max = 0
        for idx in range(n):
            if visited[idx][jdx] != 0 and visited[idx][jdx] not in used_num:
                temp_max += loaf_dict[visited[idx][jdx]]
                used_num.add(visited[idx][jdx])

        answer = max(answer, temp_max)
    

    return answer