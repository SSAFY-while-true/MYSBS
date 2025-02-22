def DFS_campus(campus, start_ij):
    di = [0, 1, 0, -1]
    dj = [1, 0 ,-1, 0]

    stack = [start_ij]
    campus[start_ij[0]][start_ij[1]] = 'X'
    meet_count = 0

    while stack:
        current_i, current_j = stack.pop()
        
        for dir in range(4):
            ni = current_i + di[dir]
            nj = current_j + dj[dir]

            if 0 <= ni < N and 0 <= nj < M:
                if campus[ni][nj] == 'O':
                    campus[ni][nj] = 'X'
                    stack.append((ni, nj))
                    
                elif campus[ni][nj] == 'P': # 사람은 따로 처리해서 숫자를 올려준다
                    meet_count += 1
                    campus[ni][nj] = 'X'
                    stack.append((ni, nj))


    if meet_count == 0:         # 탐색끝나고 처리
        meet_count = 'TT'

    return meet_count


N, M = map(int, input().split())
campus = [list(map(str, input())) for _ in range(N)]

isfind = False
for i in range(N):
    if isfind:
        break
    for j in range(M):
        if campus[i][j] == 'I':
            start_ij = (i, j)
            isfind = True
            break

print(DFS_campus(campus, start_ij))
