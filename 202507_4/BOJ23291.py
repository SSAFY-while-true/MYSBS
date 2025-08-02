from collections import deque
import sys
import copy
input = sys.stdin.readline

# 물고기 나누기
def distributre_fish(move_tank):
    new_tank = copy.deepcopy(move_tank)
    height = len(move_tank)
    width = len(move_tank[-1])
    for i in range(height):
        for j in range(width):
            # 가장 위가 아닐경우 위를본다
            if i != height - 1:
                add_num = (move_tank[i][j] - move_tank[i+1][j]) // 5
                if add_num > 0:
                    new_tank[i][j] -= add_num
                    new_tank[i+1][j] += add_num
            # 가장 아래가 아닐 경우 아래를 본다
            if i != 0:
                add_num = (move_tank[i][j] - move_tank[i-1][j]) // 5
                if add_num > 0:
                    new_tank[i][j] -= add_num
                    new_tank[i-1][j] += add_num

            # 가장 왼쪽이 아닐 경우에 왼쪽을 본다
            if j != 0:
                add_num = (move_tank[i][j] - move_tank[i][j-1]) // 5
                if add_num > 0:
                    new_tank[i][j] -= add_num
                    new_tank[i][j-1] += add_num
            # 가장 오른쪽이 아닐경우 오른쪽을 본다
            if j != width -1:
                add_num = (move_tank[i][j] - move_tank[i][j+1]) // 5
                if add_num > 0:
                    new_tank[i][j] -= add_num
                    new_tank[i][j+1] += add_num
    # 잔반처리
    for k in range(width, len(move_tank[0])):
        # 왼쪽은 항상 본다
        add_num = (move_tank[0][k] - move_tank[0][k-1]) // 5
        if add_num > 0:
            new_tank[0][k] -= add_num
            new_tank[0][k-1] += add_num
        # 가장 오른쪽이 아닐경우 오른쪽을 본다
        if k != len(move_tank[0]) -1:
            add_num = (move_tank[0][k] - move_tank[0][k+1]) // 5
            if add_num > 0:
                new_tank[0][k] -= add_num
                new_tank[0][k+1] += add_num

    return new_tank

# 평탄화 하기
def flatten_tank(move_tank):
    top_len = len(move_tank[-1])
    
    zip_tanks = list(map(list, zip(*move_tank)))
    new_tank = []
    for zip_tank in zip_tanks:
        new_tank.extend(zip_tank)
    
    new_tank.extend(move_tank[0][top_len:])

    return new_tank

def flip():
    pass

# 물고기 배정하기
def lesson1():
    # 그림 1 구현
    min_idxs = []
    min_val = float("INF")
    for idx in range(N):
        if fish_tank[idx] < min_val:
            min_idxs = [idx]
            min_val = fish_tank[idx]
        elif fish_tank[idx] == min_val:
            min_idxs.append(idx)

    for min_idx in min_idxs:
        fish_tank[min_idx] += 1

# 어항을 쌓고 분배하고 다시 내리기
def lesson2(fish_tank):


    move_tank = []
    move_tank.append(fish_tank[1:])
    move_tank.append([fish_tank[0]])

    # print(list(map(list, zip(*move_tank))))
    total_len = 1
    while True:
        floor = len(move_tank)  # 옆으로 넘어갈 길이
        bottom_len = len(move_tank[0]) # 바닥에 남은 길이
        top_len = len(move_tank[-1]) # 밑바닥에서 뺴야할 땅

        if floor > (bottom_len - top_len):  # 더 땅이 없으면
            break
        
        new_tank =list(map(list, zip(*move_tank)))

        total_len += total_len

        move_tank= [fish_tank[total_len:]]
        for idx in range(len(new_tank)-1, -1, -1):
            move_tank.append(new_tank[idx])


    move_tank = distributre_fish(move_tank)
    move_tank = flatten_tank(move_tank)
    return move_tank

def lesson3(fish_tank):
    move_tank = 
        

N, K = map(int, input().split())
fish_tank = list(map(int, input().split()))

setp = 0

lesson1()
fish_tank = lesson2(fish_tank)
fish_tank = lesson3(fish_tank)

print(fish_tank)
