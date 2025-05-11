import sys
input = sys.stdin.readline

def recur(x, y, size):
    first = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:    # 같지 않다면 9등분 후 재귀
                next_size = size // 3
                for dx in range(3):
                    for dy in range(3):
                        recur(x + dx * next_size, y + dy * next_size, next_size)
                return
    # 모두 같다면 카운트
    result[first] += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = {
    -1: 0, 
    0: 0, 
    1: 0}

recur(0, 0, N)

print(result[-1])
print(result[0])
print(result[1])