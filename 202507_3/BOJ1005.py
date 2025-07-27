from collections import deque
import sys
input = sys.stdin.readline


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N: 총 건물 갯수 K: 규칙의 총 갯수
    costs = [0] + list(map(int, input().split()))
    
    # 진입 차수, 인접리스트 생성
    indegree = [0] * (N + 1)
    adj_list = [[] for _ in range(N + 1)]
    
    for _ in range(K):
        p, c = map(int, input().split())
        adj_list[p].append(c)
        indegree[c] += 1
        
    W = int(input())    # 우리의 목표
    
    dp = [0] * (N + 1)
    queue = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = costs[i]
    while queue:
        cur_num = queue.popleft()
        
        for next_num in adj_list[cur_num]:
            # 가능한 놈들 중에 최대로 걸리는 놈만 생각하면 된다
            dp[next_num] = max(dp[next_num], dp[cur_num] + costs[next_num])
            indegree[next_num] -= 1
            
            if indegree[next_num] == 0:
                queue.append(next_num)    
    print(dp[W])