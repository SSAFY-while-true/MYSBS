"""
끝나는 시간은 가장 짧게
이제부터는 짧게 끝나는 시간중에 시작시간에 맞춰서
"""
import sys
input = sys.stdin.readline

N = int(input())
time_table = [list(map(int, input().split())) for _ in range(N)]

time_table.sort(key=lambda x : (x[1], x[0]))

total_used = 1
end_time = time_table[0][1]

for idx in range(1, N):
    start_time = time_table[idx][0]
    if start_time >= end_time:
        total_used += 1
        end_time = time_table[idx][1]

print(total_used)
