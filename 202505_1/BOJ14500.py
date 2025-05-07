import sys
input = sys.stdin.readline

N, M = map(int, input().split())
techno = [list(map(int, input().split())) for _ in range(N)]
techno_dict = {
    1: ((0, 1), (0, 2), (0, 3)),    # 일자 가로
    2: ((1, 0), (2, 0), (3, 0)),    # 일자 세로
    3: ((1, 0), (0, 1), (1, 1)),    # 네모
    4: ((1, 0), (2, 0), (2, 1)),    # ㄴ자
    5: ((1, 0), (2, 0), (2, -1)),    # ㄴ자 대칭
    6: ((-1, 0), (-1, 1), (-1, 2)),    # 90 ㄴ자 
    7: ((1, 0), (1, 1), (1, 2)),    # 90 ㄴ자  대칭
    8: ((0, 1), (1, 1), (2, 1)),    # 180 ㄴ자
    9: ((0, -1), (1, -1), (2, -1)),    # 180 ㄴ자  대칭
    10: ((0, 1), (0, 2), (1, 2)),    # 270 ㄴ자
    11: ((0, 1), (0, 2), (-1, 2)),    # 270 ㄴ자 대칭
    12: ((1, 0), (1, 1), (2, 1)),     # 번개
    13: ((1, 0), (1, -1), (2, -1)),    # 번개 대칭
    14: ((0, 1), (-1, 1), (-1, 2)),    # 번개 돌려
    15: ((0, 1), (1, 1), (1, 2)),    # 번개 돌려 대칭
    16: ((0, 1), (1, 1), (0, 2)),    # ㅜ
    17: ((0, 1), (-1, 1), (0, 2)),    # ㅗ
    18: ((1, 0), (1, -1), (2, 0)),    # ㅓ
    19: ((1, 0), (1, 1), (2, 0)),    # ㅏ
}

# print(tchno_dict[19])
max_result = 0
for i in range(N):
    for j in range(M):
        temp_max = 0
        for num in range(1,20):
            temp_max = 0
            for dir_i, dir_j in techno_dict[num]:
                ni = i + dir_i
                nj = j + dir_j

                if 0<=ni<N and 0<=nj<M:
                    temp_max += techno[ni][nj]
                else:
                    break
            
            else:
                temp_max += techno[i][j]
                max_result = max(max_result, temp_max)

print(max_result)