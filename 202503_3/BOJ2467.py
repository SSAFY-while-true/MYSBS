import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))

solution.sort()

start_idx = 0
end_idx = N-1

min_val = float('inf')

for _ in range(N-1):
    temp_val = solution[end_idx] + solution[start_idx]
    if temp_val == 0:
        result = [solution[start_idx], solution[end_idx]]
        break
    if abs(temp_val) < min_val:
        min_val = abs(temp_val)
        result = [solution[start_idx], solution[end_idx]]
    
    if temp_val < 0:            # 합이 음수라는 것은  너무 많이 뺏다 작은 쪽이 더 커져야 한다
        start_idx += 1
    
    elif temp_val > 0 :         # 합이 양수라는것은 너무 크게 더했다 큰 쪽이 작아져야 한다.
        end_idx -= 1

print(*result)