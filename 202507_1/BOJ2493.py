import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1  # 탑 번호는 1-based
    stack.append(i)

print(*result)
