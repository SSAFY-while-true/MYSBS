command = list(map(int, input().split()))

# 선택해야 하는 것 오른발? 왼발?
dp = [[[0] * 2 for _ in range(3)]  for _ in range(len(command))]

print(dp)