import sys
input = sys.stdin.readline

N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    if i != N - 1:
        result += (coordinates[i][0] + coordinates[i+1][0]) * (coordinates[i][1] - coordinates[i+1][1])
    else:
        result += (coordinates[-1][0] + coordinates[0][0]) * (coordinates[-1][1] - coordinates[0][1])
print(round(0.5 * abs(result), 1))