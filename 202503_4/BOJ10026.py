def color_dfs(start_i, start_j):
    stack = [(start_i, start_j)]

    while stack:
        cur_i, cur_j = stack.pop()

        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]

            if 0<=ni<N and 0<=nj<N:
                if not visited[ni][nj] and color_list[cur_i][cur_j] == color_list[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))



def rg_color_dfs(start_i, start_j):
    stack = [(start_i, start_j)]

    while stack:
        cur_i, cur_j = stack.pop()

        for k in range(4):
            ni = cur_i + di[k]
            nj = cur_j + dj[k]

            if 0<=ni<N and 0<=nj<N:
                if not visited2[ni][nj] and color_list[cur_i][cur_j] == color_list[ni][nj]:
                    visited2[ni][nj] = True
                    stack.append((ni, nj))
                elif not visited2[ni][nj] and color_list[cur_i][cur_j] == 'R' and color_list[ni][nj] == 'G':
                    visited2[ni][nj] = True
                    stack.append((ni, nj))
                elif not visited2[ni][nj] and color_list[cur_i][cur_j] == 'G' and color_list[ni][nj] == 'R':
                    visited2[ni][nj] = True
                    stack.append((ni, nj))


N = int(input())
color_list = [list(input()) for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

result1 = 0
result2 = 0
visited = [[False] * N for _ in range(N)] 
visited2 = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            visited[i][j] = True
            color_dfs(i, j)
            result1 += 1

        if visited2[i][j] == 0:
            visited2[i][j] = True
            rg_color_dfs(i, j)
            result2 += 1



print(result1, result2)