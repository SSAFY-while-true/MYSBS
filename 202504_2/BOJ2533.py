import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]  # dp[i][0] = 얼리X, dp[i][1] = 얼리O
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0          # 이 노드를 얼리 어답터로 선택하지 않은 경우
    dp[node][1] = 1          # 이 노드를 얼리 어답터로 선택한 경우

    for child in graph[node]:
        if not visited[child]:
            dfs(child)

            # node가 얼리 어답터가 아닐 경우, 자식은 무조건 얼리 어답터여야 함
            dp[node][0] += dp[child][1]

            # node가 얼리 어답터일 경우, 자식은 얼리여도 되고 아니어도 됨
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)  # 루트를 1로 가정

print(min(dp[1][0], dp[1][1]))
