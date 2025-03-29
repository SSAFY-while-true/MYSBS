# 시간을 기준으로 그시간이면 사람을 처리 할수 있었는지를 확인

def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left+ right) // 2
        
        total_human = 0
        for time in times:
            total_human += mid // time
            
        if total_human >= n:
            answer = mid
            
            # 그것보다 적은 시간으로 가능한지 확인
            right = mid - 1
            
        else:
            left = mid + 1 # 큰시간 확인
        
        
    return answer