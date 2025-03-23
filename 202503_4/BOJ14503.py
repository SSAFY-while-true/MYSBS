import sys
input = sys.stdin.readline


N, M = map(int, input().split())
r, c, d = map(int, input().split())
clean_map = [list(map(int, input().split())) for _ in range(N)]

if d == 1:
    d = 3
elif d == 3:
    d = 1

dr = [-1, 0, 1, 0] 
dc = [0, -1, 0, 1]


result = 1
clean_map[r][c] = 2

while True:
    for _ in range(4):
        d = (d + 1) % 4 
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            if clean_map[nr][nc] == 0:
                result += 1
                clean_map[nr][nc] = 2
                r = nr
                c = nc
                break
    else:
        back_d = (d + 2) % 4

        back_r = r + dr[back_d]
        back_c = c + dc[back_d]

        if 0 <= back_r < N and 0 <= back_c < M and clean_map[back_r][back_c] != 1:
            r = back_r
            c = back_c
            
        else:
            break

print(result)
