"""
점화식 fn=2f(n-1)+ f(n-2)
"""
# def count_case(cage):
#     if cage == 1:
#         return 3
#     if cage == 2:
#         return 7
    
#     if dp[cage] != 0:
#         return dp[cage]
    
#     dp[cage] = 2 * count_case(cage-1) + count_case(cage-2)
#     return dp[cage] % 9901

N = int(input())

dp = [0] * 3
dp[0] = 3
dp[1] = 7

for i in range(2, N):
    new_i = i % 3
    dp[new_i] = 2 * dp[new_i-1] + dp[new_i-2]

result = dp[(N-1)%3] % 9901

print(result)

