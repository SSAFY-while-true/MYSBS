def solution(info, edges):
    def my_dfs(sheep, wolf, start):
        global answer
        visited = [0] * V
        visited[0] = 1
        stack = [(sheep, wolf, start)]
        
        while stack:
            cur_sheep, cur_wolf, cur_idx = stack.pop()
            answer = max(answer, cur_sheep)



    V = len(info)
    E = len(edges)
    answer = 0
    
    left = [0] *  V
    right = [0] * V
    
    for i in range(E):
        p = edges[i][0]
        c = edges[i][1]
        
        if not left[p]:
            left[p] = c
        else:
            right[p] = c
            
    my_dfs(1, 0, 0)
            
    return answer